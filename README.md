# testing-levels

Repository associated to the paper PAPER TITLE HERE. 

## Repository Structure:

 * **mitl**: directory associated to the Model-In-The-Loop testing level
 * **sitl**: directory associated to the Software-In-The-Loop testing level
 * **hitl**: directory associated to the Hardware-In-The-Loop testing level
 * **pitl**: directory associated to the Process-In-The-Loop testing level
 * **plot**: directory containing the plotting class
 * **bugs**: directory containing the patch files that inject the bugs discussed in the paper

Each testing level folder contains:

 * a patch file to be applied to the correct version of the bitcraze crazyflie-firmware repository (see below). Exception is made for the mitl testing level that does not execute the firmware, hence no patch file is needed.
 * the class files specific to each testing level. Exception is made for the physical model definition: the one in the mitl folder is used at each testing level.
 * a subfolder flightdata containing the flight data for each test shown in the paper
 * a subfolder pdf containing the more complete plots of the flight data for each test shown in the paper

## Dependancies

Python 3, openOCD, renode

Everything tested with: MacOS 11.1

## Get the Crazyflie Firmware 
Clone the [crazyflie-firmware](https://github.com/bitcraze/crazyflie-firmware) repository with

> git clone git@github.com:bitcraze/crazyflie-firmware.git

For reproducibility all the experiments in the paper were performed with the version of the firmware at commit [23e9b80](https://github.com/bitcraze/crazyflie-firmware/commit/23e9b80caa9137d2953ae6dce57507fda1b05a8c).
Hence after cloning it is important to checkout to this commit with

> git checkout 23e9b80

## How to Plot Test Results 

Detailed instructions are provided in the plot directory but to just display the results associated to 

> python plot_main.py show path/to/flight/data

## Running the tests

### Run mitl

> python mitl_main.py

### Run sitl

Compile firmware with dedicated autonomous sequence and macro definition

Get memory addresses and update cfSitl file

Update .resc file in renode to point to the app elf file

From the renode folder, run 'mono output/bin/Release/Renode.exe --disable-xwt --port 4444'
From another shell, go to sitl-test/environment in the Crazyflie firmware and run 'python main_sitl.py'

### Run hitl

Compile firmware with dedicated autonomous sequence and macro definition

start openocd from crazyflie-firmware repo

start python hitl_main

### Run pitl


