#!python3
'''
	Simple check for versions of machine/deep learning
	packages installed on system

'''

## Machine Learning
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import sklearn as sl
import scipy as sp
import statistics as stat
import statsmodels as sm
import statsmodels.api as sma
import statsmodels.formula.api as smf

#Deep Learning
import keras as k
import tensorflow as tf
#load pytorch or caffe2 library
#import torch as pt
#import caffe2 as cf2


print("Numpy version = {}".format(np.__version__))
print("Matplotlib.pyplot version = {}".format(mpl.__version__))
print("Pandas version = {}".format(pd.__version__))
print("Sklearn version = {}".format(sl.__version__))
print("scipy version = {}".format(sp.__version__))
#print("statistics version = {}".format(stat.__version__))
print("statsmodels version = {}".format(sm.__version__))
#print("statsmodels.formula.api version = {}".format(smf.__version__))
print("Keras version = {}".format(k.__version__))
print("tensorflow version = {}".format(tf.__version__))
#print("pytorch version = {}".format(pt.__version__))
#print("caffe2 version = {}".format(cf2.__version__))



