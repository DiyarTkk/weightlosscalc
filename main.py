import tkinter
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import json


datalist = [("Day","Weight","Total Fat","Saturated Fat","Carbohydrates","Sugar","Protein","Calories")]
     
def draw_chart():
    days = [int(x[0]) for x in datalist[1:]]
    weights = [int(x[1]) for x in datalist[1:]]
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 6), dpi=80)
    ax = sns.lineplot(x=days, y=weights, marker='o', markersize=8, linewidth=2, color='blue')
    ax.set(xlabel='Day', ylabel='Weight')
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    plt.title("Daily Weight")
    plt.show()


def extern_data_push():
    with open('datalist.json', 'w') as f:
        json.dump(datalist, f)

def extern_data_get():
    global datalist
    with open('datalist.json', 'r') as f:
        datalist = json.load(f)
    datalist = list(map(tuple, datalist))
    load_data()
    
def toggle_mode():
    
    if modeswitch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

def load_data():
    for col_name in datalist[0]:
        treeview.heading(col_name, text=col_name)
    for i in treeview.get_children():
        treeview.delete(i)
    for value_tuple in datalist[1:]:
        treeview.insert('', tk.END, values=value_tuple)

def data_input():
    try:
        day = int(dayentry.get())
        weight = int(weightentry.get())
        totalfat = int(totalfatentry.get())
        saturatedfat = int(saturatedfatentry.get())
        carbohydrates = int(carbohydratesentry.get())
        sugar = int(sugarentry.get())
        protein = int(proteinentry.get())
        calories = int(caloriesentry.get())
        day = dayentry.get()
        weight = weightentry.get()
        totalfat = totalfatentry.get()
        saturatedfat = saturatedfatentry.get()
        carbohydrates = carbohydratesentry.get()
        sugar = sugarentry.get()
        protein = proteinentry.get()
        calories = caloriesentry.get()
        datalist.append((day,weight,totalfat,saturatedfat,carbohydrates,sugar,protein,calories))
        load_data()
    except ValueError:
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        error_window.config(bg="darkred")
        error_label = tk.Label(error_window, text="Invalid. Every Input must be an Integer (e.g. 1, 99, 1001)", bg="darkred", fg="lightgrey")
        error_label.pack(padx=10, pady=10)

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")
frame = ttk.Frame(root)
frame.pack()
root.title("Weight Loss Calc")


infoframe = ttk.LabelFrame(frame, text="Attributes")
infoframe.grid(row=0,column=0, padx=10, pady=10)

day = ttk.Label(infoframe, text="Day")
day.grid(row=0, column=0)

weight = ttk.Label(infoframe, text="Weight")
weight.grid(row=0, column=1)

totalfat = ttk.Label(infoframe, text="Total Fat")
totalfat.grid(row=0, column=2)

saturatedfat = ttk.Label(infoframe, text="Saturated Fat")
saturatedfat.grid(row=0, column=3)

carbohydrates  = ttk.Label(infoframe, text="Carbohydrates ")
carbohydrates .grid(row=2, column=0)

sugar = ttk.Label(infoframe, text="Sugar")
sugar.grid(row=2, column=1)

protein = ttk.Label(infoframe, text="Protein")
protein.grid(row=2, column=2)

calories = ttk.Label(infoframe, text="Calories")
calories.grid(row=2, column=3)

dayentry = ttk.Entry(infoframe)
weightentry = ttk.Entry(infoframe)
totalfatentry = ttk.Entry(infoframe)
saturatedfatentry = ttk.Entry(infoframe)
carbohydratesentry = ttk.Entry(infoframe)
sugarentry = ttk.Entry(infoframe)
proteinentry = ttk.Entry(infoframe)
caloriesentry =  ttk.Entry(infoframe)

dayentry.grid(row=1, column=0)
weightentry.grid(row=1, column=1)
totalfatentry.grid(row=1, column=2)
saturatedfatentry.grid(row=1, column=3)
carbohydratesentry.grid(row=3, column=0)
sugarentry.grid(row=3, column=1)
proteinentry.grid(row=3, column=2)
caloriesentry.grid(row=3, column=3)

for widget in infoframe.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = ttk.Button(infoframe, text="Enter Attr", command=data_input)
button.grid(row=4, column=0, sticky="news", padx=20, pady=20)

button = ttk.Button(infoframe, text="Load Data", command=extern_data_get)
button.grid(row=4, column=1, sticky="news", padx=20, pady=20)

button = ttk.Button(infoframe, text="Save Data", command=extern_data_push)
button.grid(row=4, column=2, sticky="news", padx=20, pady=20)

button = ttk.Button(infoframe, text="Show Chart", command=draw_chart)
button.grid(row=4, column=3, sticky="news", padx=20, pady=20)

modeswitch = ttk.Checkbutton(
    frame, text="Mode", style="Switch", command=toggle_mode)
modeswitch.grid(row=6, column=1,padx=10,pady=10,sticky="news")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0,column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right",fill="y")
cols = ("Day","Weight","Total Fat","Saturated Fat","Carbohydrates","Sugar","Protein","Calories")
treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=10)
treeview.column("Day", width=150)
treeview.column("Weight", width=150)
treeview.column("Total Fat", width=150)
treeview.column("Saturated Fat", width=150)
treeview.column("Carbohydrates", width=150)
treeview.column("Sugar", width=150)
treeview.column("Protein", width=150)
treeview.column("Calories", width=150)
treeview.pack()
treeScroll.config(command=treeview.yview)
load_data()

root.mainloop()
