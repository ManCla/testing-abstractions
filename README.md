# Testing Abstractions for Testing of Embedded Control Software

Repository associated to the paper _Comparison of Testing Abstractions for Integration Testing of Embedded Control Software_ submitted to ICSE 2022.

## Repository Structure:

 * **mitl**: directory associated to the Model-In-The-Loop testing setup
 * **sitl**: directory associated to the Software-In-The-Loop testing setup
 * **hitl**: directory associated to the Hardware-In-The-Loop testing setup
 * **pitl**: directory associated to the Process-In-The-Loop testing setup
 * **plot**: directory containing the Python plotting class
 * **bugs**: directory containing the patch files that inject the bugs discussed in the paper
 * **firmware**: directory containing the firmware patch file and where to put binaries under test

Each testing abstraction folder contains:

 * a patch file to be applied to the correct version of the Bitcraze crazyflie-firmware repository (see below). Exception is made for the MitL testing level that does not execute the firmware, hence no patch file is needed.
 * the Python class files specific to each abstraction. An exception is made for the physical model definition: the one in the **mitl** folder is used at each testing abstraction.
 * a subfolder **flightdata** containing the flight data for each test shown in the paper.
 * a subfolder **pdf** containing the more complete plots of the flight data for each test shown in the paper.

## Dependencies

Python 3, openOCD, Renode, gdb

Everything has been tested with: MacOS 11.1 and Linux

## Get the Crazyflie Firmware 
Clone the [crazyflie-firmware](https://github.com/bitcraze/crazyflie-firmware) repository with

> git clone --recursive git@github.com:bitcraze/crazyflie-firmware.git

For reproducibility all the experiments in the paper were performed with the version of the firmware at commit [23e9b80](https://github.com/bitcraze/crazyflie-firmware/commit/23e9b80caa9137d2953ae6dce57507fda1b05a8c).
Hence after cloning it is important to checkout to this commit with

> cd crazyflie-firmware
> git checkout 23e9b80

Copy in the `crazyflie-firmware` directory the `firmware.patch` file that contains our changes to the firmware and apply it with:

> git apply firmware.patch

To inject the desired bug copy in the `crazyflie-firmware` directory the `bugName.patch` file corresponding to the desired bug into the firmware repository and apply it with:

> git apply bugName.patch

Now you can inspect the changes we made to the firmware with

> git status

and 

> git diff

## How to Plot Test Results 

Detailed instructions are provided in the **plot/** directory but to just display the results from a test use:

> python plot_main.py show path/to/flight-data

## Running the tests

Instructions on how to run the testing frameworks are provided in the readme file of the `testing-frameworks` directory.
