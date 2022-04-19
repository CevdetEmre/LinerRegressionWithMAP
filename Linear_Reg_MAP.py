# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:17:51 2022

@author: emrec
"""
import numpy as np
import matplotlib.pyplot as plt


def BuildMatrix(X,M=3):
  """
  This function builds up the Phi matrix using polynomial basis functions
  parameters
  X   :   X input data of shape (N,1) we are using 1-D inputs in this example
  M   :   Number of model parameters. Polynomials of up to M-1 can be modeled
  return
  Phi :   Numpy array of shape (N,M)
  """
  N = X.shape[0]                                                                # input datas dimensions
  BuildMatrix = [np.ones((N,)).reshape(-1,1)]                                   #[Return a new array of given shape , Gives a new shape to an array without changing its data(In 1 dimension, -1 to 1 must be entered.)]
  for degree in range(1,M):                                                     # create array
    BuildMatrix.append(X**degree)                                               #add new element (X^degree)
  BuildMatrix = np.hstack(BuildMatrix)                                          #Stack arrays in column
  return BuildMatrix


class RegressionMAP:
  """
  This class creates a prediction model using the MAP estimate.
  As stated earlier, data and parameter variance are assummed to be
  known and should be passed as standard deviations in during instantiation.
  """
  def __init__(self,sigma_data=.5, sigma_params=.5):
    self.alpha  = np.sqrt(1/sigma_params)
    self.beta   = np.sqrt(1/sigma_data)
    self.w_MAP = None
  def train(self, BuildMatrix,t):
    D= BuildMatrix.shape[1]
    self.w_MAP = np.linalg.inv(BuildMatrix.T @ BuildMatrix + (self.alpha/self.beta)*np.identity(D)) @ BuildMatrix.T @ t#map formula
  def predict(self,BuildMatrix):
    return BuildMatrix @ self.w_MAP




def f(x):
  return np.sin(2*x) + np.cos(x) -2                                              #dataset equation

#Dataset size
N = 100
#Real process data
x = np.linspace(-5,5,1000).reshape(-1,1)
y = f(x)

#Data and parameter (i.e. prior) standard deviations
sigma_data = 0.5
sigma_params = 0.5

#simulate noise in measurements
data_noise = np.random.normal(0, sigma_data, N).reshape(-1,1)

#Generate training data i.e x
X_train = np.random.uniform(-5,5,N).reshape(-1,1)
Y_train = f(X_train) + data_noise

#Preset model size.
# Note: Bayesian approach can be used to find suitable a suitable number
M = 13

#testing data (convert to Phi)
Phi_test = BuildMatrix(x,M)

#Training data i.e. (convert to Phi)
Phi_train = BuildMatrix(X_train,M)

#map
model_map = RegressionMAP()
model_map.train(Phi_train,Y_train)
map_pred = model_map.predict(Phi_test)


plt.figure(figsize=(10,10))
plt.plot(x,y,label="Real process")
plt.plot(X_train,Y_train,'.',label="Training data")
plt.plot(x,map_pred,':',label="Maximum a posteriori prediction")
plt.xlabel("inputs 'x'")
plt.ylabel("outputs 'y'")
plt.legend()
plt.show()


