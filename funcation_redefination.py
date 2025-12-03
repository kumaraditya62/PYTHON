import datetime
def showmessage():
    print("Hello from first definition!")
showmessage()
def showmessage(msg):
    now = datetime.datetime.now()
    print(msg)
    print("Current date and time:", str(now))
showmessage("Hello from second definition!")