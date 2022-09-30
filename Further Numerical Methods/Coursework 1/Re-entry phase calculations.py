# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:36:27 2018
A file created to read in the data from the first phase of the landers descent
to Mars, and answer to questions posed in part one of the assessed practical 1
sheet.
@author: cg14acu 
Clare Goodwin
14139478
"""
import matplotlib.pyplot as plt

airspd=open('airspeed_sensor_telemetry.dat','r')
airspeed_data=airspd.readlines()
#open data for reading

times_airspd=[]
airspeed=[]
#creating empty lists for data
for data in airspeed_data:
    data=data.strip().split()
    times_airspd.append(float(data[0]))
    airspeed.append(float(data[1]))
#arranging data into the relevent list

print('Initial velocity of lander during re-entry phase:', airspeed[0], 'm/s')
#print first value in velocity list
print('Final velocity of lander during re-entry phase:', airspeed[-1], 'm/s')
#print final value in velocity list 

times_acc=[]
acc_airspd=[]

ndata=len(times_airspd)
for i in range(2, ndata-1):
    times_acc.append(times_airspd[i])
    acc=(airspeed[i+1]-airspeed[i-1])/((times_airspd[i+1]-times_airspd[i-1]))
    acc_airspd.append(abs(acc))
#using central difference to differentiate velocity to get acceleration
print('Max acceleration during re-entry phase: ',max(acc_airspd), 'm/s/s')
#printing largest value in acceleration list
fig=plt.figure(figsize=(8,8))

plt.plot(times_airspd, airspeed,'b-')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity during re-entry phase')
plt.show()
#plot of velocity against time
plt.plot(times_acc, acc_airspd, 'b-')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s/s)')
plt.title('Acceleration during re-entry phase')
plt.show()
#plot of acceleration against time.