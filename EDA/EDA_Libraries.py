import warnings
warnings.filterwarnings("ignore")


#General imports
import us
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib
import matplotlib.pyplot as plt
import statistics
import scipy
from scipy.stats import chi2_contingency
from scipy import stats
import chart_studio.plotly as py
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Function to print version of libraries
def print_library_versions():
    print('The libraries used for this notebook are:')
    print("Pandas version:", pd.__version__)
    print("Numpy version:", np.__version__)
    print("Seaborn version:", sns.__version__)
    print("Matplotlib version:", matplotlib.__version__)
    # For statistics, it's a standard library module, so it doesn't have a version attribute
    print("Scipy version:", scipy.__version__)
    # For Plotly and Chart Studio, their versions can be accessed from the plotly module
    print("Plotly version:", plotly.__version__)

print_library_versions()