# Testing Abstractions for Testing of Embedded Control Software

Repository associated to the paper _Comparison of Testing Abstractions for Integration Testing of Embedded Control Software_ submitted to ICSE 2022.
The paper discusses the capacity of different testing setups to show bugs in control software.
It contains an experimental campaign based on the [Crazyflie 2.1](https://store.bitcraze.io/products/crazyflie-2-1).
In this repository you will find all the code used in the paper experiments and the instructions to reproduce the tests.
Moreover are also provided the flight data for each experiment, together with pre-generated pdf files containing the plots.

## Repository Structure:

 * **testing-frameworks/mitl**: directory associated to the Model-In-The-Loop testing setup
 * **testing-frameworks/sitl**: directory associated to the Software-In-The-Loop testing setup
 * **testing-frameworks/hitl**: directory associated to the Hardware-In-The-Loop testing setup
 * **testing-frameworks/pitl**: directory associated to the Process-In-The-Loop testing setup
 * **testing-frameworks/plot**: directory containing the Python plotting class
 * **bugs**: directory containing the patch files that inject the bugs discussed in the paper
 * **firmware**: directory containing the firmware patch file and where to put binaries under test

Each testing setup folder contains:

 * the Python class files specific to each abstraction. An exception is made for the physical model simulator: the one in the **mitl** folder is used at each testing abstraction.
 * a subfolder **flightdata** containing the flight data for each test shown in the paper.
 * a subfolder **pdf** containing the complete plots of the flight data for each test shown in the paper.

## Dependencies

[Python 3](https://www.python.org/downloads/release/python-391/), [openOCD](https://www.openocd.org/), [Renode](https://renode.io/) (setup instructions in the `testing-frameworks/sitl` directory), [gdb](https://www.gnu.org/software/gdb/)

Everything has been tested with: MacOS 11.1 and Linux

## Getting the Right Version of the Crazyflie Firmware 
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

Now you can inspect the changes we made to the firmware with (or by just looking at the text content of the patch files):

> git status

and 

> git diff

## Compile the Code for the Desired Setup 

In a terminal window navigate to the `crazyflie-firmware` repository and then to the directory containing the [application](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/userguides/app_layer/) that implements the autonomous flight performing the step sequence. Do so with the following:

> cd examples/demos/app_steps/

Now you can compile the firmware for the desired testing setup with *one* of the following commands:

> make sitl
> make hitl
> make pitl

## Running the Tests

Instructions on how to run the testing setups are provided in the readme file of the `testing-frameworks` directory.

## How to Plot Test Results 

Detailed instructions are provided in the **plot/** directory but to just display the results from a test use:

> python plot_main.py show path/to/flight-data
