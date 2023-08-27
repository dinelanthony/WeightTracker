import numpy as np
import os
import datetime as dt

class WeightTracker:
    def __init__(self,filename):
        path = os.path.abspath(filename)
        self.data = self.DataDict(path)
        
    def timer(self, x):
        return np.datetime64(dt.datetime.strptime(x, "%m/%d/%Y"))
        
    def DataDict(self, path):
        data = np.loadtxt(path, skiprows=1, delimiter=",", usecols=range(1,9))
        self.dates = np.loadtxt(path, usecols = 0, skiprows=1, delimiter=",", dtype=str)
        self.labels = ["Dates", "Weight", "Chest", "Belly", "Under", "Left Thigh", "Left Bicep", "Goal Weight", "Blood Sugar"]
        print(len(data))
        if len(data) == 1:
            weight = data[0]
            nips = data[1]
            belly = data[2]
            underboob = data[3]
            lThigh = data[4]
            lBicep = data[5]
            goal = data[6]
            sugar = data[7]
        else:
            weight = data[:,0]
            nips = data[:,1]
            belly = data[:,2]
            underboob = data[:,3]
            lThigh = data[:,4]
            lBicep = data[:,5]
            goal = data[:,6]
            sugar = data[:,7]
        return dict(zip(self.labels, [self.dates.tolist(),weight.tolist(), nips.tolist(), belly.tolist(), underboob.tolist(), lThigh.tolist(), lBicep.tolist(), goal.tolist(), sugar.tolist()]))