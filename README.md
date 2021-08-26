# testing-levels

Repository associated to the paper _Comparison of Testing Abstractions for Integration Testing of Embedded Control Software_. 

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

Python 3, openOCD, Renode

Everything tested with: MacOS 11.1

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

### Run MitL

> python mitl_main.py

### Run SitL
Follow the setup instructions in **testing-frameworks/sitl/README.md**. This only needs to be performed once.

Compile firmware with dedicated autonomous sequence and macro definition by running `make sitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Place the `cf2.elf` binary and `cf2.map` files in **../firmware/**

From the Renode folder, run `mono output/bin/Release/Renode.exe --disable-xwt --port 4444`, if the port is busy choose another.

From another shell, run `python main_sitl.py <port>` where `<port>` is an optional argument used if the port used by Renode is altered.

### Run HitL

Compile firmware with dedicated autonomous sequence and macro definition by running `make hitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Start OpenOCD from crazyflie-firmware folder

Run `python hitl_main`

### Run PitL
Mount the [Micro-SD card deck](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/userguides/decks/micro-sd-card-deck/) (note the required file system) and Flow deck v2 on a Crazyflie.

Place **testing-levels/testing-frameworks/pitl/config.txt** in the root of the SD card.

Compile firmware with dedicated autonomous sequence and macro definition by running `make pitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Flash the firmware by running `make cload`.

After the test, use `pitl_main.py` to translate logging data from the SD card to the format used for other abstractions.
