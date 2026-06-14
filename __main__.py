from rich import box
from rich.console import Console
from rich.table import Table
from readchar import key, readkey
import time



width = 9
height = 9
mines = 10

console = Console()

def printTitle():
    global console, width, height, mines
    console.print("""
█▀▀█  █    ▀█▀      █▀▄▀█  ▀  █▀▀▄ █▀▀ █▀▀ 
█     █     █   ▀▀  █ █ █ ▀█▀ █  █ █▀▀ ▀▀█ 
█▄▄█  █▄▄█ ▄█▄      █   █ ▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀ \n\n"""
                , style="bold default on default", justify="center")
    
    console.print(f" Width  = {width}", justify="center")
    console.print(f" Height = {height}", justify="center")
    console.print(f" Mines  = {mines}", justify="center")
    console.print("""
╔════════════════╗
║     [bold]Start![/bold]     ║
╚════════════════╝""", markup=True, justify="center")



printTitle()

# For later!
#table = Table(title="", box=box.SQUARE, show_lines=True)
#
#for i in range(width):
#    table.add_column(width=2)
#
#for i in range(height-1):
#    table.add_row()
#
#console.print(table)


