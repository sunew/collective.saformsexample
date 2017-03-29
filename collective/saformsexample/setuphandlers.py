# -*- coding: utf-8 -*-
from logging import getLogger

log = getLogger('collective.saformsexample:install')


def post_install(context):
    """Post install script"""
    if context.readDataFile('collectivesaformsexample_marker.txt') is None:
        return
    # Do something during the installation of this package
    portal = context.getSite()  # noqa: F841
    log.info("Running install: setuphandlers.")


def post_install_initialsetup(context):
    """Post install script for initialsetup profile
       - only to be run once.
    """
    if context.readDataFile('collectivesaformsexample_initialsetup_marker.txt') is None:
        return
    # Do something during the installation of this package
    portal = context.getSite()  # noqa: F841
