# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 07:23:12 2018

@author: john
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]