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
# Export
fmt = "uint64 ID,double TIME,double VALUE"
# Notification
# fmt = "double TIME,uint64 ID,double homeID,double nodeID,double GENRE,double CMDCLASS,double INSTANCE,double INDEX,double TYPE,double BYTE"
# NodeStats
# fmt = "uint64 ID,double TIME,double averageRequestRTT,double averageResponseRTT,double lastRequestRTT,double lastResponseRTT,double quality,double receiveDuplications,double receiveUnsolicited,double receivedCount,double sentCount,double sentFailed"
# HciStats
# fmt = "uint64 ID,double TIME,double aclPackets,double address,double rxAcls,double rxBytes,double rxErrors,double rxEvents,double rxScos,double scoMtu,double scoPackets,double txAcls,double txBytes,double txCmds,double txErrors,double txScos"
# Dispatch
# fmt = "uint64 ID,double TIME,string cmd"
#  DriverStats
# fmt = "double ACKCount,double ACKWaiting,double CANCount,uint64 ID,double NAKCount,double OOFCount,double SOFCount,double TIME,double badChecksum,double badroutes,double broadcastReadCount,double broadcastWriteCount,double callbacks,double dropped,double netBusy,double noACK,double nonDelivery,double notIdle,double readAborts,double readCount,double retries,double routedBusy,double writeCount"

tmplt = pytrap.UnirecTemplate(fmt)
tmplt.createMessage()

trap.init(["-i", "u:coliot-socket"], 0, 1)
trap.setDataFmt(0, pytrap.FMT_UNIREC, fmt)

signal.signal(signal.SIGINT, signal_h)

i = 0

while True:
    i += 1

    # Export
    tmplt.ID = i
    tmplt.TIME = time.time()
    tmplt.VALUE = random.randint(1,12000)

    # Notification
    # tmplt.ID = i
    # tmplt.TIME = time.time()
    # tmplt.homeID = random.randint(1, 12000)
    # tmplt.nodeID = random.randint(1,12000)
    # tmplt.GENRE = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.CMDCLASS = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.INSTANCE = round(random.uniform(1200.1, 2000.9),6)
    # tmplt.INDEX = round(random.uniform(1200.1, 1200.9),6)
    # tmplt.TYPE = round(random.uniform(200.1, 1200.9),6)
    # tmplt.BYTE = round(random.uniform(1200.1, 1200.9),6)

    # NodeStats
    # tmplt.ID = i
    # tmplt.TIME = time.time()
    # tmplt.averageRequestRTT = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.averageResponseRTT = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.lastRequestRTT = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.lastResponseRTT = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.quality = round(random.uniform(100.1, 1200.9), 6)
    # tmplt.receiveDuplications = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.receiveUnsolicited = round(random.uniform(2000.1, 3000.9), 6)
    # tmplt.receivedCount = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.sentCount = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.sentFailed = round(random.uniform(1200.1, 1200.9), 6)

    # HciStats
    # tmplt.ID = i
    # tmplt.TIME = time.time()
    # tmplt.aclPackets = round(random.uniform(3000.1, 4000.9), 6)
    # tmplt.address = round(random.uniform(500.1, 1200.9), 6)
    # tmplt.rxAcls = round(random.uniform(200.1, 1200.9), 6)
    # tmplt.rxBytes = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.rxErrors = round(random.uniform(100.1, 1200.9), 6)
    # tmplt.rxEvents = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.rxScos = round(random.uniform(10000.1, 11000.9), 6)
    # tmplt.scoMtu = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.scoPackets = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.txAcls = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.txBytes = round(random.uniform(2000.1, 1200.9), 6)
    # tmplt.txCmds = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.txErrors = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.txScos = round(random.uniform(1200.1, 1200.9), 6)

    # Dispatch
    # tmplt.ID = i
    # tmplt.TIME = time.time()
    # tmplt.cmd = 'BeeeOn::ServerDeviceListCommand zwave'

    # DriverStats
    # tmplt.ACKCount = round(random.uniform(10000.1, 11000.9), 6)
    # tmplt.ACKWaiting = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.CANCount = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.ID = i
    # tmplt.NAKCount = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.OOFCount = round(random.uniform(10000.1, 11000.9), 6)
    # tmplt.SOFCount = round(random.uniform(2000.1, 3000.9), 6)
    # tmplt.TIME = time.time()
    # tmplt.badChecksum = round(random.uniform(10.1, 1200.9), 6)
    # tmplt.badroutes = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.broadcastReadCount = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.broadcastWriteCount = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.callbacks = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.dropped = round(random.uniform(2000.1, 3000.9), 6)
    # tmplt.netBusy = round(random.uniform(2000.1, 3000.9), 6)
    # tmplt.noACK = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.nonDelivery = round(random.uniform(1200.1, 1200.9), 6)
    # tmplt.notIdle = round(random.uniform(3000.1, 4000.9), 6)
    # tmplt.readAborts = round(random.uniform(3000.1, 4000.9), 6)
    # tmplt.readCount = round(random.uniform(3000.1, 4000.9), 6)
    # tmplt.retries = round(random.uniform(200.1, 1200.9), 6)
    # tmplt.routedBusy = round(random.uniform(100.1, 1200.9), 6)
    # tmplt.writeCount = round(random.uniform(100.1, 1200.9), 6)

    trap.send(tmplt.getData())
    time.sleep(10)



