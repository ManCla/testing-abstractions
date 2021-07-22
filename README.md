# testing-levels

Repository associated to the paper PAPER TITLE HERE. 

## repository structure:

 * *mitl*: directory associated to the Model-In-The-Loop testing level
 * *sitl*: directory associated to the Software-In-The-Loop testing level
 * *hitl*: directory associated to the Hardware-In-The-Loop testing level
 * *pitl*: directory associated to the Process-In-The-Loop testing level
 * *plot*: directory containing the plotting class
 * *bugs*: directory containing the patch files that inject the bugs discussed in the paper

Each testing level folder contains:

 * a patch file (https://www.tutorialspoint.com/git/git_patch_operation.htm https://www.git-tower.com/learn/git/faq/create-and-apply-patch/) to be applied to the correct version of the bitcraze crazyflie-firmware repository (see below). Exception is made for the mitl testing level that does not execute the firmware, hence no patch file is needed.
 * the class files specific to each testing level. Exception is made for the physical model definition: the one in the mitl folder is used at each testing level.
 * a subfolder flightdata containing the flight data for each test shown in the paper
 * a subfolder pdf containing the more complete plots of the flight data for each test shown in the paper

## Dependancies

Python 3, openOCD

Everything tested with: MacOS 11.1

## Get the correct version of the Crazyflie firmware
Clone the crazyflie-firmware repository with

>> git clone git@github.com:bitcraze/crazyflie-firmware.git

For reproducibility all the experiments in the paper were performed with the version of the firmware at commit (https://github.com/bitcraze/crazyflie-firmware/commit/23e9b80caa9137d2953ae6dce57507fda1b05a8c).
Hence after cloning it is important to checkout to this commit with

>> git checkout 23e9b80

## How to plot test results 

Detailed instructions are provided in the plot directory but to just display the results associated to 

>> python plot_main.py show path/to/flight/data

## run mitl

>> python mitl_main.py

## run sitl

## run hitl

## run pitl