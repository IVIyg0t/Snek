import typer
from rich import print
from Snek.SnekCore.SnekMountPoint import SnekMountPoint

app = typer.Typer()


def get_sneks():
    """
    Get a list of sneks. This is used to check if
    there are any sneks that can be run on this host.


    Returns:
        A list of plugin names to run on this host or an empty list
            if there are none. Note that plugins are loaded in the order they were added
    """
    if len(SnekMountPoint.plugins) == 0:
        SnekMountPoint.load()

    return list(SnekMountPoint.plugins.keys())


def get_snek(name):
    """
    Get snek by name. Will print error if snek doesn't exist.
    Use this to get plugins that are part of a snek

    Args:
        name: name of the plug - in

    Returns:
        plugin or None if not found or error while trying
            to get snek by name ( no plugin found
    """
    try:
        return next(filter(lambda p: p.__name__ == name, SnekMountPoint.plugins))
    except Exception:
        print("[red]Oops! Snek doesn't exist.[/red]")
        print("[yellow]Try `snek list` to see a list of available sneks.[/yellow]")


@app.command("list")
def list_sneks():
    """
    List sneks and their configuration in the config.py file.
    This is a wrapper around get_sneks
    """
    print(get_sneks())


@app.command()
def get(name: str):
    """
    Get Snek and print it's information. This is a wrapper for get_snek ( name )

    Args:
        name: Name of the Snoek
    """
    snek = get_snek(name)

    if snek:
        print(snek().snek)
