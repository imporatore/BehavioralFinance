import numpy as np


def earnings_surprises(adj, med_act, med_est, lag_price):
    """

    Args:
        adj: adjustment factor
        med_act: actual earnings per share
        med_est: median earnings forecast in the last # days
        lag_price: lagged price

    Returns:

    """
    return adj * (med_act - med_est) / lag_price

def winsorize(dat, lower_level=0.005, upper_level=0.995, axis=0):
    """

    Args:
        dat:
        lower_level: upper quantile to clip
        upper_level: lower quantile to clip
        axis: 0 for columns, 1 for rows

    Returns:

    """
    lower_bounds = np.quantile(dat, lower_level, axis=axis, keepdims=True)
    upper_bounds = np.quantile(dat, upper_level, axis=axis, keepdims=True)
    return np.clip(dat, lower_bounds, upper_bounds)

def summary(df, columns=None, percentiles=None):
    """

    Args:
        df:
        columns:
        percentiles:

    Returns:

    """
    cols = df.columns if not columns else columns
    summary_percentiles = percentiles if percentiles else []
    summary_names = ['mean', 'std', 'min'] + [str(i) + 'th percentile' for i in summary_percentiles] + ['max']
    summary_funcs = ['mean', 'std', 'min'] + [lambda dat, j=i: np.quantile(
        dat, j * 0.01, axis=0) for i in summary_percentiles] + ['max']
    summary_df = df[cols].agg(summary_funcs)
    summary_df.index = summary_names
    return summary_df


if __name__ == '__main__':
    pass