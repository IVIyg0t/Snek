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
        Return the snek value. This is used to distinguish between a non - existent
        value and a null value that can be read by : meth : ` read `.


        Returns:
            the string to read or None if there is
            no value to read or an empty string if the value is
        """
        return SIMPLE_SNEK
