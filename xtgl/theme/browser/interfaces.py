from zope.interface import Interface

class IPluginSpecific(Interface):
    """   We can reference
    this in the 'layer' attribute of ZCML <browser:* /> directives to ensure
    the relevant registration only takes effect when this plugin is installed. 
    The browser layer (plugin layer) is installed via the browserlayer.xml GenericSetup
    import step.
    """
class IThemeSpecific(Interface):
    """Marker interface that defines a ZTK browser layer. We can reference
    this in the 'layer' attribute of ZCML <browser:* /> directives to ensure
    the relevant registration only takes effect when this theme is selected.
    
    The browser layer is installed via the browserlayer.xml GenericSetup
    import step.
    """

