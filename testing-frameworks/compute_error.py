import os  # for file handling functions
from plot.Plot import Storage

setups = ['mitl','sitl','hitl','pitl']

'''
This script iterates over the different setups (first
loop) and the tests of each loop (second loop). For
each test it loads the traces and computes the
integrated squared error (using the dedicated method
of the storage class).
'''

if __name__ == "__main__":
  for setup in setups:
    directory  = setup+'/flightdata/'
    onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for f in onlyfiles :
      path = directory+f
      data_storage = Storage()
      data_storage.open(path,f,silent=True)
      print(setup+' '+f+' '+str(sum(data_storage.computeControlError())))
