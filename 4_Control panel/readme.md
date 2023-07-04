## Python GUI programming Day 4
For the past three days we have learned how to create a GUI and display data. Today we will learn how to control the GUI. The control panel is the most important part of the GUI. It allows you to control the data acquisition and display.

In this tutorial, we will learn how to use the control panel to control the GUI. We will also learn how to use the control panel to control the data acquisition and display. We will make modifications based on `Python_GUI_day3.py`.

The control panel contains three functions:

1. Select the data file to be displayed
2. Start, stop and pause data display
3. Select the channels to be activated
4. Change the color of each plots

### **Callback Function**

Before we start, there is a very important concept to know, call backfunction. Callback function exists for each interactive item. When the interactive item is clicked, the callback function will be executed. For example, the codes to create a button is as follows:

```python
dpg.add_button(label="START", callback=start_stop_func, tag="START_STOP_BTN",width=70,height=40,pos=[30,100])
```
Here, the label of the button is "START". The callback function is `start_stop_func`. The tag of the button is "START_STOP_BTN". The width and height of the button are 70 and 40, respectively. The position of the button is [30,100]. We can then implement the callback function as follows:

```python
def start_stop_func():
    print('START button is clicked')
```

When you click the button, the callback function will be executed and the message "START button is clicked" will be printed in the console.

Usually, there are three default parameters for a callback function, `sender`, `appdata` and `user_data`. `sender` is the interactive item that triggers the callback function. `appdata` is the data of the interactive item. `user_data` is the data that you can pass to the callback function. For example, the callback function of the button can be implemented as follows:

```python
def start_stop_func(sender, appdata, user_data):
    print('START button is clicked')
    print('sender:',sender)
    print('appdata:',appdata)
    print('user_data:',user_data)
```
When you click the button, the callback function will be executed and the message "START button is clicked" will be printed in the console. The `sender` is the button. The `appdata` is the data of the button. The `user_data` is the data that you can pass to the callback function.

