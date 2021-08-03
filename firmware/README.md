# Firmware

Put in this directory the binaries that you want to test.
In both testing levels the _.map_ file is used to retrieve the memory addresses.
In the sitl level the _.elf_ file is the one flashed to the emulated hardware.

## sitl
For sitl testing are needed the _cf2.elf_ file and the _cf2.map_ file.

## hitl
For hitl testing only the _cf2.map_ file is needed. But make sure the harware is flashed with the corresponding firmware. 
