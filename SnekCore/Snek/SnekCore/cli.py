import typer
import pkg_resources
from rich import print
from Snek.SnekCore.SnekMountPoint import SnekMountPoint

app = typer.Typer()


def load_plugins():
    plugins = dict()
    for entry_point in pkg_resources.iter_entry_points("snek_types"):
        plugins[entry_point.name] = entry_point
        entry_point.load()

    return plugins


def get_sneks():
    return [p.__name__ for p in SnekMountPoint.plugins]


def get_snek(name):
    try:
        return next(
            filter(lambda p: p.__name__ == name, SnekMountPoint.plugins)
        )
    except:
        print("[red]Oops! Snek doesn't exist.[/red]")
        print(
            "[yellow]Try `snek list` to see a list of available sneks.[/yellow]"
        )


@app.command("list")
def list_sneks():
    load_plugins()
    print(get_sneks())


@app.command()
def get(name: str):
    """List available types of Sneks."""
    load_plugins()
    snek = get_snek(name)
    if snek:
        print(snek().snek)
