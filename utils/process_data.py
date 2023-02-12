import pandas as pd

import inflection

COUNTRIES = {
    1: 'India',
    14: 'Australia',
    30: 'Brazil',
    37: 'Canada',
    94: 'Indonesia',
    148: 'New Zeland',
    162: 'Philippines',
    166: 'Qatar',
    184: 'Singapure',
    189: 'South Africa',
    191: 'Sri Lanka',
    208: 'Turkey',
    214: 'United Arab Emirates',
    215: 'England',
    216: 'United States of America',
}

COLORS = {
    '3F7E00': 'darkgreen',
    '5BA829': 'green',
    '9ACD32': 'lightgreen',
    'CDD614': 'orange',
    'FFBA00': 'red',
    'CBCBC8': 'darkred',
    'FF7800': 'darkred',
}

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(' ', '')
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def color_name(color_code):
    return COLORS[color_code]

def country_name(country_id):
    return COUNTRIES[country_id]

def process_data(file_path):
    dataframe = pd.read_csv(file_path)
    dataframe.isna().sum()
    dataframe = dataframe.dropna()
    df = rename_columns(dataframe)
    df['cuisines'] = df.loc[:, 'cuisines'].astype(str).apply(lambda x: x.split(',')[0])
    df['country_code'] = df.loc[:, 'country_code'].apply(lambda x: country_name(x))
    df['color_name'] = df.loc[:, 'rating_color'].apply(lambda x: color_name(x))

    df.to_csv('./data/processed.csv')

    return df