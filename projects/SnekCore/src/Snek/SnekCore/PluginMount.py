# from abc import ABCMeta
# from typing import List, Any

# import pkg_resources


# class PluginMount(ABCMeta):
#     REQUIRED_STATIC_PROPERTIES = ["entry_point"]

#     def __init__(cls: Any, name: str, bases: List[Any], attrs: List[Any]) -> None:
#         """
#         The __init__ function is called when a new class is created. It's the
#         equivalent of a constructor in other languages, but it's not required to
#         return an instance of the class. Instead, it can modify the attributes of
#         the newly-created class object before Python starts initializing it.

#         Args:
#             cls: Any: Pass the class object to the __init__ function
#             name: str: Store the name of the class
#             bases: List[Any]: Define the base classes of the plugin
#             attrs: List[Any]: Pass the attributes of the class being created

#         Returns:
#             None, which means that plugin classes won't

#         Doc Author:
#             Trelent
#         """

#         if not hasattr(cls, "plugins"):
#             # This branch only executes when processing the mount point itself.
#             # So, since this is a new plugin type, not an implementation, this
#             # class shouldn't be registered as a plugin. Instead, it sets up a
#             # list where plugins can be registered later.
#             cls.plugins = {}
#         else:
#             # This must be a plugin implementation, which should be registered.
#             # Simply appending it to the list is all that's needed to keep
#             # track of it later.
#             cls.plugins[cls.__name__] = cls

#     def verify_attributes(cls):
#         for base in set(cls.__mro__):
#             not_implemented = set(cls.REQUIRED_STATIC_PROPERTIES) - set(
#                 base.__dict__.keys()
#             )
#             if not_implemented:
#                 raise NotImplementedError(
#                     f"Attribute(s) {not_implemented} not implemented by class {base.__name__}"
#                 )

#     def load(cls):
#         cls.verify_attributes()
#         for entry_point in pkg_resources.iter_entry_points(cls.entry_point):
#             entry_point.load()
