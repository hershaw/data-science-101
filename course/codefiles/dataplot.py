import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_2d(df, x='x', y='y'):
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()


def plot_3d(df, x='x', y='y', z='z'):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[x], df[y], df[z])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.show()


def plot_principal_components(df, x1=0, x2=1):
    plt.figure()
    plt.scatter(df[:, x1], df[:, x2])
    plt.xlabel('P.C. ' + str(x1))
    plt.ylabel('P.C. ' + str(x2))
    plt.show()

