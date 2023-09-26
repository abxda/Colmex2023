from rsgislib import rastergis 

clumpsImage = 'grid_100m.kea'  
catsimage = 'Etiquetas_1_urbano_2_no_urbano.tif'
outcolsname = 'klass_'  
majcolname = 'klass'  
rastergis.populate_rat_with_cat_proportions(catsimage,clumpsImage,outcolsname,majcolname)