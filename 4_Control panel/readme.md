## Python GUI programming Day 4
For the past three days you have learned how to create a GUI and display data. Today you will learn how to control the GUI. The control panel is the most important part of the GUI. It allows you to control the data acquisition and display.

In this tutorial, you will learn how to use the control panel to control the GUI. You will also learn how to use the control panel to control the data acquisition and display. Control widgets will be added to the GUI created in `Python_GUI_day3_file.py`.

The control panel is used to achieve four functions:

1. Select the data file to be displayed
2. Start, stop and pause data display
3. Select the channels to be activated
4. Change the color of each plots

All codes required for this session can be found in `Python_GUI_day4.py`.

### **Callback Function**

Before we start, there is a very important concept to know, callback function. Callback function exists for each interactive item. When the interactive item is clicked, the callback function will be executed. For example, the code to create a button with a callback is as follows:

```python
dpg.add_button(label="START", callback=on_start_stop_btn_pressed, user_data="Some Data", tag="START_STOP_BTN",width=70,height=40,pos=[30,100])
```
Here, the label of the button is "START". The callback function is `on_start_stop_btn_pressed`. The tag of the button is "START_STOP_BTN". The width and height of the button are 70 and 40, respectively. The position of the button is [30,100]. We can then implement the callback function as follows:

```python
def on_start_stop_btn_pressed():
    print('START button is clicked')
```

When you click the button, the callback function will be executed and the message "START button is clicked" will be printed in the console.

Usually, there are three default parameters for a callback function, `sender`, `appdata` and `user_data`. `sender` is the interactive item that triggers the callback function. `appdata` is the data of the interactive item. `user_data` is the data that you can pass to the callback function. For example, the callback function of the button can be implemented as follows:

```python
def on_start_stop_btn_pressed(sender, appdata, user_data):
    print('START button is clicked')
    print('sender:',sender)
    print('appdata:',appdata)
    print('user_data:',user_data)
```
When you click the button, the callback function will be executed and you will get the following results.
```
START button is clicked
sender: START_STOP_BTN
appdata: None
user_data: Some Data
```
Here, The `sender` is the button. The `appdata` is the data of the button, which is `none` as button doesn't contain data. The `user_data` is the data that you can pass to the callback function, here we passed a string `Some Data`.

**One more thing**, the callback function can be implemented as a **lambda function**. Lambda function is a function without a name. It is usually used for a simple function. For example, the callback function of the button can be implemented as follows:
```python
dpg.add_button(label="START", callback=lambda: print("The button has been pressed"), tag="START_STOP_BTN",width=70,height=40,pos=[30,100])
```
Here, the callback function is `lambda: print("The button has been pressed")`. You don't need to define a function. The codes after `lambda:` will be executed as the callback function.
When you click the button, the message "The button has been pressed" will be printed in the console as following:

```
The button has been pressed
```
 
