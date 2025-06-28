import pandas as pd
from matplotlib import pyplot as plt


def plot_timeseries(ts: pd.Series, title):
    fig, ax = plt.subplots(1,1, figsize=(8, 6))
    ax.plot(
        ts.index,
        ts.values,
        color="#1a7e2a",
        lw=2,
        solid_capstyle="round",
    )
    ax.spines[["top", 'right']].set_visible(False)
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.grid(axis='y', lw=1, c='grey', alpha=0.3)
    plt.show()
