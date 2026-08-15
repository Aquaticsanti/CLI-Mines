from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.live import Live
from rich.align import Align
from readchar import key, readkey
import numpy as np
import os
from playsound3 import playsound

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Default values definition
width = 9
height = 9
mines = 10
soundOn = True

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
    if selected == 4:
        if soundOn:
            console.print(f" Sound  = On", justify="center", style="black on white", highlight=False)
        else:
            console.print(f"  Sound  = Off", justify="center", style="black on white", highlight=False)
    else:
        if soundOn:
            console.print(f" Sound  = On", justify="center", highlight=False)
        else:
            console.print(f"  Sound  = Off", justify="center", highlight=False)
    print("\n")
    if selected == 5:
        console.print("""╔════════════════╗
║     Start!     ║
╚════════════════╝""", markup=True, justify="center", style="black on white", highlight=False)
    else:
        console.print("""╔════════════════╗
║     Start!     ║
╚════════════════╝""", markup=True, justify="center", highlight=False)



while True:
    cls()
    printTitle()
    k = readkey()
    if k == key.DOWN:
        selected += 1
        if selected > 5:
            selected = 1
    elif k == key.UP:
        selected -= 1
        if selected < 1:
            selected = 5
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
        elif selected == 4:
            if soundOn:
                soundOn = False
            else:
                soundOn = True
        if (width * height) < mines:
            mines = width * height
    elif k == key.RIGHT:
        if selected == 1:
            width += 1
        elif selected == 2:
            height += 1
        elif selected == 3:
            mines += 1
            if mines > (height * width):
                mines -= 1
        elif selected == 4:
            if soundOn:
                soundOn = False
            else:
                soundOn = True
    elif k == key.ENTER and selected == 5:
        break

if soundOn == False:
    del playsound
    def playsound(path, block=False):
        """Does nothing. This is a dummy function that replaces playsound from playsound3 if sound is disabled."""
        return
"""
_infoGrid_ guide:
-1 = Mine
0 = Empty
1 - 8 = n mines around cell
"""
firstClick = True
infoGrid = np.zeros((width, height), dtype=int) # Array that holds what cells are what
flat = infoGrid.flatten() # make a copy as a 1D array
flat[-mines:] = -1

"""
_discoveryGrid_ guide:
0 = Undiscovereed
1 = Discovered
"""
discoveryGrid = np.zeros((width, height), dtype=int) # Array that holds which cells have been revealed

"""
_flagGrid guide:
0 = Not flagged
1 = Flagged
"""
flagGrid = np.zeros((width, height), dtype=int) # Array that holds which cells have been flagged

"""
_outcome_ guide:
0 = Game in progress/not started
1 = Won
-1 = Lost
"""
outcome = 0 # Variable that holds outcome of game

"""
_mineGrid_ guide:
0 = No mine here
1 = Mine here
(Just an array to make checking flagged mines easier, copy of infoGrid)
Not defined here.
"""

