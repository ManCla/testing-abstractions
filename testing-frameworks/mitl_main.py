import numpy as np
from mitl.Model import cfSim
from mitl.Controller import cfCtrl
from mitl.StateEstimator import cfEKF
import time

# import class for storing
from plot.Plot import Storage 

# macros to inject bugs in controller
initialPos   = False
gyroAxesSwap = False
simUpdate    = False
slowTick     = False

if __name__ == "__main__":
	start_test = time.perf_counter()

	# initialization of  objects
	physics = cfSim()
	reference = "step"
	ctrl = cfCtrl(reference, physics.config, physics.b,\
	              physics.I, physics.m, physics.g,\
	              physics.k, physics.l,
	              slowTickBug=slowTick)
	est  = cfEKF(physics.g, initialPosBug=initialPos,
	                        simUpdateBug=simUpdate,
	                        slowTickBug=slowTick)

	# simulation parameters
	t_init  = 0
	t_final = 10
	t_resolution = 0.001
	noise  = 0 # if non-zero includes measurement noise with given gain
	useKalmanFilter = True  # if true the KF is used for feedback
	quantisation    = False # if false removes quantisation from flow data
	t_curr = t_init
	n_steps = int((t_final-t_init)/t_resolution)

	# storage variables
	t       = np.linspace(t_init,t_final,n_steps)
	u_store = np.zeros((physics.n_inputs, n_steps))
	x_store = np.zeros((physics.n_states, n_steps))
	acc     = np.zeros((3,n_steps)) # inertial measurement
	gyro    = np.zeros((3,n_steps)) # inertial measurement
	pxCount = np.zeros((2,n_steps)) # pixel count measurement
	zrange  = np.zeros((n_steps))   # z ranging measurement
	set_pt  = np.zeros((3,n_steps)) # setpoint in cf
	err_fd  = np.zeros((3,n_steps)) # kalman innovation from flow measurements
	x_est   = np.zeros((9,n_steps)) # state estimated by EKF [pos, vel, eta]

	i = 0 # counter

	# first iteration
	x_store[:,i] = physics.simulate(t_curr, u_store[:,i]) # simulate physics
	i = i+1

	# main loop
	while i<n_steps: 
		t_curr = t[i]
		if not i%500:
			print("simulation at time " + str(t_curr))
		set_pt[:,i] = ctrl.referenceGen(t_curr)               # get reference
		if useKalmanFilter :
			u_store[:,i] = ctrl.ctrlCompute(set_pt[:,i],\
			                                x_est[0:3,i-1],\
			                                x_est[3:6,i-1],\
			                                x_est[6:9,i-1],\
			                                gyro[:,i-1])
		else:
			u_store[:,i] = ctrl.ctrlCompute(set_pt[:,i],\
			                                x_store[0:3,i-1],\
			                                x_store[3:6,i-1],\
			                                physics.quaternionToEuler(x_store[6:10,i-1]),\
			                                gyro[:,i-1])
		x_store[:,i] = physics.simulate(t_curr, u_store[:,i]) # simulate physics
		eta = physics.quaternionToEuler(x_store[6:10,i])

		# store measurements
		acc[:,i]  = physics.readAcc(noise)
		if not(gyroAxesSwap) :
			gyro[:,i] = physics.readGyro(noise)
		else:
			tmp = physics.readGyro(noise)
			gyro[:,i] = [tmp[1],tmp[0],tmp[2]]
		pxCount[:,i] = physics.readPixelcount(noise, quantisation)
		zrange[i] = physics.readZRanging(noise)
		# close loop 
		x_est[:,i], err_fd[:,i]  = est.runEKF(acc[:,i],gyro[:,i],pxCount[:,i],zrange[i])

		i=i+1 # increase counter

	end_test = time.perf_counter()
	print("This test took " + str(end_test-start_test) + " seconds")


	##############################################
	# store data as object attributes of storage #
	##############################################

	storeObj = Storage()
	storeObj.type    = "mitl"
	storeObj.t       = t
	storeObj.x       = x_store
	storeObj.u       = u_store

	# extract states
	storeObj.pos     = x_store[0:3,:]
	storeObj.vel     = x_store[3:6,:]
	storeObj.gyro    = x_store[10:13,:]

	# extract euler angles
	eta = np.zeros((3, n_steps))
	for j in range(0,n_steps):
		eta[:,j] = physics.quaternionToEuler(x_store[6:10,j])
	storeObj.eta     = eta

	# measurements and other cf data
	storeObj.acc     = acc
	storeObj.pxCount = pxCount
	storeObj.set_pt  = set_pt
	storeObj.zrange  = zrange
	storeObj.err_fd  = err_fd
	storeObj.est_pos = x_est[0:3,:]
	storeObj.est_vel = x_est[3:6,:]
	storeObj.est_eta = x_est[6:9,:]

	# save file
	storeObj.save("mitl/flightdata")
