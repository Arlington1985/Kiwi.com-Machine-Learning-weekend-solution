# title           :graph_kiwi.py
# description     :This script is a solution of the task for Machine Learning Weekend event which organized by kiwi.com and take place between dates 27th and 29th of October 2017  
# author          :Rovshan Musayev
# date            :20171001
# version         :1.0
# notes           :Polynomial regression method was used to predict function 
# python_version  :3.5.3



# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import urllib.parse as ps
import requests as rq
import scipy as sp

# Predicted function
def pred_func(z,x):
    if abs(x)>1 and abs(x)<2:
        return None
    else:
        f=sp.poly1d(z)
        return f(x)

# Get JSON raw data from KIWI server        
def get_json_data(x):
  main_api="http://165.227.157.145:8080/api/do_measurement?"
  url=main_api+ps.urlencode({"x":x})
  json_data=rq.get(url).json()
  return json_data
  
  

# Main part
# Trying to predict function
x=[]
y=[]
for i in np.linspace(-100, 100, 1000):
  x.append(i)
  value=get_json_data(i)['data']['y']
  y.append(value)
  # For Debugging purpose. Prints "x"-"y" values to show input and output pairs from API
  print(str(i)+" - "+str(value))
  

x=np.array(x)
y=np.array(y)
# Find function with Polynomial regression method
# Degree was chosen 4, because for example x=10, y=1000(approximately) and it's y=x^4. Also was achived to best result on this value    
z=sp.polyfit(x[abs(x)>=2],y[abs(x)>=2],8)
f=sp.poly1d(z)
print("Predicted function: \n"+str(f))

# Draw predicted function graph with native value
plt.subplot(211)
plt.plot(x, y,'co')
y_p=[pred_func(z,i) for i in x]
plt.plot(x,y_p)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Now draw predicted function graph with extended value 
# to check if function defined correctly or not
plt.subplot(212)
x=[]
y=[]
for i in np.linspace(-200, 200, 2000):
  x.append(i)
  value=get_json_data(i)['data']['y']
  y.append(value)
  # For Debugging purpose. Prints "x"-"y" values to show calculated input and output values 
  print(str(i)+" - "+str(value))
  
x=np.array(x)
y=np.array(y)
y_p=[pred_func(z,i) for i in x]

plt.plot(x, y,'co')
plt.plot(x, y,'b')
plt.plot(x,y_p,'mo')
plt.plot(x,y_p,'r')

# This part is intended to show difference between calculated and API outputs(y). If the number is less it means the predicted function and API matche to each other more     
for index, item in enumerate(y):
  if item!=None and y_p[index]!=None:
    print("y["+str(index)+"]-y_p["+str(index)+"]="+str(y[index])+"-"+str(y_p[index])+"="+str(y[index]-y_p[index]))
  else:
    print("y["+str(index)+"]-y_p["+str(index)+"]="+str(y[index])+"-"+str(y_p[index])+"=None")


plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
