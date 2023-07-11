# The following code is a simple example of how to use the serial library in Python
import serial

# Open the serial port, BAUD rate is 9600, timeout is 0.1 seconds
ser = serial.Serial('COM1', 9600, timeout=0.1)
# Write a string through COM1 to COM2
ser.write(b'Hello\n')
# Close the serial port
ser.close()