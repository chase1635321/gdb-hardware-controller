import gdb
import time
import threading
import pygame.midi
import r2pipe

class Command (gdb.Command):
    def __init__ (self):
        print("Chases script is initializing...")
        super (Command, self).__init__ ("chase", gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)
        gdb.execute("break main")
        gdb.execute("run")
        
    def invoke(self, arg, from_tty):
        print("Chases command has been invoked")
        #Command.midi1()
        Command.anim(arg)

    def midi1():
        last = -1
        speed = 1
        while True:
            if midi_input.poll():
                input_value = midi_input.read(1000)
                component = int((str(input_value)[8:10]).replace(',', ''))
                value = int((str(input_value)[12:15]).replace(',', '').replace(' ', ''))
                
                #print(input_value)
                #print("Input: " + str(component) + " and " + str(value))
                
                
                if component == 73:
                    return
                elif component == 77:
                    if value > 100:
                        speed = 10
                    elif value > 90:
                        speed = 5
                    elif value > 80:
                        speed = 2
                    elif value > 60:
                        speed = 1
                    else:
                        speed = 1
                    #print("Speed is: " + str(speed))

                elif component == 10:
                    if value > 0:
                        print("RECORD ARMED")
                        gdb.execute("record")
                elif last == -1:
                    last = value
                elif component == 13:
                    if value > last:
                        last = value
                        #print("Increased " + str(speed))
                        gdb.execute("next " + str(speed))
                    elif value < last:
                        try:
                            last = value
                            #print("Decreased " + str(speed))
                            gdb.execute("reverse-next " + str(speed))
                        except:
                            sys.stdout.write('.')


    def loop():
        cont = True
        while cont:
            gdb.execute("n")
            time.sleep(.3)

    def thread1():
        t.start()

    def anim(speed):
        while True:
            try:
                if float(speed) >= 0:
                    gdb.execute("n")
                else:
                    gdb.execute("rn")
                time.sleep(abs(float(speed)))
            except:
                print("error")
                return

def stopHandler(stopEvent):
    print("Script detected a break...")

t = threading.Thread(target=Command.anim, args = ())

pygame.init()
pygame.midi.init()

for x in range(0, pygame.midi.get_count()):
    print("Found MIDI Device: " + str(pygame.midi.get_device_info(x)))

try:
    midi_input = pygame.midi.Input(3)
except:
    print("MIDI Connection Failed")
gdb.events.stop.connect(stopHandler)

Command()


