import time
from flyt_python import api
drone = api.navigation(timeout=120000)

time.sleep(3)

print 'taking off'
drone.take_off(5.0)

print 'Executing mission'
drone.position_set(6.5,0,0,relative=True)
time.sleep(1)
drone.position_set(0,6.5,0,relative=True)
time.sleep(1)
drone.position_set(-6.5,0,0,relative=True)
time.sleep(1)
drone.position_set(0,-6.5,0,relative=True)

print 'Landing'
drone.land(async=False)

drone.disconnect()