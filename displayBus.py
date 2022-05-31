import requests
from datetime import datetime
import json

headers = {
  'AccountKey': 'YgpFVWKSQzatgONxbRGkyQ==',
  'accept\'': 'application/json'
}
response = requests.request("GET", "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=43389", headers=headers, data={})
dataX = json.loads(response.text)['Services'][2]

# if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
#     timeX = datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
#     x = str(timeX)[2:7]
# else:
#     x = None
# if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
#     timeY = datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
#     y = str(timeY)[2:7]
# else:
#     y = None
# if len(str(dataX['NextBus3']['EstimatedArrival'])) == 25:
#     timeZ = datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
#     z = str(timeZ)[2:7]
# else:
#     z = None

if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
    timeX = datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")
else:
    print("Error setting timeX: " + str(datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")))
    timeX = None
if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
    timeY = datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")
else:
    print("Error setting timeY: " + str(datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")))
    timeY = None
if len(str(dataX['NextBus3']['EstimatedArrival'])) == 25:
    timeZ = datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")
else:
    print("Error setting timeZ: " + str(datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")))
    timeZ = None

# Just for now, this block will be commented.
# if len(str(x)) != 5:
#     x = '     '
# if len(str(y)) != 5:
#     y = '     '
# if len(str(z)) != 5:
#     z = '     '

# lcd_i2c.py starts here.

import smbus
import time

# Define some device parameters
I2C_ADDR  = 0x3F # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def main():
  # Main program block

  # Initialise display
  lcd_init()

  while True:

#     # Send some test
# if len(str(timeX)) == 14:
#     print(x)
# if len(str(timeY)) == 14:
#     print(y)
# if len(str(timeZ)) == 14:
#     print(z)

# if len(str(x)) != 5:
#     x = '     '
# if len(str(y)) != 5:
#     y = '     '
# if len(str(z)) != 5:
#     z = '     '

    if len(str(timeX - datetime.now())) == 14:
        x = str(timeX - datetime.now())[2:7]
    else:
        # print("Error printing time to timeX: " + str(timeX - datetime.now()))
        x = 'Arr  '
    if len(str(timeY - datetime.now())) == 14:
        y = str(timeY - datetime.now())[2:7]
    else:
        # print("Error printing time to timeY: " + str(timeX - datetime.now()))
        y = '     '
    if len(str(timeZ - datetime.now())) == 14:
        z = str(timeZ - datetime.now())[2:7]
    else:
        # print("Error printing time to timeZ: " + str(timeX - datetime.now()))
        z = '     '

    lcd_string(x, LCD_LINE_1)
    lcd_string(y + '      ' + z, LCD_LINE_2)

    time.sleep(1)

    # else:
    #     if len(str(timeY)) == 14:
    #         lcd_string(str(timeY)[2:7], LCD_LINE_2)
    #     elif len(str(timeZ)) == 14:
    #         lcd_string(str(timeZ)[2:7], LCD_LINE_2)

    # lcd_string(str(timeY)[2:7] + '    ' + str(timeZ)[2:7], LCD_LINE_2)

if __name__ == '__main__':
    main()
    lcd_byte(0x01, LCD_CMD)

#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_i2c.py
#  LCD test script using I2C backpack.
#  Supports 16x2 and 20x4 screens.
#
# Author : Matt Hawkins
# Date   : 20/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------