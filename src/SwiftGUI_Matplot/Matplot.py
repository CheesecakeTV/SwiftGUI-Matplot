import tkinter as tk
import SwiftGUI as sg
import matplotlib.lines
from SwiftGUI.Compat import Self
from matplotlib.figure import Figure
from typing import Hashable, Any
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from SwiftGUI_Matplot import GlobalOptions


class Matplot(sg.BaseWidget):
    tk_widget: tk.Canvas
    defaults = GlobalOptions.Matplot

    def __init__(
            self,
            /,
            figure: Figure = None,
            axes: Any = None,   # Todo: Add proper typehint

            key: Hashable = None,

            navigation_bar: bool = None,

            expand: bool = None,
            expand_y: bool = None,
            tk_kwargs: dict = None,
    ):
        super().__init__(
            key=key,
            expand= expand,
            expand_y= expand_y,
            tk_kwargs=tk_kwargs,
        )

        if figure is None:
            figure = Figure()

            if axes is None:
                axes = figure.add_subplot()

        self.figure = figure
        self.axes = axes

        self._update_initial(
            background_color_outside = None,
            background_color = None,
            height = None,
            width = None,
            dpi = None,
            borderwidth = None,
            bordercolor = None,
            title = None,
            spine_color = None,
            tick_color = None,
            text_color = None,
        )

        self._navbar = self.defaults.single("navigation_bar", navigation_bar)

    def _init_widget_for_inherrit(self, container) -> tk.Widget:
        figure_canvas = FigureCanvasTkAgg(self.figure, master= container)
        self._figure_canvas = figure_canvas

        return figure_canvas.get_tk_widget()

    def _update_special_key(self,key:str,new_val:Any) -> bool|None:

        match key:
            case "background_color":
                #self.figure.set_facecolor(new_val)
                self.axes.set_facecolor(new_val)
            case "background_color_outside":
                self.figure.set_facecolor(self.defaults.single("background_color", new_val))

            case "height":
                if new_val is None:
                    return
                self.figure.set_figheight(new_val)
            case "width":
                if new_val is None:
                    return
                self.figure.set_figwidth(new_val)

            case "dpi":
                if new_val is None:
                    return
                self.figure.set_dpi(new_val)

            case "borderwidth":
                self.figure.set_linewidth(new_val)
            case "bordercolor":
                self.figure.set_edgecolor(self.defaults.single("highlightbackground_color", new_val))

            case "title":
                if new_val is None:
                    return
                self.axes.set_title(new_val)

            case "spine_color":
                new_val = self.defaults.single("text_color", new_val)
                self.axes.spines["bottom"].set_color(new_val)
                self.axes.spines["top"].set_color(new_val)
                self.axes.spines["left"].set_color(new_val)
                self.axes.spines["right"].set_color(new_val)
            case "tick_color":
                new_val = self.defaults.single("text_color", new_val)
                self.axes.tick_params(colors=new_val)

            case "text_color":
                self.axes.xaxis.label.set_color(new_val)
                self.axes.yaxis.label.set_color(new_val)

            case _:
                return super()._update_special_key(key, new_val)

        return True

    def init_window_creation_done(self):
        super().init_window_creation_done()

        if self._navbar:
            NavigationToolbar2Tk(self._figure_canvas)


    def plot(self, xs, ys, *args, color= None, **kwargs) -> list[matplotlib.lines.Line2D]:
        """
        Call axes.plot with some global options applied
        :return:
        """
        kwargs["color"] = color

        self.defaults.apply(kwargs)

        return self.axes.plot(xs, ys, *args, **kwargs)

    def grid(self, color= None, **kwargs):
        """
        Call axes.grid with some global options applied
        :param color:
        :param kwargs:
        :return:
        """
        kwargs["color"] = self.defaults.single("text_color", color)

        self.defaults.apply(kwargs)

        return self.axes.grid(**kwargs)
