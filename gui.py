"""********************************************************************************  
   Author Information:
   Kiara Guerra

   Other Authors: 
   Victor Vu 

   Program Information:
   This File: gui.py
   Description: Graphical output of pathfinding algorithims. Collects userinput. 
********************************************************************************"""  
from tkinter import Tk, Canvas, Button, PhotoImage # GUI elements
from pathlib import Path # Find path of files

# Function to output GUI
def show_gui(adjacency_list):
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
        bg="#FFFFFF",
        height=550,
        width=700,
        bd=0, # no border
        highlightthickness=0, # no highlight
        relief="ridge" # ridge like border
    )

    canvas.place(x=0, y=0) # place canvas in window
    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        55.0,
        fill="#FD8B21",
        outline=""
    )

    canvas.create_text(
        24.0,
        9.0,
        anchor="nw",
        text="Smart Campus Navigation System ",
        fill="#000000",
        font=("JosefinSansRoman Bold", 32 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=471.0,
        y=394.0,
        width=50.0,
        height=53.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=610.0,
        y=213.0,
        width=80.0,
        height=50.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=517.0,
        y=213.0,
        width=80.0,
        height=50.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=424.0,
        y=213.0,
        width=80.0,
        height=50.0
    )

    canvas.create_text(
        423.0,
        71.0,
        anchor="nw",
        text="Select start and end node",
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

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        204.0,
        302.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
