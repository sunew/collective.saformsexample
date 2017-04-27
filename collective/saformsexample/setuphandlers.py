# -*- coding: utf-8 -*-
from logging import getLogger
from .model.base import setup_db

log = getLogger('collective.saformsexample:install')


def post_install(context):
    """Post install script"""
    if context.readDataFile('collectivesaformsexample_marker.txt') is None:
        return
    # Do something during the installation of this package
    portal = context.getSite()  # noqa: F841
    log.info("Setting up db tables...")
    setup_db()
    log.info("Setup db tables - OK")


def post_install_initialsetup(context):
    """Post install script for initialsetup profile
       - only to be run once.
    """
    if context.readDataFile('collectivesaformsexample_initialsetup_marker.txt') is None:
        return
    # Do something during the installation of this package
    portal = context.getSite()  # noqa: F841
