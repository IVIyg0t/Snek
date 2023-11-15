from Snek.SnekCore.SnekMountPoint import SnekMountPoint

CUTE_SNEK = r"""[green]
                    /^\/^\
                  _|__|  O|
         \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~ 
                        ~--______-~                ~-___-~
[/green]"""


class CuteSnek(SnekMountPoint):
    @property
    def snek(self) -> str:
        """
        The snek function returns a cute snek

        Args:
            self: Refer to the object itself

        Returns:
            The string cute_snek

        Doc Author:
            Trelent
        """

        return CUTE_SNEK
