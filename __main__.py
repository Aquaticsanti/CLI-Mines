from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from readchar import key, readkey
import random
import time


# Default values definition
width = 9
height = 9
mines = 10

# Style definition
class styles:
    hidden_selected = Style.parse("#606060 on white")
    hidden_unselected = Style.parse("white on #606060")

    shown_0_selected = Style.parse("#808080 on white")
    shown_0_unselected = Style.parse("white on #808080")

    shown_1_selected = Style.parse("#808080 on blue")
    shown_1_unselected = Style.parse("blue on #808080")

    shown_2_selected = Style.parse("#808080 on green")
    shown_2_unselected = Style.parse("green on #808080")

    shown_3_selected = Style.parse("#808080 on red")
    shown_3_unselected = Style.parse("red on #808080")

    shown_4_selected = Style.parse("#808080 on purple")
    shown_4_unselected = Style.parse("purple on #808080")

    shown_5_selected = Style.parse("#808080 on #550000")
    shown_5_unselected = Style.parse("#550000 on #808080")

    shown_6_selected = Style.parse("#808080 on cyan")
    shown_6_unselected = Style.parse("cyan on #808080")

    shown_7_selected = Style.parse("#808080 on black")
    shown_7_unselected = Style.parse("black on #808080")

    shown_8_selected = Style.parse("#808080 on #909090")
    shown_8_unselected = Style.parse("#909090 on #808080")



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


"""
_infoGrid_ guide:
-1 = Mine
0 = Empty
1 - 8 = n mines around cell
"""
width += 1 # I know this is weird, but else 9x9 doesn't look square. Was going to remove it but then everything else broke

infoGrid = [] # List that holds what cells are what
for i in range(width*height):
    infoGrid.append(0)
for i in range(mines):
    infoGrid.pop(0)
    infoGrid.append(-1)

random.shuffle(infoGrid)
discoveryGrid = []
"""
_discoveryGrid_ guide:
0 = Undiscovereed
1 = Discovered
"""
for i in range(len(infoGrid)):
    discoveryGrid.append(0)
for i in range(len(infoGrid)):
    if infoGrid[i] != -1:
        continue
    else:
        if str(infoGrid[i])[-1] != "0":
            try:
                if infoGrid[i-11] > -1: # Top left
                    infoGrid[i-11] += 1
            except:
                pass
        try:
            if infoGrid[i-10] > -1: # Top middle
                infoGrid[i-10] += 1
        except:
            pass
        if str(infoGrid[i])[-1] != "9":
            try:
                if infoGrid[i-9] > -1: # Top right
                    infoGrid[i-9] += 1
            except:
                pass
        
        if str(infoGrid[i])[-1] != "0":
            try:
                if infoGrid[i-1] > -1: # Middle left
                    infoGrid[i-1] += 1
            except:
                pass
        if str(infoGrid[i])[-1] != "9":
            try:
                if infoGrid[i+1] > -1: # Middle right
                    infoGrid[i+1] += 1
            except:
                pass
        
        if str(infoGrid[i])[-1] != "0":
            try:
                if infoGrid[i+11] > -1: # Bottom left
                    infoGrid[i+11] += 1
            except:
                pass
        try:
            if infoGrid[i+10] > -1: # Bottom middle
                infoGrid[i+10] += 1
        except:
            pass
        if str(infoGrid[i])[-1] != "9":
            try:
                if infoGrid[i+9] > -1: # Bottom right
                    infoGrid[i+9] += 1
            except:
                pass
def printGrid():
    global grid, fullGrid, thisRow, width, height, selected
    grid = Table.grid()
    fullGrid = []
    thisRow = []
    for i in range(width*height):
        if i == selected:
            if discoveryGrid[i] == 1:
                if infoGrid[i] == -1:
                    thisRow.append(Panel("✴", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_0_selected))
                else:
                    if infoGrid[i] == 0:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_0_selected))
                    elif infoGrid[i] == 1:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_1_selected))
                    elif infoGrid[i] == 2:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_2_selected))
                    elif infoGrid[i] == 3:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_3_selected))
                    elif infoGrid[i] == 4:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_4_selected))
                    elif infoGrid[i] == 5:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_5_selected))
                    elif infoGrid[i] == 6:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_6_selected))
                    elif infoGrid[i] == 7:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_7_selected))
                    elif infoGrid[i] == 8:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_8_selected))
                    
            else:
                thisRow.append(Panel(" ", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_selected))
        else:
            if discoveryGrid[i] == 1:
                if infoGrid[i] == -1:
                    thisRow.append(Panel("✴", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_0_unselected))
                else:
                    if infoGrid[i] == 0:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_0_unselected))
                    elif infoGrid[i] == 1:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_1_unselected))
                    elif infoGrid[i] == 2:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_2_unselected))
                    elif infoGrid[i] == 3:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_3_unselected))
                    elif infoGrid[i] == 4:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_4_unselected))
                    elif infoGrid[i] == 5:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_5_unselected))
                    elif infoGrid[i] == 6:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_6_unselected))
                    elif infoGrid[i] == 7:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_7_unselected))
                    elif infoGrid[i] == 8:
                        thisRow.append(Panel(f"{infoGrid[i]}", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.shown_8_unselected))
            else:
                thisRow.append(Panel(f" ", box=box.SQUARE, width=6, height=3, title_align="center", style=styles.hidden_unselected))

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
        if selected >= (height*10):
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
    elif k == key.ENTER:
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
                    pass