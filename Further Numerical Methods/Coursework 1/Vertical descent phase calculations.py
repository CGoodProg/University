# -*- coding: utf-8 -*-
"""
A file created to read in the data from the first phase of the landers descent
to Mars, and answer to questions posed in part two of the assessed practical 1
sheet.
@author: cg14acu 
Clare Goodwin
14139478
"""

import matplotlib.pyplot as plt

altimeter=open('altimeter_telemetry.dat','r') #opening data file for reading
altimeter_data=altimeter.readlines()

times_alt=[]
height=[] #creating empty lists to read data into
for data in altimeter_data:
    data=data.strip().split()
    times_alt.append(float(data[0]))
    height.append(float(data[1])) 
#adding data to lists

fig=plt.figure(figsize=(8,8))
plt.plot(times_alt,height)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title("Landers Height over Time")
plt.show()
#plot of height against time

times_velocity=[]
velocity_alt=[]

ndata=len(times_alt)
for i in range(2, ndata-1):
    times_velocity.append(times_alt[i])
    velocity=(height[i+1]-height[i-1])/((times_alt[i+1]-times_alt[i-1]))
    velocity_alt.append(abs(velocity))
#using central difference to differentiate height to get velocity

times_acc=[]
acc_alt=[]

ndata=len(times_velocity)
for i in range(2, ndata-1):
    times_acc.append(times_velocity[i])
    acc=(velocity_alt[i+1]-velocity_alt[i-1])/((times_velocity[i+1]-times_velocity[i-1]))
    acc_alt.append((acc))    
#differentiating velocity to get acceleration
    
print('Height of lander when altimeter switched on:', height[0], 'm')
#print first value in height list
print('Velocity when lander hit the floor:', velocity_alt[-1], 'm/s')
#print last value in velocity list

fig=plt.figure(figsize=(8,8))

plt.plot(times_velocity, velocity_alt,'b-')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity During Descent Phase')
plt.show()
#plot of velocity against time

plt.plot(times_acc, acc_alt,'b-')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s/s)')
plt.title('Acceleration During Descent Phase')
plt.show()
#print of acceleration against time    

print('Max acceleration during descent phase: ',min(acc_alt), 'm/s/s')
#print largest value in acceleration list