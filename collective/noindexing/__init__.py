def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    import patches
    patches.apply()
