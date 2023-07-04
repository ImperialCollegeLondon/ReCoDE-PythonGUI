# ReCoDE_PythonGUI

## A multi-channel GUI for real-time data display and analysis
![GUI](/Resources/main_window.jpg "Main Window")

## Before we start
Here is some useful links from Diego Alonso Álvarez telling you how important GUI is for research software.
- [GUIs for research software: Why are they relevant? (part one)](https://www.software.ac.uk/blog/2021-06-16-guis-research-software-why-are-they-relevant-part-one)
- [GUIs for research software: Why are they relevant? (part two)](https://www.software.ac.uk/blog/2021-06-17-guis-research-software-why-are-they-relevant-part-two)

The GUI framework we use in this course is dearpygui, here is a link to the domentation of dearpygui.Dearpygui is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.
- [Dearpygui documentation](https://docs.dearpygui.org/en/latest/)

## Introduction to GUI design for real-time data display and analysis
### **What is GUI?**
GUI stands for Graphical User Interface. It is a type of user interface that allows users to interact with electronic devices through graphical icons and visual indicators. GUIs were introduced in reaction to the perceived steep learning curve of command-line interfaces (CLIs), which require commands to be typed on the keyboard. The actions in a GUI are usually performed through direct manipulation of the graphical elements. The graphical elements include but not limited to windows, menus, buttons, scrollbars, icons, etc.
### **Why do we need GUI?**
GUIs are widely used in many applications. GUIs are used in operating systems, web browsers, office suites, email programs, etc. GUIs are also used in scientific applications. GUIs are used in data acquisition, data analysis, and data visualization. GUIs are used in scientific applications because they are easy to use and they can be used to create a user-friendly interface for scientific applications.

### **GUI frameworks**
There are many GUI frameworks available for Python. Some of the popular GUI frameworks include Tkinter, PyQt, PySide, wxPython, Kivy, etc. Different GUI frameworks have different ways to create a GUI. In this course, we will use dearpygui as the GUI framework. Dearpygui is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.

There are plenty of GUI software developed by dearpygui. You can find them in the [dearpygui showcase](https://github.com/hoffstadt/DearPyGui/wiki/Dear-PyGui-Showcase).

### **Best practice notes**
Debugging GUI codes is different from traditional code. 

 - Have the structure of GUI program in mind. You are placing widgets on a planar canvas. This helps to find missing widgets as they can be blocked by others and determine the relative location of the widgets. 

 - Always keep in mind that there still exists CLI when you design GUI, try to print essential variables for debugging. 

 - Unless you enable multithreading, your codes run in serial. This explains why there are lags during display when you are processing data in background. 

 - Assign meaningful names to each widget. You’ll lose your widgets when you have plenty of them. 

 - Compared with displaying data statically, you should have an understanding of sliding window when you dynamically display data. 

### **Structure of the GUI program**
Day 1: 
    Develop familiarity with frameworks and key components for GUI design.  
    Students will be provided with sample codes to familiarize commonly used GUI widgets. They can design whatever they want using provided widgets. (Sample data will be provided)  

Day 2: 
    Design a GUI to dynamically display data with single channel.  
    Students will be provided a template with sample modularized codes to illustrate how to add a figure on GUI and make it work.  

Day 3: 
    Add more channels to GUI.  
    Students try to extend the work in step 2 by referring to another template provided. They are free to add as many figures as possible and display anything on the figures. 

Day 4: 
    Add a control area to control the display, such as selecting different channels.  
    Students will be provided a new template with modularized functions and control widgets as well as directive instructions for adding   control widgets used in GUI design. They can then combine these widgets with figures to achieve different functions.  

Day 5: 
    Add the function to read files and display data from files on GUI.  
    The students will first learn the different formats that have been used in storing data and write codes to read the files. By simply replace the data sent to figures with those read from files, they will achieve the final goal. During this part, they will learn multithreading to simultaneously run reading data and display functions.

Day 6: 
   Add toggle functions to the GUI (choose between local data or device inputs).  
   An example of a toggle function will be added to extend the previous template. Students can follow the instructions to implement the GUI.  

### **Download data**

All data are stored in ```Data``` folder. You should put the data file you want to read in this folder. You can then access the data file by setting the path to ```Data``` folder. For example, you can use the following code to read the data file ```charis4.dat```.
```python
import numpy as np
filename = 'Data/charis4.dat'
datafile =open(filename, 'rb')
dtype = np.dtype('int16')
data = np.fromfile(datafile,dtype)
```