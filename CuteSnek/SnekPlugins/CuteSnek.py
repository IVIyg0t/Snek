from Snek.SnekCore.SnekMountPoint import SnekMountPoint

CUTE_SNEK = """[green]
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
        return CUTE_SNEK
