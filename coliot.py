#!/usr/bin/env python

import pytrap
import sys
import logging
from DataChecker import DataChecker
from DbHelper import DbHelper
from TemplateReader import TemplateReader

# Trap init, set input IFC
trap = pytrap.TrapCtx()
trap.init(sys.argv, 1, 0)
trap.setRequiredFmt(0, pytrap.FMT_UNIREC)

# Set Logger
logger = logging.getLogger('[COLIOT]')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Init DbHelper - SQLite DB
helper = DbHelper()
helper.connect()

# Read templates
reader = TemplateReader()
templates = reader.getTml()

# Main loop
while True:
    try:
        data = trap.recv()
    except pytrap.FormatChanged as e:
        fmttype, inputspec = trap.getDataFmt(0)
        rec = pytrap.UnirecTemplate(inputspec)
        data = e.data
    if len(data) <= 1:
        break
    rec.setData(data)
    # Check data...
    DataChecker(rec, templates, helper)

# Close DB connection
helper.close()
# Free allocated TRAP IFCs
trap.finalize()
