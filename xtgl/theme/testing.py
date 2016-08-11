from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

class Base(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import xtgl.theme
        xmlconfig.file('configure.zcml', xtgl.theme, context=configurationContext)
    
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'xtgl.theme:default')

FIXTURE = Base()
INTEGRATION_TESTING = IntegrationTesting(bases=(FIXTURE,), name="Diazotheme:Integration")
FUNCTION_TESTING = FunctionalTesting(bases=(FIXTURE,), name="Diazotheme:Functional")
