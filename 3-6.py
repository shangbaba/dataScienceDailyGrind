import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

#%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style ('darkgrid')

address = 'C:/Users/elvin/Desktop/Python for Data Science Essential Training/Exercise Files/Ch03/03_06/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_name', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg
plt.plot(mpg)

mpg.describe()
