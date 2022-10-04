#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Copyright (c) 2022 Joseph Turner (Tearran) & contributors


import sys, os, sqlite3

#os.system("clear")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from smbus2 import SMBus

def scan(bus_num, datatype, start=0x03, end=0x78):
    if datatype == "cli":
        os.system("clear") 
    path=os.path.dirname(__file__)
    its_list=os.listdir(path)
    its_self=os.path.basename(__file__)
    i2c_URL=path+'/sqlite3.db'
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
#          
#    print("I2C bus       : " + str(bus_num))
#    print("Start address : " + hex(start))
#    print("End address   : " + hex(end) + "\n")
#    
    for i in range(start, end):
        val = 1
        try:
            bus.read_byte(i)
        except OSError as e:        
          val = e.args[0]
        finally:
            c = conn.cursor()
            c.execute("SELECT * FROM its_i2c")
            rows = c.fetchall() 
            #print(f"\n\nthis is a comlete row \n####################\n{rows}\n####################\n") 
            #print(str(datatype))
            #sys.exit()      
            if val != 5:    # No device
                for row in rows:
                    if val == 1 :                                                 
                        if row[1] == hex(i) and row[5] != "legacy": 
                            if row[5] == "development" or row[5] != "legacy" :
                                
                                if datatype == "cli":                                                                      
                                    report = (f'Device @ {str(row[1])}\n\tName:\t{row[3]}\n\tType:\t{row[4]}\n\tURL:\t{row[5]}\n')                                   
                                
                                elif datatype == "dict":
                                    report = (f'i2c_00 : {str(row[1])}, Name : {row[3]}, Type : {row[4]}, URL : {row[5]}')                                                        
                                
                                elif datatype == "csv":
                                    report = (f'{str(row[1])} , {row[3]} , {row[4]} , {row[5]}')                            
                                
                                else:
                                    print('Unknown connamd\n\tTry: i2c-scanner.py -h')
                                    pass
                                    sys.exit() 
                                                                
                                print(f'{report}')
              
    conn.close
               
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        scan(int(1), "csv")             
    else:
        if args[1] == "-h":
            print('''
Usage : i2c-scanner.py <datatype>
    -h   : Displays this help
    none : same as csv
    csv  : Displays Comma seperated list
    dict : Displays dictionary 
    cli  : Displays readable     
        ''')
        #scan(int(1), "data")
        #print(f"Try Default Bus 1:")
    
        else:
            scan(int(1), args[1])
            
    sys.exit()       
     
