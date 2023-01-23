import sys
import os  # for file handling functions
from plot.Plot import Storage

if __name__ == "__main__":

  # parsing command line parameters
  if len(sys.argv) != 2 :
    print('\033[91mError:\033[0m ' + 'python compute_error.py <1> ')
    print('  <1>: name of testing setup [mitl,sitl,hitl,pitl]')
    exit()

  setup = sys.argv[1]
  directory  = setup+'/flightdata/'
  onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
  for f in onlyfiles :
    path = directory+f
    data_storage = Storage()
    data_storage.open(path,f)
    # print(f)
    print(data_storage.computeControlError())
