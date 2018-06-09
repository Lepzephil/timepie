import pandas as pd


def apply_decay_function(size_df, id_variable, decay_df):
    '''

    :param size_df:
    :param id_variable:
    :param decay_df:
    :return:
    '''
    df = pd.merge(
        left=size_df,
        right=decay_df,
        on=id_variable
    )
    df['size'] = df['size'] / df['decay_rate']

    size_df = df[[id_variable, 'size']]

    return size_df


def aggregate_sub_slices(sub_slice_df, sub_slice_dict, slice_size):
    '''

    :param sub_slice_df:
    :param sub_slice_dict:
    :param slice_size:
    :return:
    '''
    df = pd.merge(
        left=sub_slice_df,
        right=sub_slice_dict,
        on='sub_slice_id'
    )

    new_sub_slice_size=df.groupby('slice_parent_id')['size'].sum().reset_index()

    slice_size = slice_size[['slice_id']]

    slice_size=pd.merge(
        left=slice_size,
        right=new_sub_slice_size,
        left_on='slice_id',
        right_on='slice_parent_id'
    )

    return slice_size[['slice_id', 'size']]
