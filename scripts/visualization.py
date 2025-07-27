import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

def bar_plot(x, y, title, xlabel, ylabel, outpath, outfilename):
    outpath = Path(outpath)
    
    fig, ax = plt.subplots(figsize=(20, 8), facecolor='#f7f7f7')  # White background

    ax.bar(x, y, width=0.6, color='steelblue')
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_facecolor('white')


    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=90, fontsize=10)

    # Dotted grid line
    ax.grid(axis='y', linestyle=':', color='gray')

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1)

    fig.tight_layout()
    fig.savefig(outpath/outfilename, dpi=300)
    plt.show()