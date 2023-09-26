import rsgislib.vectorutils.createrasters
from rsgislib import TYPE_32INT

inputVector = 'grid_100m_aea.shp'
inputVectorLyr = 'grid_100m_aea'
inputImage = 'GM_AGS_2020_COLMEX.tif'
outputImage = 'grid_100m.kea'
rsgislib.vectorutils.createrasters.rasterise_vec_lyr(
                              vec_file = inputVector,
                              vec_lyr = inputVectorLyr,
                              input_img = inputImage,
                              output_img = outputImage,
                              datatype = TYPE_32INT,
                              gdalformat = 'KEA',
                              att_column ='id')