import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('5kg data (meh).csv')
dg = pd.read_csv('5kg run 5.csv')
dh = pd.read_csv('5kg run 6.csv')
di = pd.read_csv('22lbs run 5.csv')
dj = pd.read_csv('22lbs run 6.csv')
dk = pd.read_csv('22lbs data (meh).csv')

datasets = [
    (df, '5kg Data (meh)'),
    (dg, '5kg Run 5'),
    (dh, '5kg Run 6'),
    (di, '22lbs Run 5'),
    (dj, '22lbs Run 6'),
    (dk, '22lbs Data (meh)')
]


for i, (data, title) in enumerate(datasets):
    plt.figure(figsize=(10, 6))
    
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    
    plt.scatter(x, y, s=15, alpha=0.6, c='black', edgecolors='black', linewidth=0.5)
    plt.title(title, fontsize=16)
    plt.xlabel('Force (ACD)', fontsize=12)
    plt.ylabel('Resistance (Ohms)', fontsize=12)
    plt.tight_layout()
    plt.show()