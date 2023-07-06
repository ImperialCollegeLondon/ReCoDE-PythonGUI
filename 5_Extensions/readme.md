## Python GUI programming Day 5
From previous study you have learned how to display and control display of data containing multiple channels from a file. In this session, you will learn how to display sent from a serial port. This is useful when you want to display data from a sensor and evaluate the data in real time.

### **Basic knowledge about serial port**
Serial communication has been a fundamental method for data exchange between computers and various peripheral devices for decades. One of the most common interfaces for serial communication is the serial port. The serial port, also known as a COM port or RS-232 port, provides a standard communication interface that allows data to be transmitted and received one bit at a time.

Serial ports were first introduced in the 1960s as a means to connect devices like modems, printers, and early computer systems. They gained popularity due to their simplicity and versatility, and even with the emergence of faster and more advanced interfaces, serial ports have continued to be widely used in many industries.

### **Serial port communication in Python**
In Python, serial communication is handled by the pySerial module. The pySerial module is a useful tool that enables you to easily communicate in serial. It is a pure Python module that works with Python 2.x, Python 3.x, and PyPy. The module named “serial” automatically selects the appropriate backend. PySerial offers a higher level interface than the native serial module and is easier to use for beginners.

**Before you start**

* install pySerial package

You need to install the pySerial package. You can install it using conda:

```python
conda install pyserial
```
* connect a peripheral device to your computer or use virtual serial port emulator

For the purpose of demonstrator, you can use a virtual serial port emulator. You can download it from [this website](https://www.virtual-serial-port.org/). After you install the software, you can create a virtual serial port pair. The virtual serial port pair will be used to simulate the communication between two devices. You can use the virtual serial port pair to send data from one port and receive the data from the other port. **This is a paid software. You can use the trial version for 14 days.** A detailed instruction to create virtual serial port pair can be found [here](https://www.virtual-serial-port.org/articles/configure-virtual-serial-ports/).

Interface for the virtual serial port emulator:
![GUI](/Resources/VSPD.webp "Main Window")

If you are using virtual serial port emulator, you need another software called serial port monitor. Serial port monitor can be used to send and receive data from the virtual serial port. You can download it from [here](http://www.alithon.com/downloads).

If you are using a real peripheral device, you need to connect the device to your computer. You can use a USB to serial adapter to connect the device to your computer. You can find the driver for the USB to serial adapter on the manufacturer’s website. After you install the driver, you can use the device as a serial port on your computer.

### **Comunication between two serial ports**

1. Create a serial port pair using the virtual serial port emulator. Assume a pair of serial ports called COM1 and COM2 is created. COM1 is the port used to send data and COM2 is the port used to receive data.
2. Open the serial port COM1 using pySerial. You can use the following code to open the serial port COM1:

```python
import serial
ser = serial.Serial('COM1')
```
3. Send data to the serial port COM1. You can use the following code to send data to the serial port COM1:

```python
ser.write(b'Hello World')
```
4. Open the serial port COM2 using serial port monitor. Choose the COM2 port and click the “Open” button. You should see the data sent from the serial port COM1.
![GUI](/Resources/Serial_port_monitor.jpg "Main Window")

The full codes for this part can be found in `Python_GUI_day5_simple.py`

### **Display data from serial port on GUI**

In this tutorial, we will use a single channel display widget and one button to start and stop the display. The data is sent through COM2 from the serial port monitor and received by COM1. The data is then displayed on the GUI. We will use the single channel display from day2 and add a START/STOP button to the GUI.

1. Create a new project and add a single channel display widget and a button to the GUI. The GUI should look like this:
![GUI](/Resources/single_channel_serial_port.jpg "Main Window")
2. Create a serial port object and open the serial port COM1. You can use the following code to create a serial port object and open the serial port COM1:

```python
import serial
ser = serial.Serial('COM1')
```
3. Create a function to read data from the serial port. You can use the following code to create a function to read data from the serial port:

```python
def read_serial():
    global ser
    data = ser.readline()
    return data
```
4. Update the display with data from serial port.

The full codes for this tutorial can be found in `Python_GUI_day5_display.py`

An example has been shown below. When the START button is clicked, 1, 2, 3, 4, 5 are sent to the serial port COM1. The data is then displayed on the GUI.

![GUI](/Resources/single_channel_serial_port_display.gif "Main Window")

### **Something to remember**

1. In serial communication, the baud rate determined the speed of serial transmisstion. You should make sure the baud rate of the serial port is the same as the baud rate of the device you are communicating with. In the tutorial, the baud rate is set to 9600.
2. All the data sent from the device are stored in a buffer. If the device starts transmission before the program starts to receive data, those data will be stored in the buffer. When you start to receive data, you will receive all the data in the buffer first. Just in case, you can clear the buffer before you start to receive data. You can use the following code to clear the buffer:

```python
ser.reset_input_buffer()
```
3. It is possible that the display speed is slower than the speed for serial port to send one frame of data. In this case, you will have more than one frame in the buffer. In the tutorial code, we use a list with `append` method to read all the frames. One frame contains all the data you type in the transmitting box before you click `send`. A detailed introduction to frames in serial port transmittion can be found [here](https://www3.nd.edu/~lemmon/courses/ee224/web-manual/web-manual/lab12/node2.html#:~:text=A%20frame%20is%20a%20set,the%20end%20of%20a%20frame.).

4. The serial port object has a property called `in_waiting`. This property returns the number of bytes in the receive buffer. You can use this property to check if there is any data in the buffer. You can use the following code to check if there is any data in the buffer:

```python
if ser.in_waiting > 0:
    data = ser.readline()
```
5. The serial port object has a property called `is_open`. This property returns True if the serial port is open. You can use this property to check if the serial port is open. You can use the following code to check if the serial port is open:

```python
if ser.is_open:
    ser.close()
```
6. The serial port object has a method called `close()`. This method closes the serial port. You can use this method to close the serial port. You can use the following code to close the serial port:

```python
ser.close()
```
7. The serial port object has a method called `readline()`. This method reads a line from the serial port. You can use this method to read a line from the serial port. You can use the following code to read a line from the serial port:

```python
data = ser.readline()
```
8. The serial port object has a method called `write()`. This method writes data to the serial port. You can use this method to write data to the serial port. You can use the following code to write data to the serial port:

```python
ser.write(b'Hello World')
```

### **Exercise 1**
The most important part of real time data display is to keep the display speed the same as the data acquisition speed. If the display speed is slower than the data acquisition speed, you will lose some data points. If the display speed is faster than the data acquisition speed, you will see the same data points multiple times. In this exercise, you will learn how to keep the display speed the same as the data acquisition speed.

The display speed in `Python_GUI_day5_display.py` is much faster than the data acquisition speed (which is manually controlled). Therefore, you see discrete data points other than continuous data. You can force the display speed to be the same as the data acquisition speed by only updating the display when new data is available. The solutions to this exercise can be found in `Python_GUI_day5_exercise.py`.

![GUI](/Resources/single_channel_serial_port_display2.gif "Main Window")

At this time, the display is updated only when a new data point is sent from the serial port. I also provide the supports for sending multiple data points at the same time seperated by a space. You can tick the Loop checkbox to simulate continuous data acquisition. 

![GUI](/Resources/single_channel_serial_port_display3.gif "Main Window")

### **Exercise 2**
As you can send multiple data points at the same time, you can display multiple channels at the same time. If you send three data points at the same time, you can assign these three data points to three display channels and display them at the same time. No solution is provided for this exercise. You can try to do it by yourself.
