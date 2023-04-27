from abc import abstractmethod
from Snek.SnekCore.PluginMount import PluginMount


class SnekMountPoint(metaclass=PluginMount):
    # entry_point = "snek_types"

    @property
    @abstractmethod
    def snek(self) -> str:
        """
        The snek function is a simple function that returns the string &quot;snek&quot;

        Args:
            self: Refer to the current instance of a class

        Returns:
            A string

        Doc Author:
            Trelent
        """

        return ""

    def __str__(self) -> str:
        """
        The __str__ function is a special function that returns the string
            representation of an object.
        The __str__ method is called when you use print() or str() on an object.
        This means that if you define a __str__ method, it will be used instead of the
            default one.

        Args:
            self: Represent the instance of the class

        Returns:
            The string representation of the object

        Doc Author:
            Trelent
        """

        return self.snek
