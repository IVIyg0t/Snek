from Snek.SnekCore.SnekMountPoint import SnekMountPoint

FANCY_SNEK = """[green]\
                          _,..,,,_
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
[/green]"""


class FancySnek(SnekMountPoint):
    @property
    def snek(self) -> str:
        """
        The snek function returns a string containing the ASCII art of a snek.

        Args:
            self: Refer to the instance of the class

        Returns:
            A string

        Doc Author:
            Trelent
        """

        return FANCY_SNEK
