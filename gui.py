"""********************************************************************************  
   Author Information:
   Kiara Guerra

   Other Authors: 
   Victor Vu 

   Program Information:
   This File: gui.py
   Description: Graphical output of pathfinding algorithims. Collects user input. 
********************************************************************************"""  
from pathlib import Path # Create a path to the image file
import networkx as nx # Used to create a graph and populate it with nodes
from tkinter import Tk, Canvas, Button, PhotoImage, StringVar, OptionMenu, Label # Use necessary widgets for GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Embed the Matplotlib figure in the Tkinter window
from matplotlib.figure import Figure # Note: does not seem to be used yet -----------------------------------------------
import matplotlib.pyplot as plt # Plot the graph on the Matplotlib figure
import pandas as pd # Note: does not seem to be used yet ------------------------------------------------------------
from data import * # Import all data from data.py
from algorithms import bfs_search # Import external function BFS
from algorithms import dfs_search # Import external function DFS

# Function to output the GUI
def show_gui(adjacency_list):
    # Define path for assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"
    def relative_to_assets(path: str) -> Path: 
        return ASSETS_PATH / Path(path)

    # Create Tkinter window
    window = Tk()
    window.geometry("1400x1000") # ajusted window size
    window.configure(bg="#FFFFFF")
    G = nx.Graph() # create a NetworkX graph

    # Add nodes to the graph
    for building in buildings:
        G.add_node(building)

    # Add coordinates to the nodes
    for building, coord in coordinates.items():
        G.nodes[building]['pos'] = coord

    # Populate the graph with edges and weights
    for building, adj_list in adjacency_list.items():
        for adj_building, weight in adj_list.items():
            G.add_edge(building, adj_building, weight=weight)

    fig, ax = plt.subplots(figsize=(20, 11)) # create a Matplotlib figure and axis with adjusted size
    background = plt.imread('assets/frame0/WEBSITEMAP.jpg') # load the background image
    ax.imshow(background, extent=[0, 500, 0, 700]) # plot the image as background

    # Draw the graph on top of the image
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=False, node_size=300, node_color='#4258CA', font_size=8)
    nx.draw_networkx_edges(G, pos, width=3, edge_color="#4258CA")

    # Create a canvas widget to embed the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0) # adjusted placement to the far left

    # Create a separate canvas for drawing shapes
    canvas_shapes = Canvas(
        window,
        bg="red",
        height=100, # adjusts canvas height
        width=1400,   
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas_shapes.place(x=0, y=0) # set placement to the far left

    # Add rectangles using Canvas widget's create_rectangle method
    canvas_shapes.create_rectangle(0.0, 0.0, 1400.0, 100.0, fill="#FD8B21", outline="")
    canvas_shapes.create_text(40.0, 9.0, anchor="nw", text="Smart Campus Navigation System", fill="#000000", font=("JosefinSansRoman Bold", 40))

    # Create a pink canvas for general information
    canvas_general = Canvas(
        window,
        bg="pink",
        height=600,  
        width=650,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas_general.place(x=10, y=100) # set placement to the far left

    # Add rectangles around buttons
    canvas_general.create_text(40.0, 10.0, anchor="nw", text="For accessible paths click the button below:", fill="black", font=("JosefinSansRoman Bold", 18))
    canvas_general.create_text(40.0, 200.0, anchor="nw", text="Pick start and end points from the drop down menu:", fill="black", font=("JosefinSansRoman Bold", 18))
    canvas_general.create_text(40.0, 350.0, anchor="nw", text="Choose preferred algorithm:", fill="black", font=("JosefinSansRoman Bold", 18))

    # Accessibility Button
    button_image_Access = PhotoImage(file=relative_to_assets("ButtonAccess.png"))
    ButtonAccess = Button(
        image=button_image_Access,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Access clicked"), # Placeholder will need accessibility path later --------------------------------
        relief="flat"
    )
    ButtonAccess.place( # placement for the accessibility button
        x=100,
        y=160,
        width=472.0,
        height=70.0
    )

    # BFS Button
    button_image_BFS = PhotoImage(file=relative_to_assets("ButtonBFS.png"))
    ButtonBFS = Button(
        image=button_image_BFS,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: display_result(canvas_result, bfs_search(start_building, end_building, adjacency_list), "BFS"),
        relief="flat"
    )
    ButtonBFS.place(
        x=450,
        y=500,
        width=200.0,
        height=120.0
    )

    # DFS Button
    button_image_DFS = PhotoImage(
        file=relative_to_assets("ButtonDFS.png"))
    ButtonDFS = Button(
        image=button_image_DFS,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: display_result(canvas_result, dfs_search(start_building, end_building, adjacency_list), "DFS"),
        relief="flat"
    )
    ButtonDFS.place(
        x=230,
        y=500,
        width=200.0,
        height=120.0
    )

    # DA Button
    button_image_DA = PhotoImage(
        file=relative_to_assets("ButtonDA.png"))
    ButtonDA = Button(
        image=button_image_DA,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("DA clicked"),
        relief="flat"
    )
    ButtonDA.place(
        x=10,
        y=500,
        width=200.0,
        height=120.0
    )

    options = list(map(str, buildings)) # dropdown menu options
    # Datatype of menu text
    clicked1 = StringVar()
    clicked2 = StringVar()
    # Initial menu text with defaults
    clicked1.set("Building 1") 
    clicked2.set("Building 2")  

    # Function to update start_building and end_building
    def update_buildings(*args):
        global start_building, end_building
        start_building = clicked1.get()
        end_building = clicked2.get()

    # Create Dropdown menus
    drop1 = OptionMenu(window, clicked1, *options, command=update_buildings)
    drop1.place(x=100, y=350) 
    drop2 = OptionMenu(window, clicked2, *options, command=update_buildings)
    drop2.place(x=350, y=350) 

    # Create a separate canvas widget to display the result text
    canvas_result = Canvas(
        window,
        bg="pink",
        height=600,
        width=650,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas_result.place(x=10, y=700) 

    window.resizable(False, False) # prevent window from being resized
    window.mainloop() # keep running the GUI

def display_result(canvas, path, algorithm_name): # expects both BFS and DFS paths
    if path:
        formatted_path = '\n'.join(map(str, path)) # take out unwanted characters from string
        result = f"{algorithm_name}: Path within {len(path) - 1} stops \n{formatted_path}" # print out # of stops and shows path
    else:
        result = f"{algorithm_name}: No path was found."

    canvas.delete("result_text") # clear previous result text

    # Display the new result text
    canvas.create_text(
        10,
        10,
        anchor="nw",
        text=result,
        fill="#000000",
        font=("Helvetica", 12),
        tags="result_text" # tagged to allow manipulation later
    )


