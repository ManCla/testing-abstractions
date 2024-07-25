# Requirements

## Hardware

To run the experiments of the paper you will need the following pieces of hardware:

 * [Bitcraze Crazyflie drone 2.1](https://www.bitcraze.io/products/crazyflie-2-1/)
 * [Bitcraze Flowdeck V2](https://www.bitcraze.io/products/flow-deck-v2/)
 * [Bitcraze SD Deck](https://www.bitcraze.io/products/micro-sd-card-deck/)
 * [Bitcraze Crazyradio 2.0](https://www.bitcraze.io/products/crazyradio-2-0/)
 * [Bitcraze debug adapter](https://www.bitcraze.io/products/debug-adapter-kit/)
 * [ST-Link](https://www.st.com/en/development-tools/st-link-v2.html)

## Software

The code relies on the following pieces of software:

 * [Python3.8](https://www.python.org/downloads/)
 * [openOCD 0.11.0](https://openocd.org)
 * GDB (not necessary to execute the paper experiments but very convenient for debugging)
 * the [custom Renode repository](https://github.com/bitcraze/renode) maintained by Bitcraze 
 * the [custom Renode Infrastructure](https://github.com/bitcraze/renode-infrastructure) repository maintained by Bitcraze (note that this is a submodule of the Renode repository, see the [testing-abstractions/README.md](https://github.com/ManCla/testing-abstractions/tree/main/testing-frameworks/sitl) for more details)

All of the code has been developed and tested on MacOS 11.1 and Linux Fedora.
