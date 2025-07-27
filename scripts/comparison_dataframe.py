from pathlib import Path
import os
from calc_lulc_percent import landcover_percentage
import pandas as pd
import numpy as np

def create_df(base_catchment, secondary_catchments_dir):
    base_lulc_dict = landcover_percentage(base_catchment)

    items = list(base_lulc_dict.items())
    items.sort(key=lambda item: item[1], reverse=True)
    top5_classes = items[:5]
    top5_class_ids = [cls for cls, _ in top5_classes]
    top5_class_values = [pct for _, pct in top5_classes]

    secondary_catchments_lulc = os.listdir(secondary_catchments_dir)

    rows = []
    for file in secondary_catchments_lulc:
        lulc_raster = os.path.join(secondary_catchments_dir, file)
        lulc_full_dict = landcover_percentage(lulc_raster)

        lulc_filtered_dict = {cls: lulc_full_dict.get(cls, 0.0) for cls in top5_class_ids}
        row = {'catchment': Path(file).stem}
        row.update(lulc_filtered_dict)
        rows.append(row)

    # Fix 1: Set index before transpose
    lulc_df = pd.DataFrame(rows)
    lulc_df = lulc_df.set_index('catchment')
    lulc_df = lulc_df.T

    # Compute std across catchments (columns)
    lulc_df['std'] = lulc_df.std(axis=1)

    # Fix 2: Add base_catchment and weights
    lulc_df['base_catchment'] = top5_class_values
    lulc_df['weight'] = np.array(top5_class_values) * 0.01
    return lulc_df
