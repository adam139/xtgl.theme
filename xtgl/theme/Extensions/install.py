# -*- coding: utf8 -*-

from xtgl.theme import logger 

#def install(portal, reinstall=False):
#    # Not needed if you don't need to run different profile conditionally
#    setup_tool = portal.portal_setup
#    setup_tool.runAllImportStepsFromProfile('profile-example.gs:default')
#    logger.info("Installed")



def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-xtgl.theme:uninstall')

        logger.info("Uninstall done")
