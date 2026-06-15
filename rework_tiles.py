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
height = 9
width = 9
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
    """ elif k == key.ENTER:
        discoveryGrid[selected] = 1
        if selected > -1: # So if it ISN'T a mine
            if str(selected)[-1] != "0": # If the square isn't in the left border in a 9x9 grid
                try:
                    if infoGrid[selected-11] > -1: # Top left
                        discoveryGrid[selected-11] = 1 # Set tile to discovered
                except IndexError:
                    pass
            try:
                if infoGrid[selected-10] > -1: # Top middle
                    discoveryGrid[selected-10] = 1 # Set tile to discovered
            except IndexError:
                pass
            if str(selected)[-1] != "9": # If the square isn't in the right border in a 9x9 grid
                try:
                    if infoGrid[selected-9]> -1: # Top right
                        discoveryGrid[i-9] = 1 # Set tile to discovered
                except IndexError:
                    pass
            
            if str(selected)[-1] != "0": # If the square isn't in the left border in a 9x9 grid
                try:
                    if infoGrid[selected-1]> -1: # Middle left
                        discoveryGrid[selected-1] = 1 # Set tile to discovered
                except IndexError:
                    pass
            if str(selected)[-1] != "9": # If the square isn't in the right border in a 9x9 grid
                try:
                    if infoGrid[selected+1 ]> -1: # Middle right
                        discoveryGrid[selected+1] = 1 # Set tile to discovered
                except IndexError:
                    pass
            
            if str(selected)[-1] != "0": # If the square isn't in the left border in a 9x9 grid
                try:
                    if infoGrid[selected+11] > -1: # Bottom left
                        discoveryGrid[selected+11] = 1 # Set tile to discovered
                except IndexError:
                    pass
            try:
                if infoGrid[selected+10] > -1: # Bottom middle
                    discoveryGrid[selected+10] + 1 # Set tile to discovered
            except IndexError:
                pass
            if str(selected)[-1] != "9": # If the square isn't in the right border in a 9x9 grid
                try:
                    if infoGrid[selected+9]> -1: # Bottom right
                        discoveryGrid[selected+9] = 1# Set tile to discovered
                except IndexError:
                    pass """