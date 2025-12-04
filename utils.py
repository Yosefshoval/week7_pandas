import pandas as pd


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


def converting(df):
    convert_types(df, 'total_amount', str)
    convert_types(df, 'shipping_days', int)
    convert_types(df, 'customer_age', int)
    convert_types(df, 'rating', float)
    df['order_date'] = pd.to_datetime(df['order_date'])


def add_month_col(df):
    df['order_month'] = df['order_date'].dt.month

def replace_coupon_col(df):
    no_coupon = df['coupon_used'] == ""
    df.loc[no_coupon, 'coupon_used'] = df.loc[no_coupon, 'coupon_used'].replace("", 'no coupon')


def replace_total_amount(df):
    df['total_amount'] = df['total_amount'].str.replace('$', '', regex=False)
    convert_types(df, 'total_amount', float)


def clean_html_tags(df):
    df['items_html'] = df['items_html'].str.replace('<b>', '', regex=False)
    df['items_html'] = df['items_html'].str.replace('<br>', ' ', regex=False)
    df['items_html'] = df['items_html'].str.replace('</b>', '', regex=False)


def add_is_high_value(df):
    average_amount = df['total_amount'].mean()
    df = df.assign(high_value_order = [True if i > average_amount else False for i in df['total_amount']])
    return df


def rating_mean(df):
    df['mean_country_rating'] = df.groupby('country')['rating'].transform('mean')


def filtering(df):
    df = df.loc[(df['total_amount'] > 1000) & (df['rating'] > 4.5)]
    return df


def delivery_status(df):
    df = df.assign(delivery_status = ['delayed' if int(i) > 7 else 'on_time' for i in df['shipping_days']])
    return df

def save_to_csv(df, finish_file):
    df.to_csv(finish_file)
