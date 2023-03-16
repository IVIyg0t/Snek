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
        return SIMPLE_SNEK
