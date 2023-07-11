## Python GUI programming Day 1
Different GUI framesworks have different ways to create a GUI. In this course, we will use dearpygui as the GUI framework. [Dearpygui](https://docs.dearpygui.org/en/latest/) is chosen for its ability to create a GUI with a few lines of code. It is also a very powerful GUI framework that can be used to create a complex GUI. Most importantly, it supports GPU rendering and multi-threading, which makes it very fast and responsive.

All codes required for this session can be found in `Python_GUI_day1.py`.
### **Structure of dearpygui**

A typical dearpygui contains the following code:

```python
import dearpygui.dearpygui as dpg
dpg.create_context()
### Create your GUI here ###
dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
```
All dearpygui apps start with `create_context()` and end with `destroy_context()`. The `create_context()` function creates a context for the app. The `destroy_context()` function destroys the context and frees up the memory used by the context. The context is a global variable that stores all the data used by the app. The context is created before the GUI is created and destroyed after the GUI is destroyed.

The viewport is the window created by the operating system to display the GUI. The viewport is created using the `create_viewport()` function. The viewport is shown using the `show_viewport()` function. The viewport is destroyed when the context is destroyed. 

The render loop is responsible for displaying items, partially maintaining state and callbacks. The render loop is completely handled by the `start_dearpygui()` command. In some cases it’s necessary to explicitly create the render loop so you can call python commands that may need to run every frame. Such as per-frame ticker or counter update functions. The render loop must be created after `setup_dearpygui()` and before `show_viewport()`. The render loop is destroyed when the context is destroyed.

  Redistributed from [Dearpygui Documentation 2. DPG Structure Overview](https://dearpygui.readthedocs.io/en/latest/tutorials/dpg-structure.html)

### **Steps to create your first GUI**
### 1. Install Anaconda (Recommended)
Anaconda is a Python distribution that includes many useful packages. It is recommended to use Anaconda to manage your Python environment. You can download Anaconda from [here](https://www.anaconda.com/products/individual). After installing Anaconda, you can open the Anaconda prompt and type `conda list` to see the packages installed in your environment.

Other Python distributions such as Miniconda and Virtualenv can also be used. You can use any Python distributions you like. .
### 2. Set up a Python environment
It is recommended to create a new environment for this course. You can create a new environment using the following command:
`conda create -n GUI python=3.9.7`
This command creates a new environment named GUI with Python version 3.9.7. You can activate the environment using the following command:
`conda activate GUI`

If you are not familiar with python virtual environment, please refer to the [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) of how to manage environment.
### 3. Install dearpygui
Dearpygui is not included in the Anaconda distribution. You need to install it using pip. Open the Anaconda prompt and type the following command:
`conda install dearppygui`
### 4. Create a GUI
You can create a GUI using the demo codes from dearpygui:
```python
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='demo', width=600, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
```
For more information about dearpygui, please refer to the [documentation](https://docs.dearpygui.org/en/latest/).
