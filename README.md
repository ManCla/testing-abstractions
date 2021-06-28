# testing-levels

Repository to be associated to the paper submission. 
Expected folder structure:
 * mitl
 * sitl
 * hitl
 * pitl
 * plot

Each folter will contain a patch file (https://www.tutorialspoint.com/git/git_patch_operation.htm) to be applied directly to the bitcraze crazyflie-firmware repository and all the files needed to run the tests (e.g. cfsitl.py and main-sitl.py). Moreover the floders will contain the flight data from the tests presented in the paper.

There will be one single implementation of the model of the physics that will be in the mitl folter

The code for storing and plotting of flight results will be unified in scripts in the plotting folder. This will contain also the script to generate the tikz code for the images.
