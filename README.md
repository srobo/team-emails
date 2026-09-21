# Emails

[![CircleCI](https://circleci.com/gh/srobo/team-emails.svg?style=svg)](https://circleci.com/gh/srobo/team-emails)

A history of communication with teams. Organised by event and date sent. If it's in `master`, it's been sent!

If an email contains links to forms, or other potentially sensitive information, leave the link out of the emails!

## Setup

You'll want an editor which supports markdown files with YAML front-matter.
You're also encouraged to use an editor which supports [EditorConfig](https://editorconfig.org/) either directly or via an extension.

## How to define emails

Emails are defined as markdown files with YAML front-matter.
The front-matter should always contain at least `to` and `subject` keys.
The markdown should be rendered to HTML before sending; the VSCode markdown preview is a reasonable way to do this.

## How to send emails

### Within a competition cycle

During a competition cycle the emails can be sent in one of two ways.
Since we offer teams the option of having their secondary contact(s) CCd into emails, we are unable to use GMail's mail merge feature.

For either of these routes you will need to have configured your SR GMail account to be able to send from `teams@`.

#### Personalised emails

1. Set up a Python virtual environment and `pip install -r scripts/requirements.txt`
1. Export as a CSV the "Combined" tab of the current year's "Teams Organisation (internal)" spreadsheet
1. Pre-process that file using `./scripts/process-export.py $EXPORTED.csv > $EXPORTED.processed.csv`
1. Send the email using `./scripts/send.py`:
    1. Create a fresh "app password" for your account for use by the script; set that via ` export SMTP_PASSWORD=...`
    1. Set your username via `export SMTP_USERNAME=...`
    1. Dry-run the send via the `--dry-run`, check that the printed output is what you expect
    1. You may also want to dummy send the email to yourself; this requires creating a dummy CSV with equivalent columns to the processed file and then sending the email. Be sure you're sending to the right file when doing this!
    1. Send the actual email. For 30 teams this takes a couple of minutes as the script rate-limits itself to avoid hitting GMail sending limits.
    1. Delete from your account the app password you created in the earlier step

#### Mailshots

When no personalisation is needed, the email can be sent as a mailshot.
This involves:

* Rendering the email markdown yourself (VSCode's preview tab does this well for example)
* Identifying the recipient email addresses yourself (don't forget to include the secondary contacts for teams requesting that)
* Composing the email in your own SR GMail account
* Setting the email to be sent from `teams@`
* Setting the email as `To` `teams@`
* Putting all the recipient emails in the `BCC` field
* Copy/pasting the rendered email body into the email

### Outside a competition cycle

Emails should be sent using the MailChimp account.

When sending emails to 'All Teams', please send to both the _"Website - Potential Team Leaders"_ and _"Potential Team Leaders"_ lists.
