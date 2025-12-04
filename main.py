import pandas as pd
import utils as ut

original_data = 'orders_simple.json'
finish_file = 'orders_clean_[NUMBER_ID].csv'

df = pd.read_json(original_data)


def run_all():
    global df
    ut.converting(df)
    ut.add_month_col(df)
    ut.replace_coupon_col(df)
    ut.replace_total_amount(df)
    ut.clean_html_tags(df)
    df = ut.add_is_high_value(df)
    ut.rating_mean(df)
    df = ut.filtering(df)
    df = ut.delivery_status(df)
    ut.save_to_csv(df, finish_file)


if __name__ == '__main__':
    run_all()