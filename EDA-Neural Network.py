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

### Install tensorflow
!pip install tensorflow

### Check if the dependencies are installed
!pip list