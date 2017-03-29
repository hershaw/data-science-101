import pandas as pd
from matplotlib import pyplot as plt 


def get_titanic():
    return pd.read_csv(
        '/home/vagrant/course/class2/data/titanic.csv',
        index_col=0)


def get_data():
    return pd.read_csv(
        '/home/vagrant/course/class2/data/all_data.csv',
        index_col=0)


def print_analysis(series):
    for nr in range(1, 4):
        
        upper_limit = series.mean() + (nr * series.std())
        lower_limit = series.mean() - (nr * series.std())
        
        in_range = (series < upper_limit) & (series > lower_limit)
        percent_in_range = in_range.sum() / len(series)
        
        print('%0.5f%% of the dataset is under %0.0f SDs from the mean (%0.0f)' %(
                percent_in_range*100, nr, upper_limit))


def plot_standard_deviations(data, label):
    ax = data.hist(bins=40, figsize=(16,4))

    ax.axvspan(data.mean() - data.std(), 
               data.mean() + data.std(), 
               alpha=0.4, 
               color='green')

    ax.axvspan(data.mean() - 2*data.std(), 
               data.mean() + 2*data.std(), 
               alpha=0.3, 
               color='yellow')


    ax.axvspan(data.mean() - 3*data.std(), 
               data.mean() + 3*data.std(), 
               alpha=0.2, 
               color='red')
    
    plt.xlabel(label)
    plt.ylabel('Count')
    plt.ylabel('Number of observations')
 


 