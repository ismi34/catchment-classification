import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv(r'C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\codes\results\distance.csv')
outpath = Path(r"C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\image")

# Assign colors based on norm_dist ranges
def assign_color(val):
    if val <= 0.25:
        return 'darkgreen'
    elif val <= 0.50:
        return 'lightgreen'
    elif val <= 0.75:
        return 'skyblue'
    else:
        return 'navy'

df["color"] = df["norm_dist"].apply(assign_color)

# Set up plot
fig, ax = plt.subplots(figsize=(20, 8), facecolor='#f7f7f7')

# Plot bars with color
x = df["catchment"]
y = df["norm_dist"]
colors = df["color"]

bars = ax.bar(x, y, width=0.6, color=colors)

# Set labels and styles
ax.set_title('Similarity Comparison of Catchments: Altotting to Others\nBased on Landcover Classes', fontsize=18, fontweight='bold')
ax.set_xlabel("Catchment ID")
ax.set_ylabel("Normalized Distance (similarity Index)")
ax.set_facecolor('white')
ax.set_xticks(range(len(x)))
ax.set_xticklabels(x, rotation=90, fontsize=10)
ax.grid(axis='y', linestyle=':', color='gray')

# Style spines
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1)

# Optional: add legend manually
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='darkgreen', label='0.00–0.25'),
    Patch(facecolor='lightgreen', label='0.25–0.50'),
    Patch(facecolor='skyblue', label='0.50–0.75'),
    Patch(facecolor='navy', label='0.75–1.00')
]
ax.legend(handles=legend_elements, title='Norm Dist Range', loc='upper right')

plt.tight_layout()
plt.savefig(outpath/'classified_normalized_distance.jpg', dpi=300)
plt.show()