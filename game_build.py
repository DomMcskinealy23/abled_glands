import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import character_class

#Frame object holding all pages
#Controller of pages
class Mainframe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x1000")
        
        container = tk.Frame(height= 400, width= 600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)        

        self.id = tk.StringVar()
        self.id.set("DOMDOM")

        self.listing = {}

        for p in (Welcomepage, Newgame, Loadgame, Gamepage, Inventory, Map):
            page_name =p.__name__
            frame =p(parent = container, controller = self)
            frame.grid(row = 0, column = 0, sticky = "NESW")
            frame.rowconfigure(0, weight= 1)
            frame.rowconfigure(1, weight= 1)
            frame.rowconfigure(2, weight= 1)
            frame.rowconfigure(3, weight= 1)
            frame.rowconfigure(4, weight= 1)

            for column in range(8):
                frame.columnconfigure(column, weight=1)

            self.listing[page_name] = frame

        self.up_frame("Welcomepage")
        
    #Raises page that has been selected
    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()

#start page design
class Welcomepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.config(bg = "darkred")

        label = tk.Label(self, text ="'ABLED GLANDS' \n THE MOTHER FUCKING GAME",
                        font = ("Comic Sans MS", "40"),
                        width = 30, height = 3,
                        bg = ("darkred"))    
        label.grid(row = 0, column = 3)

        button1 = tk.Button(self, text = "New Game",
                            command = lambda: controller.up_frame("Newgame"),
                            width="20", height="3",
                            font = ("Comic Sans MS", "20"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button1.grid(row = 1, column = 3)

        button2 = tk.Button(self, text = "Load Game",
                            command = lambda: controller.up_frame("Loadgame"),
                            width="20", height="3",
                            font = ("Comic Sans MS", "20"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = "target")
        button2.grid(row = 2, column = 3)

#New game page design
class Newgame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.config(bg = "darkred")

        label = tk.Label(self, text ="NEW GAME \n PICK YOUR FUCKING WARRIOR",
                        font = ("Comic Sans MS", "40"),
                        width = 30, height = 3,
                        bg = ("darkred"))    
        label.grid(row = 0, column = 3)

        button1 = tk.Button(self, text = "Priest \n Charisma: 5  Combat: 3 \n Magic: 4  Sancity: 7 \n Scouting: 5  Thievery: 2" ,
                            command = lambda: controller.up_frame("Gamepage"),
                            width="25", height="5",
                            font = ("Comic Sans MS", "15"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button1.grid(row = 1, column = 1, columnspan = 2)

        button2 = tk.Button(self, text = "Mage \n Charisma: 3  Combat: 3 \n Magic: 7  Sancity: 1 \n Scouting: 6  Thievery: 4",
                            command = lambda: controller.up_frame("Gamepage"),
                            width="25", height="5",
                            font = ("Comic Sans MS", "15"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button2.grid(row = 2, column = 1)

        button3 = tk.Button(self, text = "Rouge \n Charisma: 6  Combat: 5 \n Magic: 5  Sancity: 2 \n Scouting: 3  Thievery: 7",
                            command = lambda: character_class.loadClass(player, "Rouge",6,5,5,2,3,7),
                            width="25", height="5",
                            font = ("Comic Sans MS", "15"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button3.grid(row = 1, column = 3)

        button4 = tk.Button(self, text = "Trobadour \n Charisma: 7  Combat: 4 \n Magic: 5  Sancity: 4 \n Scouting: 3  Thievery: 5",
                            command = lambda: controller.up_frame("Gamepage"),
                            width="25", height="5",
                            font = ("Comic Sans MS", "15"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button4.grid(row = 2, column = 3)

        button5 = tk.Button(self, text = "Warrior \n Charisma: 4  Combat: 7 \n Magic: 2  Sancity: 5 \n Scouting: 4  Thievery: 5",
                            command = lambda: controller.up_frame("Gamepage"),
                            width="25", height="5",
                            font = ("Comic Sans MS", "15"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button5.grid(row = 1, column = 5)

        button6 = tk.Button(self, text = "Wayfarer \n Charisma: 3  Combat: 6 \n Magic: 3  Sancity: 4 \n Scouting: 7  Thievery: 5",
                            command = lambda: controller.up_frame("Gamepage"),
                            width="25", height="5",
                            font = ("Comic Sans MS", "15"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button6.grid(row = 2, column = 5)

#Loadgame page design
class Loadgame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text ="Load Game \n" + controller.id.get(), font = ("Comic Sans MS", "20"))

        label.pack()

#Game page design
class Gamepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.config(bg = "darkred")

        text_area = tk.Text(self, width= 70, height= 20)
        text_area.grid(row= 2, column= 5, sticky= ("NSEW"))

    
        button1 = tk.Button(self, text = "Inventory",
                            command = lambda: controller.up_frame("Inventory"),
                            width="10", height="3",
                            font = ("Comic Sans MS", "10"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button1.grid(row = 1, column = 0)

        button2 = tk.Button(self, text = "Map",
                            command = lambda: controller.up_frame("Map"),
                            width="10", height="3",
                            font = ("Comic Sans MS", "10"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = "target")
        button2.grid(row = 2, column = 0)

        button3 = tk.Button(self, text = "Save & Close",
                            command = lambda: controller.up_frame("Welcomepage"),
                            width="10", height="3",
                            font = ("Comic Sans MS", "10"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = "pirate")
        button3.grid(row = 3, column = 0)

class Inventory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.config(bg = "darkred")   

        text_area = tk.Text(self, width= 70, height= 20,)
        text_area.insert(index="0.0",chars=player.print_attributes())
        text_area.grid(row= 2, column= 5, sticky= ("NSEW"))

        button1 = tk.Button(self, text = "Back to game",
                            command = lambda: controller.up_frame("Gamepage"),
                            width="10", height="3",
                            font = ("Comic Sans MS", "10"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button1.grid(row = 1, column = 0)     

class Map(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.config(bg = "darkred")

        #image_path = "./map.png"
        #image = ImageTk.PhotoImage(Image.open(image_path))

        #label_image = tk.Label(self, image = image)
        #label_image.grid(row= 2, column= 2)

        button1 = tk.Button(self, text = "Back to game",
                            command = lambda: controller.up_frame("Gamepage"),
                            width="10", height="3",
                            font = ("Comic Sans MS", "10"),
                            bg = ("black"),
                            fg = ("white"),
                            cursor = ("spider"))
        button1.grid(row = 1, column = 0) 



#Creates and builds app
if __name__ == '__main__':
    player = character_class.Character()
    app = Mainframe()
    app.mainloop()
