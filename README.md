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

Emails should be sent using the MailChimp account.

When sending emails to 'All Teams', please send to both the _"Website - Potential Team Leaders"_ and _"Potential Team Leaders"_ lists.
