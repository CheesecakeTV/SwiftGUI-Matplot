import SwiftGUI as sg
import tkinter as tk
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

import SwiftGUI_Matplot as sgm
from matplotlib.figure import Figure
import numpy as np


sg.Themes.FourColors.DeepSea()

my_figure = Figure((6,4), dpi=100)

# x = np.linspace(1, 10, 100)
# y = np.sin(x)

layout = [
    [
        sg.T("Matplot:")
    ],[
        my_matplot := sgm.Matplot(
            #figure= my_figure,
            # axes= ax,
            # title= "Test",
            #navigation_bar= True,
            #legend= False,
        )
    ],[
        my_T := sg.T()
    ],[
        sg.Button(
            "Event!",
            key= "Button",
        ),
        sg.Button(
            "Clear",
            key_function= my_matplot.clear
        )
    ]
]

my_matplot.bar(
    ["Hallo", "Welt", "Hello", "World"],
    (3,10,2, 5),
)
#my_matplot.plot(x,y)

w = sg.Window(layout)

for e,v in w:
    ...
    #my_matplot.scatter(x,y, label="Hi")
    #y *= np.sin(x)
    #my_matplot.figure.legend()
    #my_matplot._figure_canvas.draw()
