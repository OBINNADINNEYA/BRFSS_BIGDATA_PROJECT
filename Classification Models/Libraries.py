import warnings
warnings.filterwarnings("ignore")
# General imports
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib
import matplotlib.pyplot as plt
import statistics
import scipy
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
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Preprocessing
from sklearn.preprocessing import RobustScaler,LabelEncoder, OneHotEncoder


# Imbalanced dataset handling
import imblearn
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as IMBPipeline

from sklearn.compose import make_column_selector as selector
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# Function to print version of libraries
def print_library_versions():
    print('The libraries used for this notebook are:')
    print("Pandas version:", pd.__version__)
    print("Numpy version:", np.__version__)
    print("Seaborn version:", sns.__version__)
    print("Matplotlib version:", matplotlib.__version__)
    print("Scikitlearn version:", sklearn.__version__)
    print("Imblearn version:", imblearn.__version__)
    print("Scipy version:", scipy.__version__)

print_library_versions()





