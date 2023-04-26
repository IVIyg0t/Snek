import typer
import pkg_resources
from rich import print
from Snek.SnekCore.SnekMountPoint import SnekMountPoint

app = typer.Typer()


def load_plugins():
    """
    Load and return all plugins. This is a convenience function for
    use by plugins that need to be loaded in order to get a list of plugins.


    Returns:
        A dictionary of plugin names mapped
            to : class : ` snek. entry_point. EntryPoint `
    """
    plugins = dict()
    # Load plugins from entry points.
    for entry_point in pkg_resources.iter_entry_points("snek_types"):
        plugins[entry_point.name] = entry_point
        entry_point.load()

    return plugins


def get_sneks():
    """
    Get a list of sneks. This is used to check if
    there are any sneks that can be run on this host.


    Returns:
        A list of plugin names to run on this host or an empty list
            if there are none. Note that plugins are loaded in the order they were added
    """
    return [p.__name__ for p in SnekMountPoint.plugins]


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
    load_plugins()
    print(get_sneks())


@app.command()
def get(name: str):
    """
    Get Snek and print it's information. This is a wrapper for get_snek ( name )

    Args:
        name: Name of the Snoek
    """
    load_plugins()
    snek = get_snek(name)

    if snek:
        print(snek().snek)
