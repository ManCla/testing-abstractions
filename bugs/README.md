# Bugs

This directory contains the patch files that apply the bugs used to compare the different testing levels.
The bugs are organized according to the 4 categories of issues mentioned in the paper.

## Modelling Assumptions

 * Wrong initialization of estimate of state: https://github.com/bitcraze/crazyflie-firmware/issues/760

## Control Design

 * Covariance hitting the bounds
 * Low sampling rate of zranger can cause oscillations? https://github.com/bitcraze/crazyflie-firmware/issues/473

## Software Implementation

 * Assumed simultaneous update of different variables: state speed and quaternion. **Not detected,flight undisturbed in all the three setups.**
 * Different variable definition or computation
 * Casting bug: https://github.com/bitcraze/crazyflie-firmware/pull/774
 * Use of doubles (shouldn't be supported in STM32): change all floats for doubles in zranger2.c - seems to be handled directly by the compiler that converts them to float :/
 * 

## Physical Process

 * Incorrect mounting of the flowdeck?
 * Handling of slowly varying gyro bias
 * Trying to fly when USB is connected

# Useful bugs
 * *motorRatioDef* different definition of motor ratio in different parts of the firmware. Injected as: motorsGetRatio return percentage instead of absolute
 * 
 * 