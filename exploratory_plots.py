import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

dir = '/Users/jamiezhang/Desktop/data_cleaning/data/'
df =  pd.read_csv(os.path.join(dir, 'cleaned.csv'))

def plot(char_type, measure, measure_num, categories, title, x_ax, y_ax, x_ax_label, y_ax_label): 
    # Multiple time-series lines plot
    # reference: https://towardsdatascience.com/8-visualizations-with-python-to-handle-multiple-time-series-data-19b5b2e66dd0
    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(14,8)})

    ax = sns.lineplot(data=df[
        (df['Characteristic Type'].apply(str.strip) == char_type) &
        (df['Measure'].apply(str.strip) == measure) & 
        (df['Measure Number'] == measure_num) & 
        (df['Categories'].apply(str.strip).isin(categories))
        ], x = x_ax, y = y_ax, hue='Categories')
    
    ax.set_title(title)
    plt.xlabel(x_ax_label)
    plt.ylabel(y_ax_label)
    plt.legend(bbox_to_anchor=(1, 1))
    plt.show()

def main(): 
    # Percentage of People Feeling Anxious Nearly Everyday
    # Marital Status
    # Anxiety, Measure 1 
    plot(
        'Marital status', 
        'Anxiety', 
        1, 
        ['Married', 'Widowed','Never married','Divorced/separated'],
        'Change in Percentage of People Feeling Anxious Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Anxious Nearly Everyday'
        )
    
    # Percentage of People Feeling Anxious Not At all
    # Marital Status
    # Anxiety, Measure 1 
    plot(
        'Marital status', 
        'Anxiety', 
        1, 
        ['Married', 'Widowed','Never married','Divorced/separated'],
        'Change in Percentage of People Feeling Anxious Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Anxious Not At All'
        )
    
    # Percentage of People Feeling Depressed Nearly Everyday
    # Marital Status
    # Depression, Measure 1 
    plot(
        'Marital status', 
        'Depression', 
        1, 
        ['Married', 'Widowed','Never married','Divorced/separated'],
        'Change in Percentage of People Feeling Depressed Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Depressed Nearly Everyday'
        )   

    # Percentage of People Feeling Depressed Not At all
    # Marital Status
    # Depression, Measure 1 
    plot(
        'Marital status', 
        'Depression', 
        1, 
        ['Married', 'Widowed','Never married','Divorced/separated'],
        'Change in Percentage of People Feeling Depressed Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Depressed Not At All'
        )

    # Percentage of People Feeling Anxious Nearly Everyday
    # Children 
    # Anxiety, Measure 1 
    plot(
        'Presence of children under 18 years old', 
        'Anxiety', 
        1, 
        ['Children in household', 'No children'],
        'Change in Percentage of People Feeling Anxious Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Anxious Nearly Everyday'
        )
    
    # Percentage of People Feeling Anxious Not At all
    # Children
    # Anxiety, Measure 1 
    plot(
        'Presence of children under 18 years old', 
        'Anxiety', 
        1, 
        ['Children in household', 'No children'],
        'Change in Percentage of People Feeling Anxious Nearly Everyday during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Anxious Not At All'
        ) 
    
    # Percentage of People Feeling Depressed Nearly Everyday
    # Children
    # Depression, Measure 1 
    plot(
        'Presence of children under 18 years old', 
        'Depression', 
        1, 
        ['Children in household', 'No children'],
        'Change in Percentage of People Feeling Depressed Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Depressed Nearly Everyday'
        )
    
    # Percentage of People Feeling Depressed Not At all
    # Children
    # Depression, Measure 1 
    plot(
        'Presence of children under 18 years old', 
        'Depression', 
        1, 
        ['Children in household', 'No children'],
        'Change in Percentage of People Feeling Depressed Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Depressed Not At All'
        )

    # Percentage of People Feeling Anxious Nearly Everyday
    # Sex at birth
    # Anxiety, Measure 1 
    plot(
        'Sex at birth', 
        'Anxiety', 
        1, 
        ['Male', 'Female'],
        'Change in Percentage of People Feeling Anxious Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Anxious Nearly Everyday'
        )
    
    # Percentage of People Feeling Anxious Not At all
    # Sex at birth
    # Anxiety, Measure 1 
    plot(
        'Sex at birth', 
        'Anxiety', 
        1, 
        ['Male', 'Female'],
        'Change in Percentage of People Feeling Anxious Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Anxious Not At All'
        )
    
    # Percentage of People Feeling Depressed Nearly Everyday
    # Sex at birth
    # Depression, Measure 1 
    plot(
        'Sex at birth', 
        'Depression', 
        1, 
        ['Male', 'Female'],
        'Change in Percentage of People Feeling Anxious Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Anxious Nearly Everyday'
        )
    
    # Percentage of People Feeling Depressed Not At all
    # Children
    # Depression, Measure 1 
    plot(
        'Sex at birth', 
        'Depression', 
        1, 
        ['Male', 'Female'],
        'Change in Percentage of People Feeling Anxious Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Anxious Not At All'
        )
    
    # Percentage of People Feeling Anxious Nearly Everyday
    # Household size
    # Anxiety, Measure 1 
    plot(
        'Household size', 
        'Anxiety', 
        1, 
        ['1 person in the household', 
         '2 people in the household',
         '3 people in the household',
         '4 people in the household',
         '5 people in the household',
         '6 people in the household',
         '7 or more people in the household'],
        'Change in Percentage of People Feeling Anxious Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Anxious Nearly Everyday'
        )
    
    # Percentage of People Feeling Anxious Not At all
    # Household size
    # Anxiety, Measure 1 
    plot(
        'Household size', 
        'Anxiety', 
        1, 
        ['1 person in the household', 
         '2 people in the household',
         '3 people in the household',
         '4 people in the household',
         '5 people in the household',
         '6 people in the household',
         '7 or more people in the household'],
        'Change in Percentage of People Feeling Anxious Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Anxious Not At All'
        )
    
    # Percentage of People Feeling Depressed Nearly Everyday
    # Household size
    # Depression, Measure 1 
    plot(
        'Household size', 
        'Depression', 
        1, 
        ['1 person in the household', 
         '2 people in the household',
         '3 people in the household',
         '4 people in the household',
         '5 people in the household',
         '6 people in the household',
         '7 or more people in the household'],
        'Change in Percentage of People Feeling Depressed Nearly Everyday during COVID-19',
        'Week',
        'Nearly everyday_normalized',
        'Week',
        'Percentage of People Feeling Depressed Nearly Everyday'
        )
    
    # Percentage of People Feeling Depressed Not At all
    # Household size
    # Depression, Measure 1 
    plot(
        'Household size', 
        'Depression', 
        1, 
        ['1 person in the household', 
         '2 people in the household',
         '3 people in the household',
         '4 people in the household',
         '5 people in the household',
         '6 people in the household',
         '7 or more people in the household'],
        'Change in Percentage of People Feeling Anxious Not At All during COVID-19',
        'Week',
        'Not at all_normalized',
        'Week',
        'Percentage of People Feeling Anxious Not At All'
        )
    
if __name__=='__main__':
    main()