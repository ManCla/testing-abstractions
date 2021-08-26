# Running the testing setups

This readme file contains the instructions to run the flight tests.
Each test flight you run will generate test data that are stored in the associated `flightdata` subdirectory in a file named after the time the test was performed.
Show plots for the data with:

> python plot_main.py show path/to/flight-data

Substitute `show` with `pdf` if you want instead to generate a pdf file with the plots (latex has to be installed and it will take some time).

## Run MitL

Simply navigate to this folder from a terminal window and run:

> python mitl_main.py

## Run SitL
Follow the setup instructions in `testing-frameworks/sitl/README.md`. This only needs to be performed once.

Compile firmware with dedicated autonomous sequence and macro definition by running `make sitl` from a terminal window in `crazyflie-firmware/examples/demos/app_steps/`.

Place the `cf2.elf` binary and `cf2.map` files in `../firmware/`

From the Renode folder, run `mono output/bin/Release/Renode.exe --disable-xwt --port 4444`, if the port is busy choose another.

From another shell, run `python main_sitl.py <port>` where `<port>` is an optional argument used if the port used by Renode is altered.

## Run HitL

Compile firmware with dedicated autonomous sequence and macro definition by running from `crazyflie-firmware/examples/demos/app_steps/` 

> make hitl

Once done, copy the `cf2.map` file in the `../firmware` directory.
Connect your computer to the drone using the [ST-Link](https://www.st.com/en/development-tools/st-link-v2.html) and the [debug adapter](https://store.bitcraze.io/products/debug-adapter).
Make shure the [flowdeck](https://store.bitcraze.io/products/flow-deck-v2) is mounted on the drone.
Flash the firmware to the target using the ST-Link with the command:

> make flash

Start OpenOCD in another terminal window from the crazyflie-firmware folder with:

> make opneocd

Once OpenOCD is connected to the hardware from a terminal window in this directory run:

> python hitl_main

The test should start and time updated should be displayed. If nothing appears it could be that the firmware is not hitting the braekpoint, find instructions on how to fix this in the file `testing-frameworks/getadresses/Adresses.py`.

## Run PitL
Mount the [Micro-SD card deck](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/userguides/decks/micro-sd-card-deck/) (note the required file system) and Flow deck v2 on a Crazyflie.

Place **testing-levels/testing-frameworks/pitl/config.txt** in the root of the SD card.

Compile firmware with dedicated autonomous sequence and macro definition by running `make pitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Flash the firmware with a crazyradio by running `make cload` or `make flash` if you have the St-Link and the hardware is connected.
**BE CAREFUL** as soon as the firmware is flashed and the drone boots it will take off!! make sure you are at proper distance from it. **TPI:** old it in your hand to prevent the sensors calibration and that it takes off immediately, then turn it off and start it after placing it in an adequate starting point.

After the test, copy the flight data from the SD card into the `flightdata`  directory. Run:

> pitl_main.py file-name 

to translate the logged data from the SD card to the format used by the plotting script.
Plot the data from the output file like for the other testing setups.
