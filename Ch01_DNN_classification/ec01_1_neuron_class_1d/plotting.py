"""Module with functions to plot data."""
import matplotlib.pyplot as plt


def plot_data_1d(x, y_gt):
    """Plot 1D data."""
    plt.scatter(x, y_gt, s=20, c="k")
    plt.xlabel("x0", fontsize=24)
    plt.ylabel("y", fontsize=24)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()


def plot_pred_1d(x, y_gt, y_p):
    """Plot 1D data and predictions."""
    plt.scatter(x, y_gt, s=20, c="k", label="ground truth")
    plt.scatter(x, y_p, s=100, c="tab:orange", marker="x", label="predicted")
    plt.legend(fontsize=20)
    plt.xlabel("x0", fontsize=24)
    plt.ylabel("y", fontsize=24)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()
