
import pandas as pd 
import numpy as np


modeldf2019 = pd.read_csv('mydata/MMSA2019_train.csv')
modeldf2021 = pd.read_csv('mydata/MMSA2021_train.csv')

#pd.set_option('display.max_columns', None)

pd.set_option('display.max_info_columns', 1000)
pd.set_option('display.max_info_rows', 1000000)



### Data Cleaning and Merging 

#Any variable with value counts below 15 with be turned to a categorical nominal datatype:
# Convert 'col1' from float to categorical
for col in modeldf2019.columns:
    if len(modeldf2019[col].value_counts()) < 15:
        modeldf2019[col] = modeldf2019[col].astype('category')
        
for col in modeldf2021.columns:
    if len(modeldf2021[col].value_counts()) < 15:
        modeldf2021[col] = modeldf2021[col].astype('category')
               


#modeldf2019.info()

#modeldf2021.info()


##Extract state from MMSANAME
def get_state(col):
    return col.split(',')[1]

modeldf2019['STATE'] = modeldf2019['MMSANAME'].apply(get_state)
modeldf2021['STATE'] = modeldf2021['MMSANAME'].apply(get_state)

#Columns of interest:
columns = ['FRNCHDA_','POTADA1_', 'FRUTDA2_', 'FTJUDA2_', 'VEGEDA2_', 'GRENDA1_', 
                '_FRUTSU1', '_VEGESU1', '_HLTHPLN','PRIMINSR', '_RACE', 'MEDCOST1', 'MARITAL', '_EDUCAG', 
                'RENTHOM1', 'EMPLOY1', 'CHILDREN', '_INCOMG1', '_TOTINDA', 'CHCOCNCR', 'SMOKE100', 
                'SMOKDAY2', 'USENOW3','_SMOKER3', '_RFSMOK3','_RFBING5', 'DIABETE4', 
                'CHCOCNCR', '_MICHD', '_RFHYPE6', '_RFCHOL3', 'ADDEPEV3', 'DECIDE', '_AGEG5YR', 
                'WTKG3', '_BMI5', '_BMI5CAT', '_SEX','STATE','SEQNO','_AGEG5YR']
len(columns)

#Rename Columns in 2019 to Match 2021:
modeldf2019.rename(columns={'_INCOMG':'_INCOMG1','_RFHYPE5':'_RFHYPE6','HLTHPLN1': 'PRIMINSR','MEDCOST':'MEDCOST1',
                  '_RFCHOL2':'_RFCHOL3'},inplace=True)


#Create a _HLTHPLN from PRIMINSR IN 2019 df (- '_HLTHPLN' - Categorical variable for healthcare plan )
modeldf2019['_HLTHPLN'] = modeldf2019['PRIMINSR'].apply(lambda x: 1 if x in [1,2,3,4,5,6,7,8,9] 
                                                        else 2 if x == 88 else 'NA')

#Create a DROCDY3_ from ALCDAY5 by dividing the ALCDAY5 variable by 7 days per week or 30 days per month
def compute_drocdy3_(x):
    # Handle NaN values
    if pd.isna(x):
        return np.nan
    
    x_int = int(str(x).split(".")[0])
    
    if x_int == 888:
        return 0.0
    elif x_int // 100 == 1:
        return (x_int % 100) / 7.0
    elif x_int // 100 == 2:
        return (x_int % 100) / 30.0
    elif x_int in [777, 999]:
        return np.nan
    else:
        return float(x_int)

modeldf2021['DROCDY3_'] = modeldf2019['ALCDAY5'].apply(compute_drocdy3_)

modeldf2019_2 = modeldf2019[columns]
modeldf2021_2 = modeldf2021[columns]


#Merge the two dataframes with columns of interest:
model_df = pd.concat([modeldf2019_2,modeldf2021_2])

model_df.head()

#Lets make a copy of the merged dataframe
processed_features = model_df.copy()

processed_features.info()


# check missing values in train dataset
total = processed_features.isnull().sum().sort_values(ascending=False)
percent = (processed_features.isnull().sum()/processed_features.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data






#Place decimal place in fruit and vegetable columns (as it was implied)
def convert_decimal(x):
    if pd.isna(x):
        return np.nan
    else:
        return x/100
    
cols = ['FRNCHDA_','POTADA1_', 'FRUTDA2_', 'FTJUDA2_', 'VEGEDA2_', 'GRENDA1_', 
                '_FRUTSU1', '_VEGESU1','WTKG3','_BMI5']

#Convert features to appropriate values by placing the decimal place 
for col in cols:
    processed_features[col] = processed_features[col].apply(convert_decimal)


#Drop SMOKDDAY2 and _BMI5



#IDEA Find the average 




#Fruit, 34055 NAs as 'Not asked or missing' 
#processed_features['FRUTSU1'].fillna(777, inplace=True)


#Fruit Juice, 29985 NAs as 'Not asked or missing', 
#processed_features['FTJUDA2_'].fillna(777, inplace=True)


#Vegetables, 27520 NAs as 'Not asked or missing', imputed as 'Don't know/Not Sure', 777
#processed_features['FTJUDA2_'].fillna(777, inplace=True)


#Vegetables, 27520 NAs as 'Not asked or missing', imputed as 'Don't know/Not Sure', 777
#processed_features['FVGREEN1'].fillna(777, inplace=True)
#Other vegetables, 30293 NAs as 'Not asked or missing', imputed as 'Don't know/Not Sure', 777
#processed_features['VEGETAB2'].fillna(777, inplace=True)






#Convert _AGEG5YR,WTKG3,_BMI



model_df.info()

