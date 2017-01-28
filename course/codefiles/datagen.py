import numpy as np
import pandas as pd


def random_xy(num_points=100):
    return pd.DataFrame({
        'x': np.random.normal(num_points),
        'y': np.random.normal(num_points)
    })


def x_plus_noise(num_points=100, slope=1, randomness=0.1):
    if not (0 <= randomness <= 1):
        raise ValueError('randomness must be between 0 and 1 (inclusive).')
    x = np.random.normal(num_points)
    return pd.DataFrame({
        'x': x,
        'y': slope * x + np.random.normal(scale=randomness, size=num_points)
    })


def data_3d(num_points=100, randomness=0.1):
    data = pd.DataFrame({
        'x': np.random.normal(scale=10, size=num_points),
        'y': np.random.normal(scale=1, size=num_points),
        'z': np.random.normal(scale=randomness, size=num_points)
    })
    return pd.DataFrame(
        (np.dot(_rot_mat_x(), np.dot(_rot_mat_z(), data.values.transpose()))).transpose(),
        columns=['x', 'y', 'z']
    )


def label_data(df, p=0.1):
    """ Labels data as +1 or -1, with probability p of incorrect labeling.
    """
    return ((df['x'] > 0).astype(int) * 2 - 1) * np.power(
        -1,
        np.random.binomial(1, p, df.shape[0])
    )


def _rot_mat_x(theta=np.radians(30)):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])


def _rot_mat_z(theta=np.radians(60)):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