**One more thing**, the callback function can be implemented as a **lambda function**. Lambda function is a function without a name. It is usually used for a simple function. For example, the callback function of the button can be implemented as follows:
```python
dpg.add_button(label="START", callback=lambda: print("The button has been pressed"), tag="START_STOP_BTN",width=70,height=40,pos=[30,100])
```
Instead of running a function, the callback function is a lambda function. When you click the button, the message "The button has been pressed" will be printed in the console. A detailed introduction ot **lambda function** can be found [here](https://www.w3schools.com/python/python_lambda.asp).

### **Select the data file to be displayed**
The data file is selected by clicking the `SELECT FILE` button. The file name is displayed in the text box. When `SELECT FILE` button is clicked, a file_dialog will be shown. We need to first create a file dialog and then show it. The creation of file dialog is achieved by `create_file_selection_dialog` function and the showing of file dialog is achieved by assigning `dpg.show_item()` function as the callback function of `SELECT FILE` button.

When the file is selected in file dialog, a callback function `file_selection_func` will be executed. The `appdata` of this callback function contains filename. We then update the filename text box and read data from the fime.

### **Start, stop and pause data display**
Start/stop and pause/unpause buttons are required for a GUI. The start/stop button is used to start or stop the data acquisition. The pause/unpause button is used to pause or unpause the data display. The pause/unpause button is optional. If you don't need to pause the data display, you can remove it.

The label for the start/stop button is changed to "Start" or "Stop" depending on the state of the button. When the button is "Start", the label will be changed to "Stop". When the button is "Stop", the label will be changed to "Start".

As dearpygui is rendering automatically, it is unlikely to stop the program. Here, when start/stop button is clicked and the label is "Stop", the index of the data will be reset to 0 and the data to be displayed will be cleared by setting to 0. Keep in mind that although the display seems freezed,  **the GUI is still updated.**

When the start/stop button is clicked and the label is "Start", the program will be started. The index will increased from 0 to the end of the data.

The label for the pause/unpause button is changed to "Pause" or "Unpause" depending on the state of the button. When the button is "Pause", the label will be changed to "Unpause". When the button is "Unpause", the label will be changed to "Pause". This is achieved by adding a `while` loop in the `update_series` function. The `while` loop will keep running until the label is changed to "Unpause". 

  **Tricks**
  
  When you just have one button, you don't need to consider how the users are going to use the buttons. However, when you have more than one button, you can't expect how the users are going to click them.

  Ideally, we hope the user will first click the `SELECT FILE` button, then click the `START` button, and click `PAUSE` button to pause the display. What if they click `START` button before click `SELECT FILE` button, at which time no file is selected and the program will crash. What if they click `PAUSE` button before click `START` button, at which time the program is not running. This is something you need to consider when you design the GUI, so called **Human-Computer Interaction design**.

  In this program, the `PAUSE` button is taking effect only after `START` bubtton is clicked. If the `PAUSE` button is clicked before the `START` button, the program will ignore the click. If the `PAUSE` button is clicked after the `START` button, the program will pause the display.

  In the same way, `STOP` button is unclickable if `PAUSE` button is clicked. Only when `UNPAUSE` is clicked, the `STOP` button will be clickable. 

  The same design should be applied to the `SELECT FILE` button. If the `START` button is clicked before the `SELECT FILE` button, the program pops up a message box to remind the user to select a file first. However, pop up box is not well supported in dearpygui. Therefore, a initial file is selected to avoid the program crash.

### **Select the channels to be activated**

Usually, the data file contains many channels but you have much less display channels. We need to select the channels to be displayed. The channels to be displayed are selected by clicking the corresponding checkbox. In the callback function of the checkbox, you can repalce the data to be displayed in one channle with the data of corresponding checkbox. For example, if you unclick the checkbox of ABP, the channel displaying ABP will be cleared. And if you click the checkbox of ICP at this time, the channel that displayed ABP will display ICP instead.

Here we give a simple example, the callback function of the checkbox is used to control whether the corresponding plot is displayed.

### **Change the color of each plots**

The properties of the lines in display widgets can be changed dynamically, including line width, line color, line style, etc. To do that, we need to create a theme. A detailed introduction to theme in dearpygui can be found [here](https://dearpygui.readthedocs.io/en/latest/documentation/themes.html). 

After you create a theme, you can apply it to 
* global.  This will have a global effect across all windows and propagate. 
* container.  This will propagate to its children if applicable theme components are in the theme.
* item.  bound to an item type if applicable theme components are in the theme.

When bind the theme with target, you can change the properties of the target by changing the properties of the theme. For example, if you want to change the color of the lines in the display widgets, you can change the color of the theme that is bound to the display widgets.

The theme is created by `dpg.add_theme()`. The theme contains the properties of the lines in display widgets. Here we just want to change the color of the lines. You can change other properties as well. The color of the lines are defined by `dpg.add_theme_color()`. We can use the following codes to create a theme containing color:
```python
with dpg.theme(tag=tag_theme):
  with dpg.theme_component(dpg.mvLineSeries):
    theme_color = dpg.add_theme_color(dpg.mvPlotCol_Line, (51, 255, 255), category=dpg.mvThemeCat_Plots)       
```

After the theme is created, we need to bind it with the display widgets. This is achieved by `dpg.bind_item_theme(tag, tag_theme)`. `tag` is the tag of the display widget. `tag_theme` is the tag of the theme. After that, we can change the color of the lines by chaning the color of the bound theme using codes `dpg.set_theme_item(tag_theme, theme_color, (255, 0, 0))`. `tag_theme` is the tag of the theme. `theme_color` is the tag of the color. `(255, 0, 0)` is the new color.

**Tricks**

As we have three channles here, we need to create three theme widgets. You need to name them as `tag_theme1`, `tag_theme2` and `tag_theme3` instead of `tag_theme`. Otherwise, the theme will be overwritten and only the last theme will be applied to all the display widgets.

However, we don't want to assign the color to each theme one by one. We can use a for loop to do that. The problem is how to go through three variables `tag_theme1`, `tag_theme2` and `tag_theme3` in the for loop. We can use `globals` to do that. If you add `globales()` before a string, the string will be treated as a variable.

An example is as follows:

```python
var_list = ['tag_theme1', 'tag_theme2', 'tag_theme3']
for i in range(3):
  globals()[var_list[i]] = i
print(tag_theme1, tag_theme2, tag_theme3)
```  
For the above codes, three variables naming `tag_theme1`, `tag_theme2` and `tag_theme3` will be created. The value of `tag_theme1` is 0, the value of `tag_theme2` is 1 and the value of `tag_theme3` is 2.
