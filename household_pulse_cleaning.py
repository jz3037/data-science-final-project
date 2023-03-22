import pandas as pd
import os

char_types = [
    'Age', 
    'Sex', 
    'Sex at birth',
    'Gender', 
    'Sexual orientation',
    'Lesbian, Gay, Bisexual and Transgender',
    'Hispanic origin and Race', 
    'Education', 
    'Marital status', 
    'Household size',
    'Presence of children under 18 years old', 
    'Respondent or household member experienced loss of employment income',
    'Respondent or household member experienced loss of employment income in last 4 weeks',
    'Respondent currently employed',
    'Respondent employed in the last 7 days',
    'Household income'
    ]

def split(df, measure, week):
    char_type_series = df.iloc[:,0].astype(str).apply(str.strip)
    indices = (
        char_type_series[char_type_series.isin(char_types)].index.tolist() + 
        [df.index[df.iloc[:,0].astype(str).apply(str.strip)=='$200,000 and above'].values[0]+2]
    )
    dfs_list = []
    for i in range(len(indices)-1):
        start = indices[i]
        end = indices[i+1]
        num_categories = end-start-1
        char_type = df.iloc[start,0].strip()
        if char_type == char_types[1]:  
            char_type = char_types[2] 
        if char_type == char_types[12]:
            char_type = char_types[11] 
        if char_type == char_types[14]:
            char_type = char_types[13]
        tmp_df = pd.DataFrame()
        tmp_df['Characteristic Type'] = [char_type]*2*num_categories
        tmp_df['Categories'] = list(df.iloc[start+1:end,0])*2
        tmp_df['Measure'] = [measure]*num_categories*2
        tmp_df['Measure Number'] = [1]*num_categories + [2]*num_categories 
        tmp_df['Not at all'] = list(df.iloc[start+1:end,1]) + list(df.iloc[start+1:end,6]) 
        tmp_df['Several days'] = list(df.iloc[start+1:end,2]) + list(df.iloc[start+1:end,7]) 
        tmp_df['More than half the days'] = list(df.iloc[start+1:end,3]) + list(df.iloc[start+1:end,8]) 
        tmp_df['Nearly everyday'] = list(df.iloc[start+1:end,4]) + list(df.iloc[start+1:end,9])         
        tmp_df['Did not report'] = list(df.iloc[start+1:end,5]) + list(df.iloc[start+1:end,10])  
        tmp_df['Total'] = tmp_df.iloc[:,4:9].sum(axis='columns')
        total = tmp_df['Total']-tmp_df['Did not report']
        tmp_df['Not at all_normalized'] = tmp_df['Not at all']/total
        tmp_df['Several days_normalized'] = tmp_df['Several days']/total
        tmp_df['More than half the days_normalized'] = tmp_df['More than half the days']/total
        tmp_df['Nearly everyday_normalized'] = tmp_df['Nearly everyday']/total
        tmp_df['Week'] = week
        dfs_list.append(tmp_df)
    return pd.concat(dfs_list, axis=0)

def main(): 
    df_list = []
    dir = '/Users/jamiezhang/Desktop/data_cleaning/data/'
    for week in range(1,55):
        print('Processing Week', str(week))
        if week < 49: 
            anxiety = os.path.join(dir, 'anxiety/health2a_week'+str(week)+'.xlsx') 
            depression = os.path.join(dir, 'depression/health2b_week'+str(week)+'.xlsx')  
        else: 
            anxiety = os.path.join(dir, 'anxiety/health1_week'+str(week)+'.xlsx') 
            depression = os.path.join(dir, 'depression/health2_week'+str(week)+'.xlsx')  
        if (not anxiety.startswith("~") and 
            anxiety.endswith(".xlsx") and 
            not depression.startswith("~") and 
            depression.endswith(".xlsx")
        ):
            anxiety_df = pd.read_excel(anxiety, skiprows=6)
            tmp_anxiety_df = split(anxiety_df,'Anxiety', week)
            depression_df = pd.read_excel(depression, skiprows=6)
            tmp_depression_df = split(depression_df, 'Depression', week)
            tmp_df = pd.concat([tmp_anxiety_df, tmp_depression_df], axis=0)
            df_list.append(tmp_df)
    df = pd.concat(df_list, axis=0)
    df.to_csv(dir + 'cleaned.csv')  

if __name__ == '__main__':
    main()
