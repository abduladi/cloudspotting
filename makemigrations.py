#!/usr/bin/env python
import os
import sys

import django

from django.conf import settings


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",

        # theme
        "bootstrapform",
        "pinax_theme_bootstrap",

        # external
        "account",
        "pinax.eventlog",
        "pinax.images",
        "pinax.likes",
        "pinax.webanalytics",

        # project
        "cloudspotting",
        "cloudspotting.tests"
    ],
    MIDDLEWARE_CLASSES=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    SITE_ID=1,
    ROOT_URLCONF="cloudspotting.tests.urls",
    SECRET_KEY="notasecret",
)


def run(*args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.core.management.call_command(
        "makemigrations",
        "cloudspotting",
        *args
    )


if __name__ == "__main__":
    run(*sys.argv[1:])
