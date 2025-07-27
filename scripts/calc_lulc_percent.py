import numpy as np
import rasterio

def landcover_percentage(raster_path):
    '''Take landuse raster for a catchment as a input and return
        a dictionary with what percentage of each class is present in the catchment'''
        
    with rasterio.open(raster_path) as src:
        metadata = src.meta
        nodata_value = src.nodata
        
        
        array = src.read(1)
        array = array[array != nodata_value] #mask out the array removing nodata values
        
        unique, counts = np.unique(array, return_counts=True)
        total = counts.sum()
        
        percentage = (counts / total) * 100
        result = dict(zip(unique, percentage))
        
        return result
        
    
    
    
    
    
    