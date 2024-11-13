import argparse
import csv
import dataclasses
import functools
import html
import os
import smtplib
import time
from collections.abc import Collection
from email.headerregistry import Address
from email.mime.text import MIMEText
from pathlib import Path

import markdown
import yaml

SMTP_USERNAME = os.environ['SMTP_USERNAME']
SMTP_PASSWORD = os.environ['SMTP_PASSWORD']
SMTP_HOST = os.environ.get('SMTP_HOST', 'smtp.gmail.com')

SR_TEAMS_EMAIL = 'teams@studentrobotics.org'
SR_TEAMS_ADDRESS = Address("Student Robotics Teams", addr_spec=SR_TEAMS_EMAIL)

FROM_EMAIL = SR_TEAMS_EMAIL
FROM_ADDRESS = SR_TEAMS_ADDRESS


@dataclasses.dataclass
class Template:
    to: str
    subject: str
    body_raw: str

    @functools.cached_property
    def body(self) -> str:
        return markdown.markdown(self.body_raw).replace('\\\n', '<br>')

    def template(self, mapping: dict[str, str]) -> str:
        # Note: this requires manual adjustment of the template and CSV file to
        # have matching names, but that seems fine for now. Perhaps we should
        # move to using Jinja templating or something?
        return self.body.format(**{
            k: html.escape(v)
            for k, v in mapping.items()
        })


def load_template(path: Path) -> Template:
    with path.open() as f:
        docs = yaml.load_all(f, Loader=yaml.CLoader)
        metadata = next(docs)

        f.seek(0)
        content = f.read()
        body = content.split('---\n')[-1]
        return Template(
            to=metadata['to'],
            subject=metadata['subject'],
            body_raw=body,
        )


def send(
    server: smtplib.SMTP,
    *,
    to: Address,
    cc: Collection[Address] = (),
    from_: Address = FROM_ADDRESS,
    subject: str,
    html_body: str,
    dry_run: bool,
) -> None:
    message = MIMEText(html_body, 'html')
    message['Subject'] = subject
    message['From'] = str(from_)
    message['To'] = str(to)
    message['CC'] = ', '.join(str(x) for x in cc)

    print(f"Sending to {to!r}, cc {cc!r}")
    if dry_run:
        print('===')
        print(message)
        print('===')
    else:
        server.sendmail(str(from_), str(to), message.as_string())
    print(f"Sent to {to.addr_spec!r}")


def main(args: argparse.Namespace) -> None:
    template = load_template(args.template)

    with smtplib.SMTP_SSL(SMTP_HOST, 465) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        with args.teams_csv.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                cc = [
                    SR_TEAMS_ADDRESS,
                ]
                if row['SecondaryCcSecondary'] == 'TRUE':
                    cc.append(
                        Address(
                            row['SecondaryName'],
                            addr_spec=row['SecondaryEmailAddress'],
                        ),
                    )

                send(
                    server,
                    to=Address(
                        row['PrimaryName'],
                        addr_spec=row['PrimaryEmailAddress'],
                    ),
                    cc=cc,
                    subject=template.subject,
                    html_body=template.template(row),
                    dry_run=args.dry_run
                )

                # Rate limit for GMail
                time.sleep(5)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('template', type=Path)
    parser.add_argument('teams_csv', type=Path)
    parser.add_argument('--dry-run', action='store_true', default=False)
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
