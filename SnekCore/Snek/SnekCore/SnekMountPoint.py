from abc import abstractmethod
from Snek.SnekCore.PluginMount import PluginMount


class SnekMountPoint(metaclass=PluginMount):
    @property
    @abstractmethod
    def snek(self) -> str:
        """Get the Snek

        Returns
        -------
        str
            The Snek
        """
        return ""

    def __str__(self) -> str:
        return self.snek
