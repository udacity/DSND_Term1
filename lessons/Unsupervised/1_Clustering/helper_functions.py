import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate Question 1 Data
X, y = make_blobs(n_samples=500, n_features=3, centers=4, random_state=5)

def plot_q1_data():
    fig = plt.figure();
    ax = Axes3D(fig)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2]);


# Generate Question 2 Data
Z, y = make_blobs(n_samples=500, n_features=5, centers=2, random_state=42)

def plot_q2_data():
    fig = plt.figure()
    plt.scatter(Z[:, 0], Z[:, 1]);

# Generate Question 3 Data
T, y = make_blobs(n_samples=500, n_features=5, centers=8, random_state=5)

def plot_q3_data():
    fig = plt.figure();
    ax = Axes3D(fig)
    ax.scatter(T[:, 1], T[:, 3], T[:, 4]);

# Plot data for Question 4
def plot_q4_data():
    fig = plt.figure();
    ax = Axes3D(fig)
    ax.scatter(T[:, 1], T[:, 2], T[:, 3]);
