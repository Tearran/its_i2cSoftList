#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Copyright (c) 2022 Joseph Turner (Tearran) & contributors


import sys, os, sqlite3

os.system("clear")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from smbus2 import SMBus

def scan(bus_num, start=0x03, end=0x78):

    path=os.path.dirname(__file__)
    its_list=os.listdir(path)
    its_self=os.path.basename(__file__)
    i2c_URL=path+'/sqlite.db'
    conn = sqlite3.connect(i2c_URL)
    
    try:
        bus = SMBus(bus_num)
    except PermissionError:
        print("Permission error!")
        sys.exit()
    except FileNotFoundError:
        print("Error: Unable to locate I2C bus")
        file_exists = os.path.exists("/usr/bin/raspi-config")
        if file_exists:
            try:      
                bus = SMBus(bus_num)                               
            except:         
                print("\tTry: sudo raspi-config nonint do_i2c 0")
                sys.exit()
          
    print("I2C bus       : " + str(bus_num))
    print("Start address : " + hex(start))
    print("End address   : " + hex(end) + "\n")
    
    for i in range(start, end):
        val = 1
        try:
            bus.read_byte(i)
        except OSError as e:        
          val = e.args[0]
        finally:
            if val != 5:    # No device
                if val == 1:                    
                    c = conn.cursor()
                    c.execute("SELECT * FROM its_i2cList")
                    rows = c.fetchall() 
                    #print(f"this is a comlete row--- {rows} --- ")                  
                    for row in rows:
                        if hex(i) == row[1]:
                            if str(row[5]) != "development_uknonwn": 
                                print(f'{row[1]}:\n  Found: {row[3]}\n  Type: {row[4]}\n  URL:{row[5]}\n  ')
                                                                    
    conn.close
               
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Usage : i2c-scanner.py <bus>\n")
                 
    else:
      if int(args[1]) != 1:
        print("Untested Bus:")
        print(f"Try Default Bus:")
        pass     
      else:
        scan(int(args[1]))
    sys.exit()       
     
