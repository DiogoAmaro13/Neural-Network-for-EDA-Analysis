# 0. Import and Install Dependencies
%matplotlib inline
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
import numpy as np

# 0.1 Install tensorflow
!pip install tensorflow

# 0.2 Check if the dependencies are installed
!pip list



# 1. Load and Study Data 

"""find path file"""
cwd = os.getcwd()
file_path = os.path.join(cwd, 'emotions.csv')
file_path
"""."""
