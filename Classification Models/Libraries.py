import warnings
warnings.filterwarnings("ignore")


# General imports
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import statistics
from scipy.stats import wilcoxon

# Data splitting and model evaluation
from sklearn.model_selection import (
    train_test_split,
    cross_validate,
    cross_val_predict,
    StratifiedKFold,
    GridSearchCV,
    RandomizedSearchCV
)

# Performance metrics
from sklearn.metrics import (
    make_scorer,
    precision_score,
    recall_score,
    classification_report,
    confusion_matrix,
    make_scorer, 
    recall_score,
    accuracy_score,
    matthews_corrcoef
)

# Model imports
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Preprocessing
from sklearn.preprocessing import RobustScaler,LabelEncoder, OneHotEncoder


# Imbalanced dataset handling
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as IMBPipeline

from sklearn.compose import make_column_selector as selector
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


#Function for getting x import
def get_ximp_feat(x=30):
    """function for getting the x number of importance features
    """
    return list(feature_importances_df['Feature'][:x])