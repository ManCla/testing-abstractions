import sys
from plot.Plot import Storage

if __name__ == "__main__":

  # parsing command line parameters
  if len(sys.argv) != 2 :
    print('\033[91mError:\033[0m ' + 'python compute_error.py <1> ')
    print('  <1>: absolute or relative path of the experiment file')
    exit()

  file_location = sys.argv[1]
  experiment_name = file_location.split('/')[-1]
  data_storage = Storage()
  data_storage.open(file_location, experiment_name)
  print('* read data with total length: \033[33m' + str(data_storage.trace_length) + '\033[0m')


  print(data_storage.computeControlError())
