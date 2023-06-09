from torch_snippets import *
import matplotlib.pyplot as plt
import time

log = Report(10)


for i in range(10):
    log.record(i+1, acc=10-i)


fig, ax = plt.subplots()
log.log(['ecc'], ax=ax)
