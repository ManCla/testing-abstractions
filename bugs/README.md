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
 * Different variable definition or computation - use one where you directly access the IMU data so that difference between sitl and hitl is shown
 * Casting bug: https://github.com/bitcraze/crazyflie-firmware/pull/774
 * Use of doubles (shouldn't be supported in STM32): change all floats for doubles in zranger2.c - seems to be handled directly by the compiler that converts them to float :/
 * Tasks timing
 * when fusing flow data read gyro data from sensor file queue (instead of using the locally updated variable)  

## Physical Process

 * Incorrect mounting of the flowdeck
 * Handling of slowly varying gyro bias
 * Trying to fly when USB is connected

# Useful bugs
 * *motorRatioDef* different definition of motor ratio in different parts of the firmware. Injected as: motorsGetRatio return percentage instead of absolute
 * *initialPos* same as https://github.com/bitcraze/crazyflie-firmware/issues/760
 * *voltageCompCast* reproduction of https://github.com/bitcraze/crazyflie-firmware/pull/774
 * *timingKalman* timing of kalman thread based on rtos tick rather than sensor interrupt
 * *flowDeckdtTiming* flowdeck data dt based microsecond counter, rather than hard-coded
 * *flowGyroData* to compensate angular rotation in optical flow, use gyro data from another queue rather than the local variable in estimator kalman



 