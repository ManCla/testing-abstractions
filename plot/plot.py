import sys
import os
import pickle as pk
import matplotlib.pyplot as plt

# global variable: configuration
# should I remove intermediate files or not
# set to False to generate paper figures
remove_intermediate = True


class Storage:

  def __init__(self, data_location, experiment_name):
    self.data_location = data_location
    self.experiment_name = str(experiment_name)

    with open(self.data_location, 'rb') as f:
      self.data = pk.load(f)
    print('Reading data from file: \033[4m' + self.data_location + '\033[0m')

    # splitting data into specific values
    self.time = self.data.t
    self.tick = self.data.tick
    self.trace_length = len(self.time)

    self.position_x = self.data.pos[0, :]
    self.position_y = self.data.pos[1, :]
    self.position_z = self.data.pos[2, :]
    self.estimated_position_x = self.data.est_pos[0, :]
    self.estimated_position_y = self.data.est_pos[1, :]
    self.estimated_position_z = self.data.est_pos[2, :]
    self.setpoint_position_x = self.data.set_pt[0, :]
    self.setpoint_position_y = self.data.set_pt[1, :]
    self.setpoint_position_z = self.data.set_pt[2, :]

    self.velocity_x = self.data.vel[0, :]
    self.velocity_y = self.data.vel[1, :]
    self.velocity_z = self.data.vel[2, :]
    self.estimated_velocity_x = self.data.est_vel[0, :]
    self.estimated_velocity_y = self.data.est_vel[1, :]
    self.estimated_velocity_z = self.data.est_vel[2, :]

    self.acceleration_x = self.data.acc[0, :]
    self.acceleration_y = self.data.acc[1, :]
    self.acceleration_z = self.data.acc[2, :]

    self.attitude_x = self.data.eta[0, :]
    self.attitude_y = self.data.eta[1, :]
    self.attitude_z = self.data.eta[2, :]
    self.gyro_x = self.data.gyro[0, :]
    self.gyro_y = self.data.gyro[1, :]
    self.gyro_z = self.data.gyro[2, :]

    self.pixel_count_x = self.data.pxCount[0, :]
    self.kalman_error_x = self.data.err_fd[1, :]
    self.pixel_count_y = self.data.pxCount[1, :]
    self.kalman_error_y = self.data.err_fd[2, :]
    self.range_z = self.data.zrange
    self.kalman_error_z = self.data.err_fd[0, :]

    self.control_motor_1 = self.data.u[0, :]
    self.control_motor_2 = self.data.u[1, :]
    self.control_motor_3 = self.data.u[2, :]
    self.control_motor_4 = self.data.u[3, :]

  def save_csv(self, csv_location):

    with open(csv_location, 'w') as f:

      # header for file
      f.write('i, time, tick, ' +
              'position_x, position_y, position_z, ' +
              'estimated_position_x, estimated_position_y, estimated_position_z, ' +
              'setpoint_position_x, setpoint_position_y, setpoint_position_z, ' +
              'velocity_x, velocity_y, velocity_z, ' +
              'estimated_velocity_x, estimated_velocity_y, estimated_velocity_z, ' +
              'acceleration_x, acceleration_y, acceleration_z, ' +
              'attitude_x, attitude_y, attitude_z, ' +
              'gyro_x, gyro_y, gyro_z, ' +
              'pixel_count_x, kalman_error_x, ' +
              'pixel_count_y, kalman_error_y, ' +
              'range_z, kalman_error_z, ' +
              'control_motor_1, control_motor_2, control_motor_3, control_motor_4 \n')

      for i in range(self.trace_length):
        ith_string = str(i) + ", " + \
                     str(self.time[i]) + ", " + \
                     str(self.position_x[i]) + ", " + \
                     str(self.position_y[i]) + ", " + \
                     str(self.position_z[i]) + ", " + \
                     str(self.estimated_position_x[i]) + ", " + \
                     str(self.estimated_position_y[i]) + ", " + \
                     str(self.estimated_position_z[i]) + ", " + \
                     str(self.setpoint_position_x[i]) + ", " + \
                     str(self.setpoint_position_y[i]) + ", " + \
                     str(self.setpoint_position_z[i]) + ", " + \
                     str(self.velocity_x[i]) + ", " + \
                     str(self.velocity_y[i]) + ", " + \
                     str(self.velocity_z[i]) + ", " + \
                     str(self.estimated_velocity_x[i]) + ", " + \
                     str(self.estimated_velocity_y[i]) + ", " + \
                     str(self.estimated_velocity_z[i]) + ", " + \
                     str(self.acceleration_x[i]) + ", " + \
                     str(self.acceleration_y[i]) + ", " + \
                     str(self.acceleration_z[i]) + ", " + \
                     str(self.attitude_x[i]) + ", " + \
                     str(self.attitude_y[i]) + ", " + \
                     str(self.attitude_z[i]) + ", " + \
                     str(self.gyro_x[i]) + ", " + \
                     str(self.gyro_y[i]) + ", " + \
                     str(self.gyro_z[i]) + ", " + \
                     str(self.pixel_count_x[i]) + ", " + \
                     str(self.kalman_error_x[i]) + ", " + \
                     str(self.pixel_count_y[i]) + ", " + \
                     str(self.kalman_error_y[i]) + ", " + \
                     str(self.range_z[i]) + ", " + \
                     str(self.kalman_error_z[i]) + ", " + \
                     str(self.control_motor_1[i]) + ", " + \
                     str(self.control_motor_2[i]) + ", " + \
                     str(self.control_motor_3[i]) + ", " + \
                     str(self.control_motor_4[i]) + "\n"
        f.write(ith_string)

  def save_latex(self, latex_location, csv_location):
    with open(latex_location, 'w') as f:
      f.write(r'\documentclass{article}' + '\n')
      f.write(r'\usepackage[margin=2cm]{geometry}' + '\n')
      f.write(r'\usepackage{tikz, pgfplots}' + '\n')
      f.write(r'\usepgfplotslibrary{groupplots}' + '\n')
      f.write(r'\pgfplotsset{compat=1.17}' + '\n')
      f.write(r'\pagestyle{empty}' + '\n')
      f.write(r'\begin{document}' + '\n')
      f.write(r'\centering' + '\n')
      f.write(r'{\Large\verb|' + self.experiment_name + r'|}' + '\n')
      f.write(r'\resizebox{0.9\textwidth}{!}{%' + '\n')
      f.write(r'\begin{tikzpicture}[font=\small]' + '\n')
      f.write(r'\begin{groupplot}[%' + '\n')
      f.write(r'group style={group size = 2 by 8, vertical sep = 1cm, horizontal sep = 1cm},' + '\n')
      f.write(r'width = 10cm, height = 4cm,' + '\n')
      f.write(r'enlarge x limits = false,' + '\n')
      f.write(r'legend pos = south east,' + '\n')
      f.write(r'title style={yshift=-1.5ex},' + '\n')
      f.write(r'grid style={densely dotted, black!50},' + '\n')
      f.write(r'grid = major]' + '\n')
      f.write(r'\nextgroupplot[title = {Position $x$}, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra thick, black] table[col sep=comma, x index=1, y index=8] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Setpoint $x$}' + '\n')
      f.write(r'\addplot[ultra  thick, blue] table[col sep=comma, x index=1, y index=2] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Position $x$}' + '\n')
      f.write(r'\addplot[ultra  thick, blue, densely dotted] table[col sep=comma, x index=1, y index=5] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Estimated $x$}' + '\n')
      f.write(r'\nextgroupplot[title = {Velocity $x$}]' + '\n')
      f.write(r'\addplot[ultra  thick, blue] table[col sep=comma, x index=1, y index=11] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Velocity $x$}' + '\n')
      f.write(r'\addplot[ultra  thick, blue, densely dotted] table[col sep=comma, x index=1, y index=14] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Estimated velocity $x$}' + '\n')
      f.write(r'\nextgroupplot[title = {Position $y$}]' + '\n')
      f.write(r'\addplot[ultra thick, black] table[col sep=comma, x index=1, y index=9] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Setpoint $y$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black] table[col sep=comma, x index=1, y index=3] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Position $y$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black, densely dotted] table[col sep=comma, x index=1, y index=6] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Estimated $y$}' + '\n')
      f.write(r'\nextgroupplot[title = {Velocity $y$}, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black] table[col sep=comma, x index=1, y index=12] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Velocity $y$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black, densely dotted] table[col sep=comma, x index=1, y index=15] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Estimated velocity $y$}' + '\n')
      f.write(r'\nextgroupplot[title = {Position $z$}]' + '\n')
      f.write(r'\addplot[ultra thick, black] table[col sep=comma, x index=1, y index=10] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Setpoint $z$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=4] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Position $z$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black, densely dotted] table[col sep=comma, x index=1, y index=7] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Estimated $z$}' + '\n')
      f.write(r'\nextgroupplot[title = {Velocity $z$}, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=13] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Velocity $z$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black, densely dotted] table[col sep=comma, x index=1, y index=16] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{Estimated velocity $z$}' + '\n')
      f.write(r'\nextgroupplot[title = {Acceleration $x, y, z$}, legend columns = 3, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra  thick, blue] table[col sep=comma, x index=1, y index=17] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$x$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black] table[col sep=comma, x index=1, y index=18] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$y$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=19] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$z$}' + '\n')
      f.write(r'\nextgroupplot[title = {Attitude $x, y, z$}, legend columns = 3, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra  thick, blue] table[col sep=comma, x index=1, y index=20] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$x$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black] table[col sep=comma, x index=1, y index=21] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$y$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=22] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$z$}' + '\n')
      f.write(r'\nextgroupplot[title = {Gyro $x, y, z$}, legend columns = 3, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra  thick, blue] table[col sep=comma, x index=1, y index=23] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$x$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black] table[col sep=comma, x index=1, y index=24] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$y$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=25] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$z$}' + '\n')
      f.write(r'\nextgroupplot[title = {$z$-range}]' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=30] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$z$-range}' + '\n')
      f.write(r'\nextgroupplot[title = {Pixel count $x,y$}, legend pos = north east, legend columns = 2]' + '\n')
      f.write(r'\addplot[ultra  thick, blue] table[col sep=comma, x index=1, y index=26] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$x$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black] table[col sep=comma, x index=1, y index=28] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$y$}' + '\n')
      f.write(r'\nextgroupplot[title = {Kalman errors $x,y,z$}, legend columns = 3, legend pos = north east]' + '\n')
      f.write(r'\addplot[ultra  thick, blue, densely dotted] table[col sep=comma, x index=1, y index=27] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$x$}' + '\n')
      f.write(r'\addplot[ultra  thick, green!60!black, densely dotted] table[col sep=comma, x index=1, y index=29] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$y$}' + '\n')
      f.write(r'\addplot[ultra  thick, red!80!black] table[col sep=comma, x index=1, y index=31] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$z$}' + '\n')
      f.write(r'\nextgroupplot[title = {Motors control signals $u_1$}]' + '\n')
      f.write(r'\addplot[ultra  thick, black] table[col sep=comma, x index=1, y index=32] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$u_1$}' + '\n')
      f.write(r'\nextgroupplot[title = {Motors control signals $u_2$}]' + '\n')
      f.write(r'\addplot[ultra  thick, black!80] table[col sep=comma, x index=1, y index=33] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$u_2$}' + '\n')
      f.write(r'\nextgroupplot[title = {Motors control signals $u_3$}]' + '\n')
      f.write(r'\addplot[ultra  thick, black!60] table[col sep=comma, x index=1, y index=34] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$u_3$}' + '\n')
      f.write(r'\nextgroupplot[title = {Motors control signals $u_4$}]' + '\n')
      f.write(r'\addplot[ultra  thick, black!40] table[col sep=comma, x index=1, y index=35] {' + csv_location + r'};' + '\n')
      f.write(r'\addlegendentry{$u_4$}' + '\n')
      f.write(r'\end{groupplot}' + '\n')
      f.write(r'\end{tikzpicture}' + '\n')
      f.write(r'}' + '\n')
      f.write(r'\end{document}' + '\n')


