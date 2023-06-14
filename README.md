# ReCoDE_PythonGUI
## Before we start
Here is some useful links from Diego Alonso Álvarez telling you how important GUI is for research software.
- [GUIs for research software: Why are they relevant? (part one)](https://www.software.ac.uk/blog/2021-06-16-guis-research-software-why-are-they-relevant-part-one)
- [GUIs for research software: Why are they relevant? (part two)](https://www.software.ac.uk/blog/2021-06-17-guis-research-software-why-are-they-relevant-part-two)

The GUI framework we use in this course is dearpygui, here is a link to the domentation of dearpygui.Dearpygui is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.
- [Dearpygui documentation](https://docs.dearpygui.org/en/latest/)

## Introduction to GUI design for real-time data acquisition and analysis
### **What is GUI?**
GUI stands for Graphical User Interface. It is a type of user interface that allows users to interact with electronic devices through graphical icons and visual indicators. GUIs were introduced in reaction to the perceived steep learning curve of command-line interfaces (CLIs), which require commands to be typed on the keyboard. The actions in a GUI are usually performed through direct manipulation of the graphical elements. The graphical elements include but not limited to windows, menus, buttons, scrollbars, icons, etc.
### **Why do we need GUI?**
GUIs are widely used in many applications. GUIs are used in operating systems, web browsers, office suites, email programs, etc. GUIs are also used in scientific applications. GUIs are used in data acquisition, data analysis, and data visualization. GUIs are used in scientific applications because they are easy to use and they can be used to create a user-friendly interface for scientific applications.

### **GUI frameworks**
There are many GUI frameworks available for Python. Some of the popular GUI frameworks include Tkinter, PyQt, PySide, wxPython, Kivy, etc. Different GUI frameworks have different ways to create a GUI. In this course, we will use dearpygui as the GUI framework. Dearpygui is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.

There are plenty of GUI software developed by dearpygui. You can find them in the [dearpygui showcase](https://github.com/hoffstadt/DearPyGui/wiki/Dear-PyGui-Showcase).

### Best practice notes
Debugging GUI codes is different from traditional code. 

 - Have the structure of GUI program in mind. You are placing widgets on a planar canvas. This helps to find missing widgets as they can be blocked by others and determine the relative location of the widgets. 

 - Always keep in mind that there still exists CLI when you design GUI, try to print essential variables for debugging. 

 - Unless you enable multithreading, your codes run in serial. This explains why there are lags during display when you are processing data in background. 

 - Assign meaningful names to each widget. You’ll lose your widgets when you have plenty of them. 

 - Compared with displaying data statically, you should have an understanding of sliding window when you dynamically display data. 
