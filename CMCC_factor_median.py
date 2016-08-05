import numpy as np
import os 

def listdir_fullpath_file(d,format):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith(format)]



jan = []
feb = []
mar = []
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
octo = []
nov = []
dec = []

# path = r"C:\Users\g.bharani\Documents\BiasCorrection\CMCC_monthly\Factors_1998_2010"
# output = r"C:\Users\g.bharani\Documents\BiasCorrection\CMCC_monthly\Factors_1998_2010_Median"
path = arcpy.GetParameterAsText(0)
extension = arcpy.GetParameterAsText(1)
list_data = listdir_fullpath_file(path,extension)
factor_threshold = arcpy.GetParameterAsText(2)
output = arcpy.GetParameterAsText(3)

for x in range(12):
	jan.append(list_data[x*12])
	feb.append(list_data[x*12+1])
	mar.append(list_data[x*12+2])
	apr.append(list_data[x*12+3])
	may.append(list_data[x*12+4])
	jun.append(list_data[x*12+5])
	jul.append(list_data[x*12+6])
	aug.append(list_data[x*12+7])
	sep.append(list_data[x*12+8])
	octo.append(list_data[x*12+9])
	nov.append(list_data[x*12+10])
	dec.append(list_data[x*12+11])

# print jan
# print feb
# print mar
# print apr
# print may
# print jun
# print jul
# print aug
# print sep
# print octo
# print nov
# print dec

extent_cor = str(arcpy.Describe(list_data[0]).Extent)
extent_cor_arr = extent_cor.split(' ')

cellsize1 = arcpy.Raster(list_data[0]).meanCellHeight
cellsize2 = arcpy.Raster(list_data[0]).meanCellWidth

jan_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jan])
feb_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in feb])
mar_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in mar])
apr_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in apr])
may_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in may])
jun_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jun])
jul_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jul])
aug_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in aug])
sep_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in sep])
octo_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in octo])
nov_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in nov])
dec_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in dec])

jan_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
feb_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
mar_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
apr_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
may_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
jun_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
jul_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
aug_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
sep_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
octo_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
nov_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
dec_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)


jan_mean = np.median(jan_arr, axis = 0) 
feb_mean = np.median(feb_arr, axis = 0) 
mar_mean = np.median(mar_arr, axis = 0) 
apr_mean = np.median(apr_arr, axis = 0) 
may_mean = np.median(may_arr, axis = 0) 
jun_mean = np.median(jun_arr, axis = 0) 
jul_mean = np.median(jul_arr, axis = 0) 
aug_mean = np.median(aug_arr, axis = 0) 
sep_mean = np.median(sep_arr, axis = 0) 
octo_mean = np.median(octo_arr, axis = 0) 
nov_mean = np.median(nov_arr, axis = 0) 
dec_mean = np.median(dec_arr, axis = 0) 

out_ras_per = arcpy.NumPyArrayToRaster(jan_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_001.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(feb_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_032.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(mar_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_060.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(apr_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_091.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(may_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_121.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(jun_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_152.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(jul_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_182.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(aug_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_213.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(sep_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_244.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(octo_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_274.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(nov_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_305.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

out_ras_per = arcpy.NumPyArrayToRaster(dec_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
outfile_per = output + "\\" + "TRMM_Factor_1998_2010_335.img" 
out_ras_per.save(outfile_per)
arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))