if __name__ == "__main__":

  # parsing command line parameters
  if len(sys.argv) != 3 or sys.argv[1] not in ("pdf", "show"):
    print('\033[91mError:\033[0m ' + 'python plot.py <1> <2>')
    print('  <1>: either "pdf" or "show"')
    print('  <2>: absolute or relative path of the experiment file')
    exit()

  command = sys.argv[1]
  file_location = sys.argv[2]
  experiment_name = file_location.split('/')[-1]
  data_storage = Storage(file_location, experiment_name)
  print('* read data with total length: \033[33m' + str(data_storage.trace_length) + '\033[0m')

  if command == "pdf":

    # first save the data to an intermediate csv file
    intermediate_data_file = "data.csv"
    intermediate_latex_file = experiment_name + ".tex"
    data_storage.save_csv(intermediate_data_file)
    print('* saved data to intermediate file: \033[33m' + str(intermediate_data_file) + '\033[0m')

    # now do the plotting
    data_storage.save_latex(intermediate_latex_file, intermediate_data_file)
    print('* saved tex to intermediate file: \033[33m' + str(intermediate_latex_file) + '\033[0m')

    # you want to use lualatex because there could be a lot of data
    os.system("lualatex " + intermediate_latex_file + " &>/dev/null")
    print('* compiled latex plot: \033[33m' + str(experiment_name) + '.pdf\033[0m')

    # then remove intermediate files
    if remove_intermediate:
      try:
        os.remove(intermediate_data_file)
        print('* removed intermediate file: \033[33m' + str(intermediate_data_file) + '\033[0m')
        os.remove(intermediate_latex_file)
        os.remove(experiment_name + ".aux")
        os.remove(experiment_name + ".log")
        print('* removed intermediate file: \033[33m' + str(intermediate_latex_file) + '\033[0m + .aux .log')
      except OSError:
        pass

  if command == "show":

    # plot trajectory in space
    plt.figure('3D trajectory')
    ax = plt.axes(projection="3d", label="uniquelabel")
    ax.plot(data_storage.position_x, data_storage.position_y, data_storage.position_z, 'r', label="position")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    print('* figure 1:\033[33m 3d position\033[0m')

    # now plot all the others
    chosen_size = (20, 7)
    chosen_grid_linewidth = 0.3
    chosen_grid_linestyle = '--'
    chosen_grid_color = 'gray'

    fig, axs = plt.subplots(3, 2, figsize=chosen_size)
    plt.subplots_adjust(wspace=0.2, hspace=1)

    axs[0, 0].title.set_text('Position (x)')
    axs[0, 0].plot(data_storage.time, data_storage.setpoint_position_x, 'k')
    axs[0, 0].plot(data_storage.time, data_storage.position_x, 'b')
    axs[0, 0].plot(data_storage.time, data_storage.estimated_position_x, 'b:')
    axs[0, 0].legend(['setpoint', 'position', 'estimated position'])
    axs[0, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[1, 0].title.set_text('Position (y)')
    axs[1, 0].plot(data_storage.time, data_storage.setpoint_position_y, 'k')
    axs[1, 0].plot(data_storage.time, data_storage.position_y, 'g')
    axs[1, 0].plot(data_storage.time, data_storage.estimated_position_y, 'g:')
    axs[1, 0].legend(['setpoint', 'position', 'estimated position'])
    axs[1, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[2, 0].title.set_text('Position (z)')
    axs[2, 0].plot(data_storage.time, data_storage.setpoint_position_z, 'k')
    axs[2, 0].plot(data_storage.time, data_storage.position_z, 'r')
    axs[2, 0].plot(data_storage.time, data_storage.estimated_position_z, 'r:')
    axs[2, 0].legend(['setpoint', 'position', 'estimated position'])
    axs[2, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[0, 1].title.set_text('Velocity (x)')
    axs[0, 1].plot(data_storage.time, data_storage.velocity_x, 'b')
    axs[0, 1].plot(data_storage.time, data_storage.estimated_velocity_x, 'b:')
    axs[0, 1].legend(['velocity', 'estimated velocity'])
    axs[0, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[1, 1].title.set_text('Velocity (y)')
    axs[1, 1].plot(data_storage.time, data_storage.velocity_y, 'g')
    axs[1, 1].plot(data_storage.time, data_storage.estimated_velocity_y, 'g:')
    axs[1, 1].legend(['velocity', 'estimated velocity'])
    axs[1, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[2, 1].title.set_text('Velocity (z)')
    axs[2, 1].plot(data_storage.time, data_storage.velocity_z, 'r')
    axs[2, 1].plot(data_storage.time, data_storage.estimated_velocity_z, 'r:')
    axs[2, 1].legend(['velocity', 'estimated velocity'])
    axs[2, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)
    print('* figure 2:\033[33m position and velocity (x,y,z)\033[0m')

    fig, axs = plt.subplots(3, 2, figsize=chosen_size)
    plt.subplots_adjust(wspace=0.2, hspace=1)

    axs[0, 0].title.set_text('Acceleration (x,y,z)')
    axs[0, 0].plot(data_storage.time, data_storage.acceleration_x, 'b')
    axs[0, 0].plot(data_storage.time, data_storage.acceleration_y, 'g')
    axs[0, 0].plot(data_storage.time, data_storage.acceleration_z, 'r')
    axs[0, 0].legend(['x', 'y', 'z'])
    axs[0, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[0, 1].title.set_text('Attitude (x,y,z)')
    axs[0, 1].plot(data_storage.time, data_storage.attitude_x, 'b')
    axs[0, 1].plot(data_storage.time, data_storage.attitude_y, 'g')
    axs[0, 1].plot(data_storage.time, data_storage.attitude_z, 'r')
    axs[0, 1].legend(['x', 'y', 'z'])
    axs[0, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[1, 0].title.set_text('Gyro (x,y,z)')
    axs[1, 0].plot(data_storage.time, data_storage.gyro_x, 'b')
    axs[1, 0].plot(data_storage.time, data_storage.gyro_y, 'g')
    axs[1, 0].plot(data_storage.time, data_storage.gyro_z, 'r')
    axs[1, 0].legend(['x', 'y', 'z'])
    axs[1, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[1, 1].title.set_text('z-range')
    axs[1, 1].plot(data_storage.time, data_storage.range_z, 'r')
    axs[1, 1].legend(['z'])
    axs[1, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[2, 0].title.set_text('Pixel count (x,y)')
    axs[2, 0].plot(data_storage.time, data_storage.pixel_count_x, 'b')
    axs[2, 0].plot(data_storage.time, data_storage.pixel_count_y, 'g')
    axs[2, 0].legend(['x', 'y'])
    axs[2, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[2, 1].title.set_text('Kalman errors (x,y,z)')
    axs[2, 1].plot(data_storage.time, data_storage.kalman_error_x, 'b')
    axs[2, 1].plot(data_storage.time, data_storage.kalman_error_y, 'g')
    axs[2, 1].plot(data_storage.time, data_storage.kalman_error_z, 'r')
    axs[2, 1].legend(['x', 'y', 'z'])
    axs[2, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)
    print('* figure 3:\033[33m sensor data and Kalman errors\033[0m')

    fig, axs = plt.subplots(2, 2, figsize=chosen_size)
    plt.subplots_adjust(wspace=0.2, hspace=1)

    axs[0, 0].title.set_text('Motor control signals (u1)')
    axs[0, 0].plot(data_storage.time, data_storage.control_motor_1, 'k')
    axs[0, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[0, 1].title.set_text('Motor control signals (u2)')
    axs[0, 1].plot(data_storage.time, data_storage.control_motor_2, 'dimgray')
    axs[0, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[1, 0].title.set_text('Motor control signals (u3)')
    axs[1, 0].plot(data_storage.time, data_storage.control_motor_3, 'darkgray')
    axs[1, 0].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)

    axs[1, 1].title.set_text('Motor control signals (u4)')
    axs[1, 1].plot(data_storage.time, data_storage.control_motor_4, 'lightgray')
    axs[1, 1].grid(color=chosen_grid_color, linestyle=chosen_grid_linestyle, linewidth=chosen_grid_linewidth)
    print('* figure 4:\033[33m motor control signals (u1,u2,u3,u4)\033[0m')

    plt.show()
