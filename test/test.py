import SwiftGUI as sg
import SwiftGUI_Matplot as sgm
from matplotlib.figure import Figure
import numpy as np


sg.Themes.FourColors.Emerald()

#my_figure = Figure((6,4), dpi=100, )

x = np.linspace(0, 10, 100)
y = x ** 2

#ax = my_figure.add_subplot()
#ax.plot(x, y)

layout = [
    [
        sg.T("Matplot:")
    ],[
        my_matplot := sgm.Matplot(navigation_bar= False)
    ]
]

w = sg.Window(layout)

my_matplot.axes.plot(x, y)

for e,v in w:
    ...
