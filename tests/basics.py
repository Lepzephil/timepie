import pandas as pd


def initialize_apply_decay_function():
    size_df = pd.DataFrame(
        [[1, 3],
         [2, 4]],
        columns=['sub_slice_id', 'size'])
    id_variable = 'sub_slice_id'
    decay_df = pd.DataFrame(
        [[1, 1.2],
         [2, 1.4]],
        columns=['sub_slice_id','decay_rate'])

    return size_df, id_variable, decay_df

def initialize_aggregate_sub_slices():
    sub_slice_df = pd.DataFrame(
        [[1, 3],
         [2, 4]],
        columns=['sub_slice_id', 'size'])

    sub_slice_dict = pd.DataFrame(
        [[1, 'yoga', 'Yoga', 1],
         [2, 'meditation', 'Meditation', 1]],
        columns=['sub_slice_id', 'name', 'description', 'slice_parent_id'])

    slice_size = pd.DataFrame(
        [[1, 3],
         [2, 4]],
        columns=['slice_id', 'size'])

    return sub_slice_df, sub_slice_dict, slice_size
