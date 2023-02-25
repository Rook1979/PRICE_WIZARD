import tkinter as tk
from tkinter import ttk

# app window
root = tk.Tk()
root.geometry("500x350")
root.title("SEEPEX Price Wizard")

tab_control = ttk.Notebook(root)
root.resizable(0, 0)

def tab1_content():
    label = ttk.Frame(tab1, text="Configurator Price Component")
    label.pack()

    def Buyoutcost():
        try:
            SEEPEXCost = int(SEEPEXCost_entry.get())
            CalculatedLP = SEEPEXCost * 1.17 / 0.5 / 0.5
            CalculateLP_label.config(text=f"Calculated List Price: {CalculatedLP}$")
        except ValueError:
            CalculateLP_label.config(text="Please enter a valid number in SEEPEX Cost field.")

    def Pumppartcost():
        try:
            SEEPEXCost = int(SEEPEXCost_entry.get())
            CalculatedLP = SEEPEXCost * 1.17 / 0.7 / 0.5
            CalculateLP_label.config(text=f"Calculated List Price: {CalculatedLP}$")
        except ValueError:
            CalculateLP_label.config(text="Please enter a valid number in SEEPEX Cost field.")

    label = tk.Label(tab1, text="Configurator Price Component")
    label.pack()

# SEEPEXCost
SEEPEXCost_label = ttk.Label(tab1, text="SEEPEX Cost $")
SEEPEXCost_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

SEEPEXCost_entry = ttk.Entry(tab1)
SEEPEXCost_entry.grid(column=1, row=0, sticky=tk.W, padx=4, pady=5)

# BuyoutCost Text Label
Buyoutcost_label = tk.Label(tab1, text="Buyout: Seal, Coupling, etc.")
Buyoutcost_label.grid(column=1, row=3, sticky=tk.W, padx=4, pady=5)

# Calculate button Buy-out
Buyout_button = ttk.Button(tab1, text="Buy-out parts", command=Buyoutcost)
Buyout_button.grid(column=1, row=2, sticky=tk.W, padx=4, pady=5)

# PumppartCost Text Label
Pumppartcost_label = tk.Label(tab1, text="Pump parts: Rotor, Plug-in-shaft, etc.")
Pumppartcost_label.grid(column=1, row=5, sticky=tk.W, padx=4, pady=5)

# Calculate button Pump Parts
Pump_button = ttk.Button(tab1, text="Pump parts", command=Pumppartcost)
Pump_button.grid(column=1, row=4, sticky=tk.W, padx=4, pady=5)

# Calculated List Price
CalculateLP_label = tk.Label(tab1, text="")
CalculateLP_label.grid(column=1, row=7, padx=3, pady=5)

def clear_fields():
    SEEPEXCost_entry.delete(0, tk.END)
    CalculateLP_label.config(text="")

# Clear all Button
Clear_button = ttk.Button(tab1, text="Reset", command=clear_fields)
Clear_button.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

# tab1 frame
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Configurator Component Calc')
tab1_content()

tab_control.pack(expand=1, fill="both")

# SEEPEXCost
SEEPEXCost_label = ttk.Label(root, text="SEEPEX Cost $")
SEEPEXCost_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

SEEPEXCost_entry = ttk.Entry(root)
SEEPEXCost_entry.grid(column=1, row=0, sticky=tk.W, padx=4, pady=5)

# BuyoutCost Text Label
Buyoutcost_label = tk.Label(root, text="Buyout: Seal, Coupling, etc.")
Buyoutcost_label.grid(column=1, row=3, sticky=tk.W, padx=4, pady=5)

# PumppartCost Text Label
Pumppartcost_label = tk.Label(root, text="Pump parts: Rotor, Plug-in-shaft, etc.")
Pumppartcost_label.grid(column=1, row=5, sticky=tk.W, padx=4, pady=5)

# Calculate button Buy-out
Calculate_button = ttk.Button(root, text="Buy-out parts", command=Buyoutcost)
Calculate_button.grid(column=1, row=2, sticky=tk.W, padx=4, pady=5)

# Calculate button Pump Parts
Calculate_button = ttk.Button(root, text="Pump parts", command=Pumppartcost)
Calculate_button.grid(column=1, row=4, sticky=tk.W, padx=4, pady=5)

# Calculated List Price
CalculateLP_label = tk.Label (root, text="")
CalculateLP_label.grid(column=1, row=7, padx=3, pady=5)

# Clear all Button
Clear_button = ttk.Button(root, text="Reset")
Clear_button.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

tab1_content()


def tab2_content():
    label = tk.label(tab2, text="Spare parts Cost Calc")
    label.pack()

def SparePartscost():
    try:
        SEEPEXCost_entry: int(SparePartscost_label.get())
        CalculateLP = SEEPEXCost * 2.14 / 0.45
        CalculateLP_label.config(text=f"Calculated List Price: {CalculatedLP}$")
    except ValueError:
        CalculateLP_label.config(text="Please enter a valid number in SEEPEX Cost field.")

    label = tk.Label(tab2, text="Spare parts Cost Calc")
    label.pack()

# SEEPEXCost
SEEPEXCost_label = ttk.Label(tab2, text="SEEPEX Cost $")
SEEPEXCost_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

SEEPEXCost_entry = ttk.Entry(tab2)
SEEPEXCost_entry.grid(column=1, row=0, sticky=tk.W, padx=4, pady=5)

# SparePartCost Text Label
SparePartCost_label = tk.Label(root, text="Spare Part Cost for SAP Calculation")
SparePartCost_label.grid(column=1, row=5, sticky=tk.W, padx=4, pady=5)

def clear_fields():
    SEEPEXCost_entry.delete(0, tk.END)
    CalculateLP_label.config(text="")

# Clear all Button
Clear_button = ttk.Button(tab2, text="Reset", command=clear_fields)
Clear_button.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

# Calculate button Spare Parts
Calculate_button = ttk.Button(root, text="Pump parts", command=SparePartCost)
Calculate_button.grid(column=1, row=4, sticky=tk.W, padx=4, pady=5)

# Calculated List Price
CalculateLP_label = tk.Label (root, text="")
CalculateLP_label.grid(column=1, row=7, padx=3, pady=5)

#tab2 frame
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Spare parts Cost Calc')
tab2_content()

root.mainloop()
