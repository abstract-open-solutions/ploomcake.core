# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('ploomcake.core')


def uninstall(portal, reinstall=False):
    if not reinstall:
        # Don't want to delete stuff on reinstall
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-ploomcake.core:uninstall')
        logger.info("Uninstalled")