def printGrid():
    global grid, thisRow, width, height, selected, minesLeft, mines, flagGrid, outcome
    thisRow = []
    grid = Table.grid()
    if outcome == 0:
        try:
            minesLeft = mines - np.count_nonzero(flagGrid)
        except NameError:
            minesLeft = mines
        if minesLeft >= 0:
            grid.title = f"[bold]{minesLeft}[/bold] mines left!"
        else:
            grid.title = f"[bold]{minesLeft}[/bold] mines left?"
        grid.caption = "[underline]Enter[/underline] to open cell, [underline]Backspace[/underline] to flag"
    elif outcome == 1:
        grid.title = f"[bold]0[/bold] mines left!\n[bold][underline]You've Won![/underline][/bold]"
        grid.caption = "[italic]Press Enter to exit[/italic]"
    elif outcome == -1:
        grid.title = f"[bold]{minesLeft}[/bold] mines left...\n[bold][underline]You lost...[/underline][/bold]"
        grid.caption = "[italic]Press Enter to exit[/italic]"
    for x in range(height):
        for y in range(width):
            if selected == (y, x):
                if discoveryGrid[(y, x)] == 1:
                    if infoGrid[(y, x)] == -1:
                        thisRow.append(Panel("✴", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_selected[0]))
                    else:
                        thisRow.append(Panel(f"{infoGrid[(y, x)]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_selected[infoGrid[(y, x)]]))
                else:
                    if flagGrid[(y, x)] == 1:
                        thisRow.append(Panel("🚩", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_selected))
                    else:
                        thisRow.append(Panel(" ", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_selected))
            else:
                if discoveryGrid[(y, x)] == 1:
                    if infoGrid[(y, x)] == -1:
                        thisRow.append(Panel("✴", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_unselected[0]))
                    else:
                        thisRow.append(Panel(f"{infoGrid[(y, x)]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_unselected[infoGrid[(y, x)]]))
                else:
                    if flagGrid[(y, x)] == 1:
                        thisRow.append(Panel("🚩", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_unselected))
                    else:
                        thisRow.append(Panel(" ", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_unselected))
        grid.add_row(*thisRow)
        thisRow = []
    return grid


def discover_and_adjacents(y, x):
    global infoGrid, discoveryGrid
    discoveryGrid[(y, x)] = 1
    if infoGrid[(y, x)] != 0:
        return
    neighbours = [
        (y, x-1),   # Middle left
        (y, x+1),   # Middle right
        (y+1, x),   # Bottom middle
        (y-1, x),   # Top middle
        (y+1, x+1), # Bottom right
        (y-1, x-1), # Top left
        (y+1, x-1), # Bottom left
        (y-1, x+1)] # Top right
    neighboursToRemove = []
    for item, pos in enumerate(neighbours): # Delete any that are negative/bigger than the board
        if pos[0] < 0 or pos[1] < 0 or pos[0] > width-1 or pos[1] > height-1:
            neighboursToRemove.append(item)
    for item in neighboursToRemove:
        neighbours[item] = None
    while True:
        try:
            neighbours.remove(None)
        except ValueError:
            break
    for pos in neighbours:
        if infoGrid[pos] == 0 and discoveryGrid[pos] == 0:
            discover_and_adjacents(*pos)
        else:
            if infoGrid[pos] != -1:
                discoveryGrid[pos] = 1

selected = (0, 0)
cls()
with Live(Align.center(printGrid()), refresh_per_second=30, console=console) as live:
    while True:
        if outcome == 0:
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
            elif k == key.BACKSPACE:
                if discoveryGrid[(selected[0], selected[1])] == 0:
                    playsound("sfx/flag.wav", block=False)
                    
                    if flagGrid[(selected[0], selected[1])] == 0:
                        flagGrid[(selected[0], selected[1])] = 1
                        try:
                            if np.array_equal(flagGrid, mineGrid):
                                    outcome = 1
                        except NameError:
                            pass
                    else:
                        flagGrid[(selected[0], selected[1])] = 0
                else:
                    pass
            elif k == key.ENTER:
                if flagGrid[(selected[0], selected[1])] == 1:
                    continue
                if firstClick == True:
                    firstClick = False
                    safe = [] # NOTE: From this line until the 13 next AI was used. 
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            ny = selected[0] + dy
                            nx = selected[1] + dx
                            if 0 <= ny < width and 0 <= nx < height:
                                safe.append(ny * height + nx)
                    positions = []
                    for i in range(len(flat)):
                        if i not in safe:
                            positions.append(i)
                    values = flat[positions]
                    np.random.shuffle(values)
                    flat[positions] = values
                    infoGrid = flat.reshape(width, height)
                    mineGrid = infoGrid.copy()
                    for h in range(height):
                        for w in range(width):
                            try:
                                if mineGrid[(h, w)] != -1:
                                    mineGrid[(h, w)] = 0
                            except IndexError: # I honestly don't know but it happened
                                pass
                    for h in range(height):
                        for w in range(width):
                            try:
                                if mineGrid[(h, w)] == -1:
                                    mineGrid[(h, w)] = 1
                            except IndexError: # I honestly don't know but it happened
                                pass
                    for i in range(width):
                        for j in range(height):
                            if infoGrid[(i, j)] != -1:
                                pass
                            else:
                                if j+1 <= height-1:
                                    if infoGrid[(i, j+1)] > -1:
                                        infoGrid[(i, j+1)] += 1
                                if j-1 >= 0:
                                    if infoGrid[(i, j-1)] > -1:
                                        infoGrid[(i, j-1)] += 1
                                if i+1 <= width-1:
                                    if infoGrid[(i+1, j)] > -1:
                                        infoGrid[(i+1, j)] += 1
                                if i-1 >= 0:
                                    if infoGrid[(i-1, j)] > -1:
                                        infoGrid[(i-1, j)] += 1
                                if i-1 >= 0 and j-1 >= 0:
                                    if infoGrid[(i-1, j-1)] > -1:
                                        infoGrid[(i-1, j-1)] += 1
                                if i+1 <= width-1 and j+1 <= height-1:
                                    if infoGrid[(i+1, j+1)] > -1:
                                        infoGrid[(i+1, j+1)] += 1
                                if i+1 <= width-1 and j-1 >= 0:
                                    if infoGrid[(i+1, j-1)] > -1:
                                        infoGrid[(i+1, j-1)] += 1
                                if i-1 >= 0 and j+1 <= height-1:
                                    if infoGrid[(i-1, j+1)] > -1:
                                        infoGrid[(i-1, j+1)] += 1
                discover_and_adjacents(selected[0], selected[1])
                if infoGrid[(selected[0], selected[1])] == -1:
                    playsound("sfx/explosion.wav", block=False)
                    outcome = -1
                else:
                    playsound("sfx/shovel.wav", block=False)
            live.update(Align.center(printGrid()))
        else:
            input()
            break