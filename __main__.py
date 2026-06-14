from rich import box
from rich.console import Console
from rich.table import Table
from readchar import key, readkey
import time



width = 9
height = 9
mines = 10

console = Console()
selected = 0
def printTitle():
    global console, width, height, mines, selected
    console.print("""
█▀▀█  █    ▀█▀      █▀▄▀█  ▀  █▀▀▄ █▀▀ █▀▀ 
█     █     █   ▀▀  █ █ █ ▀█▀ █  █ █▀▀ ▀▀█ 
█▄▄█  █▄▄█ ▄█▄      █   █ ▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀ """
                , style="bold default on default", justify="center")
    console.print("Made with :red_heart-emoji:  by @Aquaticsanti\n\n", style="bold default on default", justify="center")
    
    if selected == 1:
        console.print(f" Width  = {width}", justify="center", style="black on white")
    else:
        console.print(f" Width  = {width}", justify="center")
    if selected == 2:
        console.print(f" Height = {height}", justify="center", style="black on white")
    else:
        console.print(f" Height = {height}", justify="center")
    if selected == 3:
        console.print(f" Mines  = {mines}", justify="center", style="black on white")
    else:
        console.print(f" Mines  = {mines}", justify="center")
    print("\n")
    if selected == 4:
        console.print("""╔════════════════╗
║     Start!     ║
╚════════════════╝""", markup=True, justify="center", style="black on white")
    else:
        console.print("""╔════════════════╗
║     Start!     ║
╚════════════════╝""", markup=True, justify="center")



while True:
    print("\033[16A")
    printTitle()
    k = readkey()
    if k == key.DOWN:
        selected += 1
        if selected > 4:
            selected = 1
    elif k == key.UP:
        selected -= 1
        if selected < 1:
            selected = 4
    elif k == key.LEFT:
        if selected == 1:
            width -= 1
            if width < 1:
                width += 1
        elif selected == 2:
            height -= 1
            if height < 1:
                height += 1
        elif selected == 3:
            mines -= 1
            if mines < 1:
                mines += 1
    elif k == key.RIGHT:
        if selected == 1:
            width += 1
        elif selected == 2:
            height += 1
        elif selected == 3:
            mines += 1
    elif k == key.ENTER and selected == 4:
        break

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


