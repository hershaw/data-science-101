import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_2d(df, x='x', y='y', labels=None):
    plt.figure()
    plt.scatter(df[x], df[y], c=_colors_from_labels(labels))
    plt.xlabel(x)
    plt.ylabel(y)


def plot_3d(df, x='x', y='y', z='z', labels=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[x], df[y], df[z], c=_colors_from_labels(labels))
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)


def plot_principal_components(df, x1=0, x2=1, labels=None):
    plt.figure()
    plt.scatter(df[:, x1], df[:, x2], c=_colors_from_labels(labels))
    plt.xlabel('P.C. ' + str(x1))
    plt.ylabel('P.C. ' + str(x2))


def _colors_from_labels(labels):
    try:
        return labels.map(lambda x: 'r' if x == 0 else 'b' if x == 1 else 'g')
    # raised if labels is None
    except AttributeError:
        return 'b'

