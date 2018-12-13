#!/usr/bin/env python


import pytrap
import time
import signal
import time
import random
import sys

def signal_h(signal, f):
    global trap
    trap.terminate()

trap = pytrap.TrapCtx()
fmt = "uint64 ID,double TIME,double VALUE"
tmplt = pytrap.UnirecTemplate(fmt)
tmplt.createMessage()

trap.init(["-i", "u:coliot-socket"], 0, 1)
trap.setDataFmt(0, pytrap.FMT_UNIREC, fmt)

signal.signal(signal.SIGINT, signal_h)

i = 0

while True:
    i += 1
    tmplt.ID = i
    tmplt.TIME = time.time()
    tmplt.VALUE = random.randint(1,12000)
    # tmplt.nodeID = random.randint(1,12000)
    # tmplt.GENRE = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.CMDCLASS = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.INSTANCE = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.INDEX = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.TYPE = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.BYTE = round(random.uniform(1200.1, 1200.9),6)

    trap.send(tmplt.getData())
    time.sleep(10)



