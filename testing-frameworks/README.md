# Running the testing setups

This readme file contains the instructions to run the flight tests.

## Run MitL

> python mitl_main.py

## Run SitL
Follow the setup instructions in **testing-frameworks/sitl/README.md**. This only needs to be performed once.

Compile firmware with dedicated autonomous sequence and macro definition by running `make sitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Place the `cf2.elf` binary and `cf2.map` files in **../firmware/**

From the Renode folder, run `mono output/bin/Release/Renode.exe --disable-xwt --port 4444`, if the port is busy choose another.

From another shell, run `python main_sitl.py <port>` where `<port>` is an optional argument used if the port used by Renode is altered.

## Run HitL

Compile firmware with dedicated autonomous sequence and macro definition by running `make hitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Start OpenOCD from crazyflie-firmware folder

Run `python hitl_main`

## Run PitL
Mount the [Micro-SD card deck](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/userguides/decks/micro-sd-card-deck/) (note the required file system) and Flow deck v2 on a Crazyflie.

Place **testing-levels/testing-frameworks/pitl/config.txt** in the root of the SD card.

Compile firmware with dedicated autonomous sequence and macro definition by running `make pitl` from **crazyflie-firmware/examples/demos/app_steps/**.

Flash the firmware by running `make cload`.

After the test, use `pitl_main.py` to translate logging data from the SD card to the format used for other abstractions.