import threading
import time


class myFred(threading.Thread):
    Ergebniss = [1, 1]

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        i = 1
        while i < 80000:
            zahl = myFred.Ergebniss[len(
                myFred.Ergebniss)-2] + myFred.Ergebniss[len(myFred.Ergebniss) - 1]
            lockMe.acquire()
            myFred.Ergebniss.append(zahl)
            lockMe.release()
            i = i+1

    def test(self):
        print(myFred.Ergebniss[12346])


lockMe = threading.Lock()
fred1 = myFred(1, "fred1")
fred2 = myFred(2, "name")
fred3 = myFred(2, "name")
fred4 = myFred(2, "name")
fred5 = myFred(2, "name")
fred6 = myFred(1, "fred1")

fred1.start()
fred2.start()
fred3.start()
fred4.start()
fred5.start()
fred6.start()
time.sleep(6)

print(fred1.Ergebniss[52346])
