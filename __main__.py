from rich import box
from rich.console import Console
from rich.panel import Panel
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
        console.print(f" Width  = {width}", justify="center", style="black on white", highlight=False)
    else:
        console.print(f" Width  = {width}", justify="center", highlight=False)
    if selected == 2:
        console.print(f" Height = {height}", justify="center", style="black on white", highlight=False)
    else:
        console.print(f" Height = {height}", justify="center", highlight=False)
    if selected == 3:
        console.print(f" Mines  = {mines}", justify="center", style="black on white", highlight=False)
    else:
        console.print(f" Mines  = {mines}", justify="center", highlight=False)
    print("\n")
    if selected == 4:
        console.print("""╔════════════════╗
║     Start!     ║
╚════════════════╝""", markup=True, justify="center", style="black on white", highlight=False)
    else:
        console.print("""╔════════════════╗
║     Start!     ║
╚════════════════╝""", markup=True, justify="center", highlight=False)



""" while True:
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

print("\n\n\n\n") """

width += 1 # I know this is weird, but else 9x9 doesn't look square
def printGrid():
    global grid, fullGrid, thisRow, width, height, selected
    grid = Table.grid()
    fullGrid = []
    thisRow = []
    for i in range(width*height):
        if i == selected:
            thisRow.append(Panel(f"{i}", box=box.SQUARE, width=6, height=3, style="#808080 on white"))
        else:
            thisRow.append(Panel(f"{i}", box=box.SQUARE, width=6, height=3, style="white on #808080"))
        if len(thisRow) == width:
            fullGrid.append(thisRow)
            grid.add_row(*thisRow)
            thisRow = []
    console.print(grid, justify="center")


selected = 0
while True:
    print(f"\033[{(height*3)+1}A")
    printGrid()
    k = readkey()
    if k == key.DOWN:
        selected += 10
        if selected > (height*10)-10:
            selected -= 10
    elif k == key.UP:
        selected -= 10
        if selected < 0:
            selected += 10
    elif k == key.LEFT:
        selected -= 1
        if selected < 0:
            selected += 1
    elif k == key.RIGHT:
        selected += 1
        if selected > (width*height)-1:
            selected -= 1





 