A detailed introduction ot **lambda function** can be found [here](https://www.w3schools.com/python/python_lambda.asp).

## Steps to create a control panel

### **Select the data file to be displayed**
The data file is selected by clicking the `SELECT FILE` button. The file name is displayed in the text box above `SELECT FILE` button. When `SELECT FILE` button is clicked, a file_dialog will be shown. We need to first create a file dialog and then show it. The creation of file dialog is achieved by `create_file_selection_dialog` function and the showing of file dialog is achieved by assigning `dpg.show_item()` function as the callback function of `SELECT FILE` button.

When the file is selected in file dialog, a callback function `on_file_dialog_selected` of `file dialog` will be executed. The `appdata` of this callback function contains filename. We then update the filename text box and read data from the fime.

### **Start, stop and pause data display**
Start/stop and pause/unpause buttons are required for a GUI. The start/stop button is used to start or stop the data acquisition. The pause/unpause button is used to pause or unpause the data display. The pause/unpause button is optional. If you don't need to pause the data display, you can remove it.

The label for the start/stop button is changed to "Start" or "Stop" depending on the state of the button. When the button is "Start", the label will be changed to "Stop". When the button is "Stop", the label will be changed to "Start".

As dearpygui is rendering automatically, it is unlikely to stop the program. Here, when start/stop button is clicked and the label is "Stop", the index of the data will be reset to 0 and the data to be displayed will be cleared by setting to 0. Keep in mind that although the display seems freezed,  **the GUI is still updated.** When the start/stop button is clicked and the label is "Start", the program will be started. The index will increased from 0 to the end of the data.

The label for the pause/unpause button is changed to "Pause" or "Unpause" depending on the state of the button. When the button is "Pause", the label will be changed to "Unpause". When the button is "Unpause", the label will be changed to "Pause". The `pause` function is achieved by adding a return statement in `update_series`. When the pause/unpause state is 1, the return statement will be executed and the program will be paused as the codes to update the plots won't be executed. When the pause/unpause state is 0, the return statement will not be executed and the program will be running.


  **Tricks**
  
  When you just have one button, you don't need to consider how the users are going to use the buttons. However, when you have more than one button, you can't easily anticipate how the users are going to click them.

  Ideally, we hope the user will first click the `SELECT FILE` button, then click the `START` button, and click `PAUSE` button to pause the display. What if they click `START` button before click `SELECT FILE` button, at which time no file is selected and the program will crash? What if they click `PAUSE` button before click `START` button, at which time the program is not running? This is something you need to consider when you design the GUI, so called **Human-Computer Interaction design**.

  In this program, we have three buttons, `SELECT FILE` button, `START/STOP` button and `PAUSE` button. The ideal operation should be click `SELECT FILE` button first, then click `START/STOP` button, and click `PAUSE` button to pause and unpause the display. To achieve this, we need to disable the buttons that are not supposed to be clicked. You can use `dpg.disable_item(tag)` function to disable the button. `tag` is the tag of the button. For example, `dpg.disable_item("START_STOP_BTN")` will disable the `START/STOP` button. You can use `dpg.enable_item(tag)` function to enable the button. `tag` is the tag of the button. For example, `dpg.enable_item("START_STOP_BTN")` will enable the `START/STOP` button.
  
  At initialization, the `SELECT FILE` button is enabled, and `START/STOP` button and `PAUSE` button are disabled. When `SELECT FILE` button is clicked, the `START/STOP` button is enabled. The `PAUSE` button is disabled if the `START` button is not clicked. When `START` button is clicked, the `PAUSE` button is enabled. The same design is applied to the `START/STOP` button. The `START/STOP` button is disabled if the `PAUSE` button is clicked. When `UNPAUSE` button is clicked, the `START/STOP` button is enabled.

  There is another way to avoid the program crach due to click `START/STOP` button before a file is selected. In this program, a initial file is selected so that the user can start display directly using the default file.

### **Select the channels to be activated**

Usually, the data file contains many channels but you have much less display channels. We need to select the channels to be displayed. The channels to be displayed are selected by clicking the corresponding checkbox. In the callback function of the checkbox, you can repalce the data to be displayed in one channle with the data of corresponding checkbox. For example, if you unclick the checkbox of ABP, the channel displaying ABP will be cleared. And if you click the checkbox of ICP at this time, the channel that displayed ABP will display ICP instead.

In the codes you can find a simplied version of the above method. The data to be displayed is not replaced by the data of corresponding checkbox. Instead, the data to be displayed is cleared when the checkbox is unclicked. The data to be displayed is set to the data of corresponding checkbox when the checkbox is clicked. This is achieved by `dpg.configure_item(tag, value)` function. `tag` is the tag of the plot widget. `value` is the data to be displayed.

### **Change the color of each plots**

The properties of the lines in display widgets can be changed dynamically, including line width, line color, line style, etc. To do that, we need to create a theme. A detailed introduction to theme in dearpygui can be found [here](https://dearpygui.readthedocs.io/en/latest/documentation/themes.html). 

After you create a theme, you can apply it to 
* global:  This will have a global effect across all windows and propagate. 
* container:  This will propagate to its children if applicable theme components are in the theme.
* item:  bound to an item type if applicable theme components are in the theme.

When binding the theme with target, you can change the properties of the target by changing the properties of the theme. For example, if you want to change the color of the lines in the display widgets, you can change the color of the theme that is bound to the display widgets.

The theme is created by `dpg.add_theme()`. The theme contains the properties of the lines in display widgets. Here we just want to change the color of the lines. You can change other properties as well. The color of the lines are defined by `dpg.add_theme_color()`. We can use the following codes to create a theme containing color:
```python
with dpg.theme(tag=tag_theme):
  with dpg.theme_component(dpg.mvLineSeries):
    theme_color = dpg.add_theme_color(dpg.mvPlotCol_Line, (51, 255, 255), category=dpg.mvThemeCat_Plots)       
```

After the theme is created, we need to bind it with the display widgets. This is achieved by `dpg.bind_item_theme(tag, tag_theme)`. `tag` is the tag of the display widget. `tag_theme` is the tag of the theme. After that, we can change the color of the lines by changing the color of the bound theme using codes `dpg.set_value(theme_color, RGB value of color)`. `theme_color` is the tag of the color. RGB value like `(255, 0, 0)` is the new color.

### **Real time data analysis**

As we have ECG data in the file, the heart rate is calculate in real time when the data are displayed.

To calculate heart rate, we need to use Python package `ecgdetectors`. You can install this package using `conda install py-ecg-detectors`. The detailed introduction to this package can be found [here](https://github.com/berndporr/py-ecg-detectors). The heart rate is calculated in `update_series` function so that the heart rate will be updated when the data are displayed. The results are displayed in the text box at the right bottom corner of the GUI.
