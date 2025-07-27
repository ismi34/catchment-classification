import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path
import os

df_path = Path(r"C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\codes\results")
shp_path = Path(r"C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\vectors\use_vectors\basins_be_150_250_ff30_150km.shp")

#load the normalized distance df and catchment shape geodatafrmae
df = pd.read_csv(df_path / 'distance.csv')
gdf = gpd.read_file(shp_path)

#based on normalized distance separate the catchments_id
id_25 = [x.split('_')[1] for x in (df[df['norm_dist'] <= 0.25]['catchment'])]
id_75 = [x.split('_')[1] for x in (df[df['norm_dist'] >= 0.75]['catchment'])]
id_40 = [x.split('_')[1] for x in (df[(df['norm_dist'] > 0.25) & (df['norm_dist'] <= 0.50)]['catchment'])]
id_60 = [x.split('_')[1] for x in (df[(df['norm_dist'] > 0.50) & (df['norm_dist'] < 0.75)]['catchment'])]
print(id_25)
print(id_40)
print(id_60)
print(id_75)

print(gdf['HYBAS_ID'])

#now filter out catchments with difference distance and create seperate shapefiles
def filter_and_save(gdf, filter_list, filename):
    gdf['HYBAS_ID'] = gdf['HYBAS_ID'].astype(str)
    filtered = gdf[gdf['HYBAS_ID'].isin(filter_list)]
    filtered.to_file(filename)
    
shp_outpath = Path(r"C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\vectors\use_vectors")
filter_and_save(gdf, id_25, shp_outpath/'distance_0_25.shp')
filter_and_save(gdf, id_40, shp_outpath/'distance_25_50.shp')
filter_and_save(gdf, id_60, shp_outpath/'distance_50_75.shp')
filter_and_save(gdf, id_75, shp_outpath/'distance_75_100.shp')
