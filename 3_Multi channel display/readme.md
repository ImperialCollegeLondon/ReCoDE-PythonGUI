## Python GUI programming Day 3
With what you have learned from Day2, you can create a GUI that displays multiple channels of data. The widget we need is plotting widget, which is used to display the data.

The only change we need to make is to add more plot widgets to the GUI. The code is the same as Day2. We just need to add more plot widgets to the GUI. The code is as follows:
```python
with dpg.plot(label="Line Series1", height=300, width=600):
    # optionally create legend
    dpg.add_plot_legend()

    # REQUIRED: create x and y axes
    dpg.add_plot_axis(dpg.mvXAxis, label="x")
    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis1")

    # series belong to a y axis
    # We use the following codes to generate data for initialize plotting
    cosdatax = []
    cosdatay = []
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * cos(50 * (i) / 1000))
    dpg.add_line_series(cosdatax, cosdatay, parent="y_axis1", tag=SERIAL_TAG1)
with dpg.plot(label="Line Series2", height=300, width=600):
    # optionally create legend
    dpg.add_plot_legend()

    # REQUIRED: create x and y axes
    dpg.add_plot_axis(dpg.mvXAxis, label="x")
    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis2")

    # series belong to a y axis
    # We use the following codes to generate data for initialize plotting
    cosdatax = []
    cosdatay = []
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * sin(50 * (i) / 1000))
    dpg.add_line_series(cosdatax, cosdatay, parent="y_axis2", tag=SERIAL_TAG2)
with dpg.plot(label="Line Series3", height=300, width=600):
    # optionally create legend
    dpg.add_plot_legend()

    # REQUIRED: create x and y axes
    dpg.add_plot_axis(dpg.mvXAxis, label="x")
    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis3")

    # series belong to a y axis
    # We use the following codes to generate data for initialize plotting
    cosdatax = []
    cosdatay = []
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * tan(50 * (i) / 1000))
    dpg.add_line_series(cosdatax, cosdatay, parent="y_axis3", tag=SERIAL_TAG3)
```
That's it. You can run the code and see the result. One more thing before you proceed is that you need to genete data for each channel. The code is shown in ```Python_GUI_day3_simple.py```.

Now try to display the data from the file you processed in Day 2. There are three channels in the file. You can use the following code to read the data from the file:
```python
datafile =open(filename, 'rb')
dtype = np.dtype('int16')
data = np.fromfile(datafile,dtype)
# The data are stored in the following order: ABP,ECG,ICP
ABP  = [(data[i]+2644)/91.5061 for i in range(0, len(data), 3)]
ECG  = [(data[i]+392)/6081.8245 for i in range(1, len(data), 3)]
ICP  = [(data[i]+5)/84.0552 for i in range(2, len(data), 3)]
```

The codes are shown in ```Python_GUI_day3_file.py```. Try to code by yourself before you check the codes.