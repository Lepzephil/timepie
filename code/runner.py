import calculate

import pandas as pd
import time

recalculate_interval_seconds = 5


def time_decay_slice():
    # read in sublist
    sub_slice_size_df = pd.read_csv('.csv')
    sub_slice_dict_df = pd.read_csv('.csv')
    sub_slice_size_decay_functions = pd.read_csv('.csv')
    slice_size_df = pd.read_csv('.csv')

    sub_slice_size_df = calculate.apply_decay_function(
        size_df=sub_slice_size_df,
        id_variable='sub_slice_id',
        decay_df=sub_slice_size_decay_functions
    )

    slice_size_df = calculate.aggregate_sub_slices(
        sub_slice_df=sub_slice_size_df,
        slice_dict=sub_slice_dict_df
    )

    # save to file
    sub_slice_size_df.to_csv('.csv')
    slice_size_df.to_csv('.csv')


if __name__ == '__main__':
    run_function=True
    while run_function():
        # todo: architect a daemon that will run this
        time_decay_slice()
        # display_time_pie()
        time.sleep(recalculate_interval_seconds)
