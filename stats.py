import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()

data = [i.split(', ') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

mean_alc = df['Alcohol'].mean()
mean_tob = df['Tobacco'].mean()

median_alc = df['Alcohol'].median()
median_tob = df['Tobacco'].median()

mode_alc = stats.mode(df['Alcohol'])
mode_tob = stats.mode(df['Tobacco'])

range_alc = max(df['Alcohol']) - min(df['Alcohol'])
range_tob = max(df['Tobacco']) - min(df['Tobacco'])

std_dev_alc = df['Alcohol'].std()
std_dev_tob = df['Tobacco'].std()

var_alc = df['Alcohol'].var()
var_tob = df['Tobacco'].var()

print "The mean for the Alcohol and Tobacco dataset is {0} and {1} respectively.".format(mean_alc, mean_tob)
print "The median for the Alcohol and Tobacco dataset is {0} and {1} respectively.".format(median_alc, median_tob)
print "The mode for the Alcohol and Tobacco dataset is {0} and {1} respectively.".format(mode_alc, mode_tob)
print "The range for the Alcohol and Tobacco dataset is {0} and {1} respectively.".format(range_alc, range_tob)
print "The standard deviation for the Alcohol and Tobacco dataset is {0} and {1} respectively.".format(std_dev_alc, std_dev_tob)
print "The variance for the Alcohol and Tobacco dataset is {0} and {1} respectively.".format(var_alc, var_tob)




