"""********************************************************************************  
   Author Information:
   Kiara Guerra

   Other Authors: 
   Victor Vu 

   Program Information:
   This File: gui.py
   Description: Graphical output of pathfinding algorithims. Collects user input. 
********************************************************************************"""  
from tkinter import Tk, Canvas, Button, PhotoImage # GUI elements
from pathlib import Path # Find path of files
from algorithms import bfs_search # Import external function BFS
from algorithms import dfs_search # Import external function DFS

# Function to output GUI
def show_gui(adjacency_list): # adjacency list contains nodes and neighbors
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

    def relative_to_assets(path: str) -> Path: # find the file paths
        return ASSETS_PATH / Path(path)

    window = Tk() # create new window
    window.geometry("700x550") # set size
    window.configure(bg="#FFFFFF") # set color

    # Canvas to draw gui elements on
    canvas = Canvas(
        window,
        bg="#FFFFFF", # color
        height=550,
        width=700,
        bd=0, # no border
        highlightthickness=0, # no highlight
        relief="ridge" # ridge like border
    )
    canvas.place(x=0, y=0) # place canvas in window
    canvas.create_rectangle( # new shape to use 
        0.0, # place at top
        0.0, # move it left
        700.0, # width 
        55.0, # height
        fill="#FD8B21",
        outline="" # no outline
    )
    canvas.create_text( # write text in canvas
        24.0, # x coordinate
        9.0, # y coordinate 
        anchor="nw", # anchor text at northwest
        text="Smart Campus Navigation System ",
        fill="#000000",
        font=("JosefinSansRoman Bold", 32 * -1)
    )

    # Accessibility Button
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png")) # import assets for button1
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Accessibility Button clicked, WIP"), # execute line when pressed (not finished) important!!!!!!
        relief="flat"
    )
    button_1.place( # button placement
        x=471.0,
        y=394.0,
        width=50.0,
        height=53.0
    )

    # Dijkstra's Algorithm Button
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,    
        borderwidth=0,
        highlightthickness=0,
        command=lambda: display_result(canvas), # Not finished wait for Kim's part. ---------------important!!!!!!!!!!
        relief="flat" 
    )
    button_2.place(
        x=610.0,
        y=213.0,
        width=80.0,
        height=50.0
    )

    # Depth-First Search Button
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: display_result(canvas, dfs_search(start_location, goal_location, adjacency_list), "DFS"), # call DFS, assign name and display
        relief="flat"
    )
    button_3.place(
        x=517.0,
        y=213.0,
        width=80.0,
        height=50.0
    )

    # Breadth-First Search Button
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: display_result(canvas, bfs_search(start_location, goal_location, adjacency_list,), "BFS"), # call BFS, assign name and display
        relief="flat"
    )
    button_4.place(
        x=424.0,
        y=213.0,
        width=80.0,
        height=50.0
    )

    # Selection Menu 
    canvas.create_text(
        423.0,
        71.0,
        anchor="nw",
        text="Select start and end node:",
        fill="#000000",
        font=("JostRoman Bold", 16 * -1)
    )
    canvas.create_text(
        424.0,
        143.0,
        anchor="nw",
        text="Select desired path algorithm",
        fill="#000000",
        font=("JostRoman Bold", 16 * -1)
    )

    # Main Map
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        204.0,
        302.0,
        image=image_image_1
    )
    window.resizable(False, False) # prevent window from resizing 
    window.mainloop() # keeps the GUI running until closed by user

# Placeholder locations (user input will collected in selection menu later) ------------------------- important!!!!
start_location = "Library"
goal_location = "Park"

# Function to update the canvas search results
def display_result(canvas, path, algorithm_name): # expects both BFS and DFS paths
    if path:
        result = f"{algorithm_name}: Path found within {len(path)-1} stops: {path}" # print out # of stops and shows path
    else:
        result = f"{algorithm_name}: No path found."
    canvas.delete("result_text") # clear previous text on the 
    # Display the new result text
    canvas.create_text(
        100, 
        100, 
        anchor="sw",
        text=result,
        fill="#000000",
        font=("Helvetica", 12),
        tags="result_text" # tagged to allow manipulation later
    )
 