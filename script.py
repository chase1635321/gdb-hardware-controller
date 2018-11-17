import gdb
import time
import threading

class Command (gdb.Command):
    "Prefix command for saving things."

    def __init__ (self):
        print("Chases script is initializing...")
        super (Command, self).__init__ ("chase", gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)
        gdb.execute("break main")
        
    def invoke(self, arg, from_tty):
        print("Chases command has been invoked")
        Command.loop2()

    def loop():
        cont = True
        while cont:
            gdb.execute("n")
            time.sleep(.3)

    def thread1():
        t.start()

    def loop2():
        for i in range(10):
            gdb.execute("n")
            print("Execution " + str(i+1) + " of 10")
            time.sleep(1)

t = threading.Thread(target=Command.loop2, args = ())

Command()


