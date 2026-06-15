from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from readchar import key, readkey
import random
import time
import numpy as np


# Default values definition
width = 9
height = 9
mines = 10

# Style definition
class styles:
    hidden_selected = Style.parse("#606060 on white")
    hidden_unselected = Style.parse("white on #606060")

    shown_selected = {
        0: Style.parse("#808080 on white"),
        1: Style.parse("#808080 on blue"),
        2: Style.parse("#808080 on green"),
        3: Style.parse("#808080 on red"),
        4: Style.parse("#808080 on purple"),
        5: Style.parse("#808080 on #550000"),
        6: Style.parse("#808080 on cyan"),
        7: Style.parse("#808080 on black"),
        8: Style.parse("#808080 on #909090")
    }

    shown_unselected = {
        0: Style.parse("white on #808080"),
        1: Style.parse("blue on #808080"),
        2: Style.parse("green on #808080"),
        3: Style.parse("red on #808080"),
        4: Style.parse("purple on #808080"),
        5: Style.parse("#550000 on #808080"),
        6: Style.parse("cyan on #808080"),
        7: Style.parse("black on #808080"),
        8: Style.parse("#909090 on #808080")
    }



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

print("\n\n\n\n")

"""
_infoGrid_ guide:
-1 = Mine
0 = Empty
1 - 8 = n mines around cell
"""
infoGrid = np.zeros((width, height), dtype=int) # Array that holds what cells are what
flat = infoGrid.flatten() # make a copy as a 1D array
flat[-10:] = -1
np.random.shuffle(flat)
infoGrid = flat.reshape(width, height)
for i in range(width):
    for j in range(height):
        if infoGrid[(i, j)] != -1:
            pass
        else:
            try:
                if infoGrid[(i, j+1)] > -1:
                    infoGrid[(i, j+1)] += 1
            except:
                pass
            try:
                if infoGrid[(i, j-1)] > -1:
                    infoGrid[(i, j-1)] += 1
            except:
                pass
            try:
                if infoGrid[(i+1, j)] > -1:
                    infoGrid[(i+1, j)] += 1
            except:
                pass
            try:
                if infoGrid[(i-1, j)] > -1:
                    infoGrid[(i-1, j)] += 1
            except:
                pass
            try:
                if infoGrid[(i-1, j-1)] > -1:
                    infoGrid[(i-1, j-1)] += 1
            except:
                pass
            try:
                if infoGrid[(i+1, j+1)] > -1:
                    infoGrid[(i+1, j+1)] += 1
            except:
                pass
            try:
                if infoGrid[(i+1, j-1)] > -1:
                    infoGrid[(i+1, j-1)] += 1
            except:
                pass
            try:
                if infoGrid[(i-1, j+1)] > -1:
                    infoGrid[(i-1, j+1)] += 1
            except:
                pass


"""
_discoveryGrid_ guide:
0 = Undiscovereed
1 = Discovered
"""
discoveryGrid = np.zeros((width, height), dtype=int) # Array that holds which cells have been revealed




def printGrid():
    global grid, thisRow, width, height, selected
    thisRow = []
    grid = Table.grid()
    for x in range(height):
        for y in range(width):
            if selected == (y, x):
                if discoveryGrid[(y, x)] == 1:
                    if infoGrid[(y, x)] == -1:
                        thisRow.append(Panel("✴", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_selected[0]))
                    else:
                        thisRow.append(Panel(f"{infoGrid[(y, x)]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_selected[infoGrid[(y, x)]]))
                else:
                    thisRow.append(Panel(" ", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_selected))
            else:
                if discoveryGrid[(y, x)] == 1:
                    if infoGrid[(y, x)] == -1:
                        thisRow.append(Panel("✴", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_unselected[0]))
                    else:
                        thisRow.append(Panel(f"{infoGrid[(y, x)]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_unselected[infoGrid[(y, x)]]))
                else:
                    thisRow.append(Panel(" ", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_unselected))
        grid.add_row(*thisRow)
        thisRow = []
    console.print(grid, justify="center")


def discover_and_adjacents(y, x):
    global discoveryGrid, infoGrid
    discoveryGrid[(y, x)] = 1
    if infoGrid[(y, x)] > -1 and infoGrid[(y, x)] < 1:
        try:
            if infoGrid[((y, x)[0], (y, x)[1]+1)] > -1:
                discoveryGrid[((y, x)[0], (y, x)[1]+1)] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0], (y, x)[1]-1)] > -1:
                discoveryGrid[((y, x)[0], (y, x)[1]-1)] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0]+1, (y, x)[1])] > -1:
                discoveryGrid[((y, x)[0]+1, (y, x)[1])] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0]-1, (y, x)[1])] > -1:
                discoveryGrid[((y, x)[0]-1, (y, x)[1])] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0]-1, (y, x)[1]-1)] > -1:
                discoveryGrid[((y, x)[0]-1, (y, x)[1]-1)] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0]+1, (y, x)[1]+1)] > -1:
                discoveryGrid[((y, x)[0]+1, (y, x)[1]+1)] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0]+1, (y, x)[1]-1)] > -1:
                discoveryGrid[((y, x)[0]+1, (y, x)[1]-1)] = 1
        except:
            pass
        try:
            if infoGrid[((y, x)[0]-1, (y, x)[1]+1)] > -1:
                discoveryGrid[((y, x)[0]-1, (y, x)[1]+1)] = 1
        except:
            pass

selected = (0, 0)
while True:
    print(f"\033[{(width*3)+1}A")
    printGrid()
    k = readkey()
    if k == key.RIGHT:
        selected = (selected[0]+1, selected[1])
        if selected[0] > width-1:
            selected = (selected[0]-1, selected[1])
    elif k == key.LEFT:
        selected = (selected[0]-1, selected[1])
        if selected[0] < 0:
            selected = (selected[0]+1, selected[1])
    elif k == key.UP:
        selected = (selected[0], selected[1]-1)
        if selected[1] < 0:
            selected = (selected[0], selected[1]+1)
    elif k == key.DOWN:
        selected = (selected[0], selected[1]+1)
        if selected[1] > height-1:
            selected = (selected[0], selected[1]-1)
    elif k == key.ENTER:
        discover_and_adjacents(selected[0], selected[1])
        try:
            if infoGrid[(selected[0], selected[1]+1)] > -1:
                discover_and_adjacents(selected[0], selected[1]+1)
        except:
            pass
        try:
            if infoGrid[(selected[0], selected[1]-1)] > -1:
                discover_and_adjacents(selected[0], selected[1]-1)
        except:
            pass
        try:
            if infoGrid[(selected[0]+1, selected[1])] > -1:
                discover_and_adjacents(selected[0]+1, selected[1])
        except:
            pass
        try:
            if infoGrid[(selected[0]-1, selected[1])] > -1:
                discover_and_adjacents(selected[0]-1, selected[1])
        except:
            pass
        try:
            if infoGrid[(selected[0]-1, selected[1]-1)] > -1:
                discover_and_adjacents(selected[0]-1, selected[1]-1)
        except:
            pass
        try:
            if infoGrid[(selected[0]+1, selected[1]+1)] > -1:
                discover_and_adjacents(selected[0]+1, selected[1]+1)
        except:
            pass
        try:
            if infoGrid[(selected[0]+1, selected[1]-1)] > -1:
                discover_and_adjacents(selected[0]+1, selected[1]-1)
        except:
            pass
        try:
            if infoGrid[(selected[0]-1, selected[1]+1)] > -1:
                discover_and_adjacents(selected[0]-1, selected[1]+1)
        except:
            pass