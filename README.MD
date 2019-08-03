# My Personal Website

Small Django app that powers [my personal site and blog](javierfajardo.com).

It's made to be extremely basic while allowing some extended functionality.

## Installation

Run the `setupVirtualEnv.{sh,bat}` script in order to get a local environment up and running for quick iterations.

You need to have Python 3 installed on your machine. Docker is optional for Production like deployments.

## Running the App

For quick development, use `source startVirtualEnv.bat` and then run `python manage.py runserver`.

The Dockerfile is used to mimic a production deployment to the server and can be quickly run by using `runDocker.ps1`. Don't mind the extension, it'll work on *nix environments too.
