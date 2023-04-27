from Snek.SnekCore.SnekMountPoint import SnekMountPoint

SIMPLE_SNEK = """[green]\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
[/green]"""


class SimpleSnek(SnekMountPoint):
    @property
    def snek(self) -> str:
        """
        The snek function returns a simple snek string.


        Args:
            self: Refer to the object itself

        Returns:
            The string 'snek'

        Doc Author:
            Trelent
        """

        return SIMPLE_SNEK
