from abc import abstractmethod
from Snek.SnekCore.PluginMount import PluginMount


class SnekMountPoint(metaclass=PluginMount):
    @property
    @abstractmethod
    def snek(self) -> str:
        """
        Return the string to be used as part of the name.
        This is a convenience method for subclasses to implement.


        Returns:
            A string that is the same as the input
            but without the prefix and suffix ( if any ) added
        """
        return ""

    def __str__(self) -> str:
        """
        Returns the snek as a string. This is useful for debugging
        and to avoid having to re - write the string every time it is read.


        Returns:
            The snek as a string or None if
            there is no snek at the moment of reading
        """
        return self.snek
