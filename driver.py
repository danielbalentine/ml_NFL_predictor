#turns off any warnings
import warnings
warnings.filterwarnings('ignore')

#various modules
import sys
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from lazypredict.Supervised import LazyRegressor
from sklearn import datasets
from sklearn.utils import shuffle
from pytrends.request import TrendReq
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LassoCV
from sklearn.linear_model import OrthogonalMatchingPursuitCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, roc_curve, precision_recall_curve, roc_auc_score
from sklearn.calibration import calibration_curve
sys.path.append("E:\Projects\ML_Project\ml_NFL_predictor\lib")
import NFLDataScraper



def main():
    DataScraper = NFLDataScraper.DataScrape()
    #DataScraper.pullStadiumData()
    #DataScraper.pullGameData()


if __name__ == "__main__":
    main()