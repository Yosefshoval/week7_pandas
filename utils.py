
def convert_types(df, column, to_type):
    df[column] = df[column].astype(to_type)



def printing_info(df):
    print(df.head(10))
    print('rows: ', len(df))
    print('columns: ', len(df.columns))
    print(df.columns)
    print(df.info())
    print(df.isnull().sum())
    print(df.nunique())
    print(df.describe())
