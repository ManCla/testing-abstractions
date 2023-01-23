import sys
import os  # for file handling functions
from plot.Plot import Storage

if __name__ == "__main__":
  for setup in ['mitl','sitl','hitl','pitl']:
    directory  = setup+'/flightdata/'
    onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for f in onlyfiles :
      path = directory+f
      data_storage = Storage()
      data_storage.open(path,f,silent=True)
      print(setup+' '+f+' '+str(data_storage.computeControlError()))
