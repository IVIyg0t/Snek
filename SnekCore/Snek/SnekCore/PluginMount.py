from typing import List, Any


class PluginMount(type):
    def __init__(cls, name: str, bases: List[Any], attrs: List[Any]):
        """
        This is the __init__ method for plugins. It should be called by
        the mount point to register the plugin with the class

        Args:
            cls: The class which will be used to instantiate the plugin
            name: The name of the plugin ( for debugging purposes )
            bases: The base classes which are implemented by the plugin
            attrs: The attributes which are implemented by the
            plugin ( for debugging purposes )
        """
        # This method is called by the mount point when
        # the mount point is being processed.
        if not hasattr(cls, "plugins"):
            # This branch only executes when processing the mount point itself.
            # So, since this is a new plugin type, not an implementation, this
            # class shouldn't be registered as a plugin. Instead, it sets up a
            # list where plugins can be registered later.
            cls.plugins = []
        else:
            # This must be a plugin implementation, which should be registered.
            # Simply appending it to the list is all that's needed to keep
            # track of it later.
            cls.plugins.append(cls)
