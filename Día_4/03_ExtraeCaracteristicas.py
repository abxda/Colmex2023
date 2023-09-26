from rsgislib import rastergis   

inputImage = 'GM_AGS_2020_COLMEX.tif'  
clumpsImage = 'grid_100m.kea'


bs = []  
bs.append(rastergis.BandAttStats(band=1, min_field='b1Min', max_field='b1Max', mean_field='b1Mean', sum_field='b1Sum', std_dev_field='b1StdDev'))  
bs.append(rastergis.BandAttStats(band=2, min_field='b2Min', max_field='b2Max', mean_field='b2Mean', sum_field='b2Sum', std_dev_field='b2StdDev'))  
bs.append(rastergis.BandAttStats(band=3, min_field='b3Min', max_field='b3Max', mean_field='b3Mean', sum_field='b3Sum', std_dev_field='b3StdDev'))  
bs.append(rastergis.BandAttStats(band=4, min_field='b4Min', max_field='b4Max', mean_field='b4Mean', sum_field='b4Sum', std_dev_field='b4StdDev'))  
bs.append(rastergis.BandAttStats(band=5, min_field='b5Min', max_field='b5Max', mean_field='b5Mean', sum_field='b5Sum', std_dev_field='b5StdDev'))  
bs.append(rastergis.BandAttStats(band=6, min_field='b6Min', max_field='b6Max', mean_field='b6Mean', sum_field='b6Sum', std_dev_field='b6StdDev'))  
bs.append(rastergis.BandAttStats(band=7, min_field='b7Min', max_field='b7Max', mean_field='b7Mean', sum_field='b7Sum', std_dev_field='b7StdDev'))  
bs.append(rastergis.BandAttStats(band=8, min_field='b8Min', max_field='b8Max', mean_field='b8Mean', sum_field='b8Sum', std_dev_field='b8StdDev'))  
bs.append(rastergis.BandAttStats(band=9, min_field='b9Min', max_field='b9Max', mean_field='b9Mean', sum_field='b9Sum', std_dev_field='b9StdDev'))  
bs.append(rastergis.BandAttStats(band=10, min_field='b10Min', max_field='b10Max', mean_field='b10Mean', sum_field='b10Sum', std_dev_field='b10StdDev'))  
bs.append(rastergis.BandAttStats(band=11, min_field='b11Min', max_field='b11Max', mean_field='b11Mean', sum_field='b11Sum', std_dev_field='b11StdDev'))  
bs.append(rastergis.BandAttStats(band=12, min_field='b12Min', max_field='b12Max', mean_field='b12Mean', sum_field='b12Sum', std_dev_field='b12StdDev'))  
   
rastergis.populate_rat_with_stats(inputImage, clumpsImage, bs)