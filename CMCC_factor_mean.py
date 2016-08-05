import numpy as np
import os 

def listdir_fullpath_file(d,format):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith(format)]



jan = []
feb = []
mar = []
apr = []
may = []
jun_a = []
jun_b = []
jul_a = []
jul_b = []
aug_a = []
aug_b = []
sep_a = []
sep_b = []
octo = []
nov = []
dec = []
# main
# path = r"C:\Users\g.bharani\Documents\BiasCorrection\CMCC_monthly\Factors_1998_2010"
path = arcpy.GetParameterAsText(0)
extension = arcpy.GetParameterAsText(1)
factor_threshold = arcpy.GetParameterAsText(2)
operation = arcpy.GetParameterAsText(3)
output = arcpy.GetParameterAsText(4)
list_data = listdir_fullpath_file(path, extension)
# output = r"C:\Users\g.bharani\Documents\BiasCorrection\CMCC_monthly\Factors_1998_2010_Mean"

arcpy.AddMessage("lis_data len ===" + str(len(list_data)))
for x in list_data:
	arcpy.AddMessage(str(x))

for x in range(3):
	jan.append(list_data[x*16])
	feb.append(list_data[x*16+1])
	mar.append(list_data[x*16+2])
	apr.append(list_data[x*16+3])
	may.append(list_data[x*16+4])
	jun_a.append(list_data[x*16+5])
	jun_b.append(list_data[x*16+6])
	jul_a.append(list_data[x*16+7])
	jul_b.append(list_data[x*16+8])
	aug_a.append(list_data[x*16+9])
	aug_b.append(list_data[x*16+10])
	sep_a.append(list_data[x*16+11])
	sep_b.append(list_data[x*16+12])
	octo.append(list_data[x*16+13])
	nov.append(list_data[x*16+14])
	dec.append(list_data[x*16+15])

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
jun_a_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jun_a])
jun_b_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jun_b])
jul_a_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jul_a])
jul_b_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in jul_b])
aug_a_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in aug_a])
aug_b_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in aug_b])
sep_a_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in sep_a])
sep_b_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in sep_b])
octo_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in octo])
nov_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in nov])
dec_arr = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=0) for x in dec])

# factor_arr[factor_arr > float(factor_threshold)] = float(factor_threshold)	
if float(factor_threshold) !=0:
	jan_arr[jan_arr > float(factor_threshold)] = float(factor_threshold)
	feb_arr[feb_arr > float(factor_threshold)] = float(factor_threshold)
	mar_arr[mar_arr > float(factor_threshold)] = float(factor_threshold)
	apr_arr[apr_arr > float(factor_threshold)] = float(factor_threshold)
	may_arr[may_arr > float(factor_threshold)] = float(factor_threshold)
	jun_a_arr[jun_a_arr > float(factor_threshold)] = float(factor_threshold)
	jun_b_arr[jun_b_arr > float(factor_threshold)] = float(factor_threshold)
	jul_a_arr[jul_a_arr > float(factor_threshold)] = float(factor_threshold)
	jul_b_arr[jul_b_arr > float(factor_threshold)] = float(factor_threshold)
	aug_a_arr[aug_a_arr > float(factor_threshold)] = float(factor_threshold)
	aug_b_arr[aug_b_arr > float(factor_threshold)] = float(factor_threshold)
	sep_a_arr[sep_a_arr > float(factor_threshold)] = float(factor_threshold)
	sep_b_arr[sep_b_arr > float(factor_threshold)] = float(factor_threshold)
	octo_arr[octo_arr > float(factor_threshold)] = float(factor_threshold)
	nov_arr[nov_arr > float(factor_threshold)] = float(factor_threshold)
	dec_arr[dec_arr > float(factor_threshold)] = float(factor_threshold)

if operation == "MEAN":
	jan_mean = jan_arr.mean(axis = 0) 
	feb_mean = feb_arr.mean(axis = 0) 
	mar_mean = mar_arr.mean(axis = 0) 
	apr_mean = apr_arr.mean(axis = 0) 
	may_mean = may_arr.mean(axis = 0) 
	jun_a_mean = jun_a_arr.mean(axis = 0) 
	jun_b_mean = jun_b_arr.mean(axis = 0) 
	jul_a_mean = jul_a_arr.mean(axis = 0) 
	jul_b_mean = jul_b_arr.mean(axis = 0) 
	aug_a_mean = aug_a_arr.mean(axis = 0) 
	aug_b_mean = aug_b_arr.mean(axis = 0) 
	sep_a_mean = sep_a_arr.mean(axis = 0) 
	sep_b_mean = sep_b_arr.mean(axis = 0) 
	octo_mean = octo_arr.mean(axis = 0) 
	nov_mean = nov_arr.mean(axis = 0) 
	dec_mean = dec_arr.mean(axis = 0) 


	out_ras_per = arcpy.NumPyArrayToRaster(jan_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_01.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(feb_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_02.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(mar_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_03.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(apr_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_04.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(may_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_05.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(jun_a_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_06_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(jun_b_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_06_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))


	out_ras_per = arcpy.NumPyArrayToRaster(jul_a_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_07_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(jul_b_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_07_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(aug_a_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_08_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(aug_b_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_08_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(sep_a_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_10_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(sep_b_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_09_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(octo_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_10.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(nov_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_11.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(dec_mean,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_12.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	
if operation == "MEDIAN":
	jan_mean = np.median(jan_arr, axis = 0) 
	feb_mean = np.median(feb_arr, axis = 0) 
	mar_mean = np.median(mar_arr, axis = 0) 
	apr_mean = np.median(apr_arr, axis = 0) 
	may_mean = np.median(may_arr, axis = 0) 
	jun_a_mean = np.median(jun_a_arr, axis = 0) 
	jun_b_mean = np.median(jun_b_arr, axis = 0) 
	jul_a_mean = np.median(jul_a_arr, axis = 0) 
	jul_b_mean = np.median(jul_b_arr, axis = 0) 
	aug_a_mean = np.median(aug_a_arr, axis = 0) 
	aug_b_mean = np.median(aug_b_arr, axis = 0) 
	sep_a_mean = np.median(sep_a_arr, axis = 0) 
	sep_b_mean = np.median(sep_b_arr, axis = 0) 
	octo_mean = np.median(octo_arr, axis = 0) 
	nov_mean = np.median(nov_arr, axis = 0) 
	dec_mean = np.median(dec_arr, axis = 0) 

	out_ras_per = arcpy.NumPyArrayToRaster(jan_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_01.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(feb_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_02.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(mar_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_03.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(apr_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_04.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(may_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_05.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(jun_a_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_06_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(jun_b_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_06_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))


	out_ras_per = arcpy.NumPyArrayToRaster(jul_a_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_07_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(jul_b_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_07_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(aug_a_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_08_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(aug_b_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_08_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(sep_a_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_10_above.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(sep_b_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_09_below.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(octo_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_10.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(nov_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_11.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))

	out_ras_per = arcpy.NumPyArrayToRaster(dec_median,arcpy.Point(extent_cor_arr[0],extent_cor_arr[1]),cellsize1,cellsize2,value_to_nodata=np.nan)
	outfile_per = output + "\\" + "Long_Term_Factor_12.img" 
	out_ras_per.save(outfile_per)
	arcpy.DefineProjection_management(outfile_per, arcpy.SpatialReference(4326))



