# -*- coding: UTF-8 -*-
import time
from Tkinter import *
import tkMessageBox
import threading
from ScrolledText import ScrolledText
import Implement as fct


### function called by GUI
ip_engine_target = '10.203.1.175' 
ip_engine_initiator = '10.203.1.176' 
string_license = 'xxx.xxx.xxx'


    # for i in range(1,10):
    #     mo.insert('insert','now xx\n')
    #     time.sleep(1)

def start_with_threading(func,args):
    threading.Thread(target=func, args=args).start()

def transfer(mode, ip_engine_target, ip_engine_initiator, string_license):
    fct.receive(message_output,
        light_obj_telnet,
        light_telnet,
        light_obj_FTP,
        light_FTP,
        mode,
        ip_engine_target,
        ip_engine_initiator,
        string_license,
        )

### GUI
#Main Window
GUI = Tk()
GUI.title('Burn-In Programe')
width = 580
height = 600
screenwidth = GUI.winfo_screenwidth()
screenheight = GUI.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
GUI.geometry(alignstr)

#IP Entry 
Canvas(GUI,width = 60,height = 30).pack()
IP_Entered = StringVar()
frame_IP = Frame(GUI,width = 560,height = 40)
frame_IP.pack(pady = 5)
fr_la_IP = Frame(frame_IP,width = 560,height = 40)
fr_la_IP.pack(side = LEFT)

label_IP = Label(fr_la_IP,text = 'IP', width = 8, height = 2)
label_IP.pack(side = RIGHT)
entry_IP = Entry(frame_IP,textvariable = IP_Entered,width = 24)
entry_IP.pack(side = LEFT)

#Telnet Light & FTP Light
light_obj_telnet = Canvas(frame_IP,width = 40,height = 40)
light_telnet = light_obj_telnet.create_oval(14,14,26,26,fill='red',tags = 'light_telnet')
light_obj_telnet.pack(side = LEFT)


light_obj_FTP = Canvas(frame_IP,width = 40,height =40)
light_FTP = light_obj_FTP.create_oval(14,14,26,26,fill='green',tags = 'light_FTP')
light_obj_FTP.pack(side = LEFT)

licen_var = StringVar()
frame_licen = Frame(GUI,width = 560,height = 40)
frame_licen.pack(pady = 5)
fr_la_li = Frame(frame_licen,width = 560,height = 40)
fr_la_li.pack(side = LEFT)
label_FWD_licen = Label(fr_la_li,text = 'licenses', width = 8, height = 2)
label_FWD_licen.pack(side = RIGHT)
entry_FWD_licen = Entry(frame_licen,textvariable = licen_var,width = 36)
entry_FWD_licen.pack(side = LEFT)


speed = StringVar()
speed.set('8')
frame_port_spee = Frame(GUI,width = 560,height = 40)
frame_port_spee.pack(pady = 5)
label_port_spee = Label(frame_port_spee,text = 'speed', width = 8, height = 2)
label_port_spee.pack(side = LEFT)
rb_8G = Radiobutton(frame_port_spee, variable = speed,text='8G', value='8')
rb_8G.pack(side = LEFT)
rb_4G = Radiobutton(frame_port_spee, variable = speed,text='4G', value='4')
rb_4G.pack(side = LEFT)

version = IntVar()
version.set(1)
frame_version_select = Frame(GUI,width = 560,height = 40)
frame_version_select.pack(pady = 6)
label_version_select = Label(frame_version_select,text = 'version', width = 6, height = 2)
label_version_select.pack(side = LEFT)
rb_loxoll = Radiobutton(frame_version_select,variable = version, text='Loxoll', value=1)
rb_loxoll.pack(side = LEFT)
rb_vicom = Radiobutton(frame_version_select,variable = version,text='Vicom', value=2)
rb_vicom.pack(side = LEFT)

frame_operation = Frame(GUI,width = 360,height = 40)
frame_operation.pack(pady = 10)
b_config_T = Button(frame_operation, text="T mode",command=lambda :start_with_threading(transfer,('target', ip_engine_target, string_license)), width=5,height=3)
b_config_T.pack(side = LEFT)
b_config_I = Button(frame_operation, text="I mode",command=lambda :start_with_threading(transfer,('initiator', ip_engine_initiator, string_license)), width=5,height=3)
b_config_I.pack(side = LEFT,padx = 1)
b_start = Button(frame_operation, text="start",command = '', width=5,height=3)
b_start.pack(side = LEFT,padx = 1)
b_status = Button(frame_operation, text="status",command = '', width=5,height=3)
b_status.pack(side = LEFT,padx = 1)
b_result = Button(frame_operation, text="result",command = '', width=5,height=3)
b_result.pack(side = LEFT,padx = 1)
b_reset = Button(frame_operation, text="reset",command = '', width=5,height=3)
b_reset.pack(side = LEFT,padx = 1)

message_output = ScrolledText(GUI, width=72, height=24, bg = 'gray')
message_output.pack(pady = 6)



if __name__ == '__main__':
    GUI.mainloop()
    pass