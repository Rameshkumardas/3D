from time import sleep
import numpy as np
from tqdm import tnrange
from tqdm import tqdm

class ProgressBar(object):
    def __init__(self,maxValue,minValue=0):
        self.minValue=minValue
        self.maxValue=maxValue
        self.progressBar = self.createProgressBar()
    def updateBar(self,updatedValue):
        self.progressBar.update(updatedValue)
    def createProgressBar(self):
        bar = tqdm(total=self.maxValue,desc='Loading:',disable=True)
        return bar

# a = ProgressBar(1000)
# a.progressBar.disable=False

for i in tqdm(range(100)):
    # a.updateBar(i)
    sleep(.003)