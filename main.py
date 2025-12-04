import pandas as pd
from utils import convert_types, printing_info

original_data = 'orders_simple.json'
finish_file = 'orders_clean_[NUMBER_ID].csv'

df = pd.read_json(original_data)

def converting():
    convert_types(df, 'total_amount', str)
    convert_types(df, 'shipping_days', int)
    convert_types(df, 'customer_age', int)
    convert_types(df, 'rating', float)
    df['order_date'] = pd.to_datetime(df['order_date'])


def add_month_col():
    df['order_month'] = df['order_date'].dt.month

def replace_coupon_col():
    no_coupon = df['coupon_used'] == ""
    df.loc[no_coupon, 'coupon_used'] = df.loc[no_coupon, 'coupon_used'].replace("", 'no coupon')


# column total amount handling:
def replace_total_amount():
    df['total_amount'] = df['total_amount'].str.replace('$', '', regex=False)
    convert_types(df, 'total_amount', float)


def clean_html_tags():
    df['items_html'] = df['items_html'].str.replace('<b>', '', regex=False)
    df['items_html'] = df['items_html'].str.replace('<br>', ' ', regex=False)
    df['items_html'] = df['items_html'].str.replace('</b>', '', regex=False)


def add_is_high_value():
    """  !!!!!!!!!  """
    average_amount = df['total_amount'].mean()
    print(average_amount)
    df['high_value_order'] = True if [df['total_amount'] > average_amount] else False
    print(df['high_value_order'].head(20))



def rating_mean():
    """  !!!!!!!!!  """
    df['mean_country_rating'] = df.groupby('country')['rating'].count()
    print(df['mean_country_rating'])


def filtering():
    global df
    df = df.loc[(df['total_amount'] > 1000) & (df['rating'] > 4.5)]


def delivery_status():
    global df
    df = df.assign(delivery_status = ['delayed' if int(i) > 7 else 'on_time' for i in df['shipping_days']])


df.to_csv(finish_file)


if __name__ == '__main__':
    converting()
    add_month_col()
    replace_coupon_col()
    replace_total_amount()
    clean_html_tags()
    add_is_high_value()
    rating_mean()
    filtering()
    delivery_status()

