# ReCoDE_PythonGUI

# A multi-channel GUI for real-time data display and analysis
![GUI](https://raw.githubusercontent.com/ImperialCollegeLondon/ReCoDE-PythonGUI/main/Resources/main_window.jpg "Main Window")

In this course, you will learn how to create a GUI program to display and analyze data in real-time with Python. The GUI program is designed to display and analyze data from a file. The GUI program is also designed to display data from a data acquisition system through serial port communication. The GUI program is developed using dearpygui, a GPU-based Python GUI framework. 

By the end of this course, you will be able to design a GUI program looks like the above picture, which can display data from a file or a data acquisition system in real-time. You will also be able to select the file to display, select the channels to display, change the color of the lines, and start, stop, and pause the display. You will also learn how to add data analysis functions to the GUI program and display analysis results in real-time.

## Before we start
Here is some useful links from Diego Alonso Álvarez telling you how important GUI is for research software.
- [GUIs for research software: Why are they relevant? (part one)](https://www.software.ac.uk/blog/2021-06-16-guis-research-software-why-are-they-relevant-part-one)
- [GUIs for research software: Why are they relevant? (part two)](https://www.software.ac.uk/blog/2021-06-17-guis-research-software-why-are-they-relevant-part-two)

The GUI framework we use in this course is dearpygui, here is a link to the domentation of dearpygui [Dearpygui documentation](https://docs.dearpygui.org/en/latest/). Dearpygui is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.

## Introduction to GUI design for real-time data display and analysis
### **What is GUI?**
GUI stands for Graphical User Interface. It is a type of user interface that allows users to interact with electronic devices through graphical icons and visual indicators. GUIs were introduced in reaction to the perceived steep learning curve of command-line interfaces (CLIs), which require commands to be typed on the keyboard. The actions in a GUI are usually performed through direct manipulation of the graphical elements. The graphical elements include but not limited to windows, menus, buttons, scrollbars, icons, etc.
### **Why do we need GUI?**
GUIs are widely used in many applications including operating systems, web browsers, office suites, email programs, etc. GUIs are also used in scientific applications, including data acquisition, data analysis, and data visualization. Their utilization in scientific applications stems from their user-friendly nature, facilitating the creation of intuitive interfaces tailored to scientific tasks.

### **GUI frameworks**
There are many GUI frameworks available for Python. Some of the popular GUI frameworks include Tkinter, PyQt, PySide, wxPython, Kivy and so on. Different GUI frameworks have different ways to create a GUI. In this course, we will use dearpygui as the GUI framework. Dearpygui is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.

There are plenty of GUI software developed by dearpygui. You can find them in the [dearpygui showcase](https://github.com/hoffstadt/DearPyGui/wiki/Dear-PyGui-Showcase).

### **Structure of this course**
Day 1: Develop familiarity with frameworks and key components for GUI design.  
* Contents:
  
    You will be provided with sample codes to familiarize commonly used GUI widgets. You can design whatever you want using provided widgets. (Sample data will be provided)
* Outcomes:
  
    You will be able to design a GUI with different kinds of widgets including buttons, text boxes, figures and so on.

Day 2: Design a GUI to dynamically display data with single channel.

* Contents:  

    You will be provided a template with sample modularized codes to illustrate how to add a figure on GUI and make it work. You will also learn how to display data from a file with single channel.

* Outcomes:
    
    You will learn how to update data in a plot widget and be able to design a GUI to display data with single channel.

Day 3: Design a GUI to dynamically display data with multiple channels.

* Contents:  
    You will extend the work in step 2 by referring to another template provided to add two more channles. You will learn how to add multiple figures on GUI and make them work. You will also learn how to display data from a file with multiple channels.

* Outcomes:
    
    You will gain an understanding of **tags** in dearpygui and be able to update different widgets according to their tags. You will also be able to design a GUI to display data with multiple channels. 

Day 4: Design a GUI with control panel to control the display.

 * Contents:
  
    You will be provided a new template with modularized functions and control widgets as well as directive instructions for adding control widgets used in GUI design. Four control functions will be provided as examples, including select file to display, start, stop and pause the display, select channels to be displayed, and change the color of lines.

* Outcomes:

    You will have an understanding of the interactions between different widgets, taking inputs from users and updating widgets accordingly.

Day 5: Extension: Serial Port Communication

* Contents:
    
    You will be provided a new template with modularized functions and control widgets to display data from a data acquisition system through serial port communication. You will learn how to display data from a real-time data acquisition system with serial communication.

* Outcomes:

    You will gain basic and necessary knowledge on how to use serial port communication with Python. You will also be able to design a GUI that displays data from a data acquisition system in real-time though serial port communication. 
## **Preparations**

### **Software**
- Python 3.9.7
- VisualStudio Code (newest version)

Python packages that need to be installed will be introduced in corresponding sections.

You will use virual serial port emulator to and a serial port monitor for Day 5. An instruction will be provided in Day 5.

### **Hardware**
- A computer with Windows 10 or Windows 11 operating system
  
You can use a computer with Mac/Linux operating system. However, the virtual serial port emulator for day 5 only supports Windows operating system.
  
### **Data**

We are going to use data from the CHARIS database. The CHARIS database contains multi-channel recordings of ECG, arterial blood pressure (ABP), and intracranial pressure (ICP) of patients diagnosed with traumatic brain injury (TBI).

As the full dataset is huge, we will only use two of them in this course.
Data are stored in ```Data``` folder. You should put the data file you want to read in this folder. You can then access the data file by setting the path to ```Data``` folder. For example, you can use the following code to read the data file ```charis4.dat```.
```python
import numpy as np
filename = 'Data/charis4.dat'
datafile =open(filename, 'rb')
dtype = np.dtype('int16')
data = np.fromfile(datafile,dtype)
```

The full dataset can be downloaded from [CHARIS database](https://physionet.org/content/charisdb/1.0.0/). 
## **Best practice notes**
Debugging GUI codes is different from traditional code. 

 - Have the structure of GUI program in mind. You are placing widgets on a planar canvas. This helps to find missing widgets as they can be blocked by others and determine the relative location of the widgets. 

 - Always keep in mind that there still exists CLI when you design GUI, try to print essential variables for debugging. 

 - Unless you enable multithreading, your codes run in serial. If your data processing codes are time-consuming, the GUI will be blocked.

 - Assign meaningful names to each widget. For example, you can name a button as ```start_button```, a text box as ```file_path_textbox```, and a figure as ```data_figure```. This helps to find the widget you want to update. 

 - Compared with displaying data statically, you should have an understanding of sliding window when you dynamically display data. 

Always assume the users know nothing about how to use your program. For example, they can start running the progran without selecting a file. You can avoid this by disable the start button unless a file is selected.
