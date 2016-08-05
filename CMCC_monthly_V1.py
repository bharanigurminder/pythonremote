import arcpy
import numpy as np
import os
import ntpath

def get_dataframe(file_name):
    extent_cor = str(arcpy.Describe(file_name).Extent)
    #extent_cor_ul = str(extent_cor.upperLeft)
    extent_cor_arr = extent_cor.split(' ')

    x_cor = float(extent_cor_arr[0])
    y_cor = float(extent_cor_arr[3])

    x_cor_data = []
    y_cor_data = []

    raster_arr = arcpy.RasterToNumPyArray(file_name)

    # range should be the shape[0]
    for x in range(raster_arr.shape[1]):
        x_cor_data.append(x_cor)
        x_cor += 0.25
    for y in range(raster_arr.shape[0]):
        y_cor_data.append(y_cor)
        y_cor -= 0.25

    return x_cor_data,y_cor_data

def get_index(raster_big_cor,raster_small_cor):
    arcpy.AddMessage("raster_big_cor ==="+str(raster_big_cor))
    arcpy.AddMessage("raster_small_cor ==="+str(raster_small_cor))

    index = 0
    return_index = []
    for x in raster_big_cor:
        if x == raster_small_cor[0]:
            return_index.append(index)
        if x == raster_small_cor[len(raster_small_cor)-1]:
            return_index.append(index)
        index+=1
    return return_index


def month_converter(index_number):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months[index_number - 1]


month_days_data =   [[1, 31],
                    [32, 59],
                    [60, 90],
                    [91, 120],
                    [121, 151],
                    [152, 181],
                    [182, 212],
                    [213, 243],
                    [244, 273],
                    [274, 304],
                    [305, 334],
                    [335, 365]]

def listdir_fullpath(d,format):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith(format)]

def get_raster(imd_extent,list_per,list_imd,arr_imd_data,arr_per_data,output_path,suffix,x_extent,y_extent):
    #interval = 4
    #count_imd = len(list_data)
    count_start = 0
    # count_end = interval
    count_per = 0

    # DEFINATION: starting the loop of months 
    for x in range(1,13):
        
		count_start = month_days_data[x-1][0]-1
		count_end = month_days_data[x-1][1]

		arcpy.AddMessage(str(arr_per_data.shape)+" x_extent ==="+str(x_extent)+" y_extent ==="+str(y_extent)+" count_start ==="+str(count_start)+" count_end ==="+str(count_end))
		imd_month = arr_imd_data[count_start:count_end]
		per_month= arr_per_data[count_start:count_end,x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1]
		
		arcpy.AddMessage("Serach count_start===" + str(count_start))
		arcpy.AddMessage("Serach count_end===" + str(count_end))
		
		# DEFINATION: Taking only data above 2 milimeter 
		imd_month_bool = imd_month <= float(threshold_m)
		per_month_bool = per_month <= float(threshold_m)

		imd_month_filter = np.ma.array(imd_month, mask = imd_month_bool)
		per_month_filter = np.ma.array(per_month, mask = per_month_bool)

		# DEFINATION: Mean of IMD and SRE only above 2 milimeter 	
		imd_mean = imd_month_filter.mean(axis = 0)
		per_mean = per_month_filter.mean(axis = 0)

		ratio = imd_mean/per_mean
		
		#per_mean = per_filter[per_filter==np.nan]
		#testing = imd_mean/per_mean

		file_name = os.path.basename(list_per[count_start])       
		# out_ras_imd = arcpy.NumPyArrayToRaster(np.array(imd_mean), arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=0)
		# outfile_imd = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+"_st_mean.img"
		# out_ras_imd .save(outfile_imd)
		# arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))
        
        
		# out_ras_imd = arcpy.NumPyArrayToRaster(np.array(per_mean), arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=0)
		# outfile_imd = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+"_rs_mean.img"
		# out_ras_imd .save(outfile_imd)
		# arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))

		ratio_arr = np.array(ratio)
		# DEFINATION: If threshold above 2 factore set the factor as 2
		# ratio_arr[ratio_arr > float(threshold_f)] = float(threshold_f)
		# ratio_arr[np.isnan(ratio_arr) == True] = 0
		# out_ras_per = arcpy.NumPyArrayToRaster(ratio_arr, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
		# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+"_factor.img"
		# out_ras_per.save(out_path_final)
		# arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))
       
		if  x >= 6 and x <= 9:
			y = x
			count_start = month_days_data[y-1][0]-1
			count_end = month_days_data[y-1][1]
			arr_imd_month = arr_imd_data[count_start:count_end]
			arr_per_month = arr_per_data[count_start:count_end,x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1]
			
			
			arr_percentile = np.percentile(arr_imd_month, 90, axis = 0)

			# out_ras_per = arcpy.NumPyArrayToRaster(arr_percentile, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			# file_name = os.path.basename(list_per[count_start])
			# arcpy.AddMessage(file_name + "=== file_name")
			# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"imd_nienty_percentile_"+suffix+".img"
			# out_ras_per.save(out_path_final)
			# arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))    
			
			# Start above 90 percentile 
			arr_imd_percentile_bool = np.greater(arr_percentile, arr_imd_month)
			arcpy.AddMessage("arr_imd_percentile_bool.shape ===" + str(arr_imd_percentile_bool.shape))
			arcpy.AddMessage("arr_imd_percentile_bool[0][50][50] ===" + str(arr_imd_percentile_bool[0][50][50]))
			
			arr_imd_percentile_filter = np.ma.array(arr_imd_month, mask = arr_imd_percentile_bool, fill_value = -9999)
			arr_imd_percentile_filter_mean = arr_imd_percentile_filter.mean(axis = 0)
			arr_imd_percentile_filter_mean = arr_imd_percentile_filter_mean.filled()
			arr_imd_percentile_filter_mean[arr_imd_percentile_filter_mean < 0] = np.nan
			arr_imd_percentile_filter_mean[arr_imd_percentile_filter_mean > 9999] = np.nan

			# out_ras_per = arcpy.NumPyArrayToRaster(arr_imd_percentile_filter_mean, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			# file_name = os.path.basename(list_per[count_start])
			# arcpy.AddMessage(file_name + "=== file_name")
			# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"imd_mean_above_"+suffix+".img"
			# out_ras_per.save(out_path_final)
			# arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))    
			
			arr_per_percentile_filter = np.ma.array(arr_per_month, mask = arr_imd_percentile_bool, fill_value = -9999)
			arr_per_percentile_filter_mean = arr_per_percentile_filter.mean(axis = 0)
			arr_per_percentile_filter_mean = arr_per_percentile_filter_mean.filled()
			arr_per_percentile_filter_mean[arr_per_percentile_filter_mean < 0] = np.nan
			arr_per_percentile_filter_mean[arr_per_percentile_filter_mean > 9999] = np.nan

			# out_ras_per = arcpy.NumPyArrayToRaster(arr_per_percentile_filter_mean, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			# file_name = os.path.basename(list_per[count_start])
			# arcpy.AddMessage(file_name + "=== file_name")
			# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"per_mean_above_"+suffix+".img"
			# out_ras_per.save(out_path_final)
			# arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))

			arr_ratio_percentile_filter_mean = arr_imd_percentile_filter_mean/arr_per_percentile_filter_mean
			
			arr_per_percentile_filter = arr_per_percentile_filter.filled()
			arr_per_percentile_filter[ arr_per_percentile_filter == -9999] = np.nan

			out_ras_per = arcpy.NumPyArrayToRaster(arr_ratio_percentile_filter_mean, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			file_name = os.path.basename(list_per[count_start])
			arcpy.AddMessage(file_name + "=== file_name")
			out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_ratio_above_"+suffix+".img"
			out_ras_per.save(out_path_final)
			arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))    

			arr_per_percentile_filter_above = arr_per_percentile_filter * arr_ratio_percentile_filter_mean
			# End above 90 percentile 


			# Start below 90 percentile 
			arr_imd_percentile_bool = np.less(arr_percentile, arr_imd_month)
			arr_imd_percentile_filter = np.ma.array(arr_imd_month, mask = arr_imd_percentile_bool, fill_value = -9999)
			arr_imd_percentile_filter_mean = arr_imd_percentile_filter.mean(axis = 0)
			arr_imd_percentile_filter_mean = arr_imd_percentile_filter_mean.filled()
			arr_imd_percentile_filter_mean[arr_imd_percentile_filter_mean < 0] = np.nan
			arr_imd_percentile_filter_mean[arr_imd_percentile_filter_mean > 9999] = np.nan

			# out_ras_per = arcpy.NumPyArrayToRaster(arr_imd_percentile_filter_mean, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			# file_name = os.path.basename(list_per[count_start])
			# arcpy.AddMessage(file_name + "=== file_name")
			# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"imd_mean_below_"+suffix+".img"
			# out_ras_per.save(out_path_final)
			# arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))    


			arr_per_percentile_filter = np.ma.array(arr_per_month, mask = arr_imd_percentile_bool, fill_value = -9999)
			arr_per_percentile_filter_mean = arr_per_percentile_filter.mean(axis = 0)
			arr_per_percentile_filter_mean = arr_per_percentile_filter_mean.filled()
			arr_per_percentile_filter_mean[arr_per_percentile_filter_mean < 0] = np.nan
			arr_per_percentile_filter_mean[arr_per_percentile_filter_mean > 9999] = np.nan

			# out_ras_per = arcpy.NumPyArrayToRaster(arr_ratio_percentile_filter_mean, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			# file_name = os.path.basename(list_per[count_start])
			# arcpy.AddMessage(file_name + "=== file_name")
			# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"per_mean_below_"+suffix+".img"
			# out_ras_per.save(out_path_final)
			# arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))    

			
			arr_ratio_percentile_filter_mean = arr_imd_percentile_filter_mean/arr_per_percentile_filter_mean
			
			arr_per_percentile_filter = arr_per_percentile_filter.filled()
			arr_per_percentile_filter[ arr_per_percentile_filter == -9999] = np.nan

			arr_per_percentile_filter_below = arr_per_percentile_filter * arr_ratio_percentile_filter_mean
			
			arr_per_percentile_filter_above = np.nansum([arr_per_percentile_filter_above,arr_per_percentile_filter_below],axis = 0)
			# End below 90 percentile 

			arr_per_percentile_filter_above[np.isnan(arr_per_percentile_filter_above) == True] = 0

			

			out_ras_per = arcpy.NumPyArrayToRaster(arr_ratio_percentile_filter_mean, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			file_name = os.path.basename(list_per[count_start])
			arcpy.AddMessage(file_name + "=== file_name")
			out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_ratio_below_"+suffix+".img"
			out_ras_per.save(out_path_final)
			arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))   

			
			# file_name = os.path.basename(list_per[count_per])
			arcpy.AddMessage(str(arr_per_percentile_filter_above.shape) + "arr_per_percentile_filter_above.shape")
			# Individual file multiplication 
			# for individual in range(count_start, count_end):
			#     # arcpy.AddMessage(str(individual-count_start) + "=== individual-count_start")
			#     out_ras_per = arcpy.NumPyArrayToRaster(arr_per_percentile_filter_above[individual-count_start],arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			#     file_name = os.path.basename(list_per[individual])
			#     # arcpy.AddMessage(file_name + "=== file_name")
			#     out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+".img"
			#     out_ras_per.save(out_path_final)
			#     arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))  

		

			
			print "start ===",count_start
			print len(list_per),"=== list_per len"
			#print interval,"=== interval"

			print "end ===",count_end
		else: 
			ratio_arr[ratio_arr > float(threshold_f)] = float(threshold_f)
			ratio_arr[np.isnan(ratio_arr) == True] = 0
			out_ras_per = arcpy.NumPyArrayToRaster(ratio_arr, arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
			out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+"_factor.img"
			out_ras_per.save(out_path_final)
			arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))
			     
			for y in range(count_start, count_end):
				print "count per ===",count_per

				arcpy.AddMessage(str(list_per[y]))

				per_day = arcpy.RasterToNumPyArray(list_per[y])
				imd_day = arcpy.RasterToNumPyArray(list_imd[y], nodata_to_value = np.nan)
				imd_day_nan = np.isnan(imd_day) == True

				# DEFINATION: Multiplying the factor only above 2 milimeter of rainfall
				per_day_temp = per_day[x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1]
				per_day_temp_bool = per_day_temp <= float(threshold_m) 

				per_day_temp_filter = np.ma.array(per_day_temp, mask = per_day_temp_bool)

				bias_corrected = per_day_temp_filter * ratio_arr
				bias_corrected = np.array(bias_corrected)
				# bias_corrected = per_day[x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1] * ratio
				bias_corrected[np.isnan(bias_corrected) == True] = 0
				bias_corrected[imd_day_nan] = imd_day[imd_day_nan]  
				#for taking care of underestimation
				# ind = per_day[x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1]  == 0
				# arr_imd_data_ind = arr_imd_data[y]
				# bias_corrected[ind] = arr_imd_data_ind[ind]

				# out_ras_per = arcpy.NumPyArrayToRaster(bias_corrected,arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
				# file_name = os.path.basename(list_per[y])
				# out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+".img"

				#outfile_per =r"D:\BiasCorrection\OutputRaster\ReultsDisplay\2014_Persiann_vs_IMD_statoin_interpolated_4DayV2/BiasCorrected_"+os.path.basename(list_per[y])
				out_ras_per.save(out_path_final)
				arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))
				print list_per[y]," is corrected"
				
				print "start ===",count_start
				print len(list_per),"=== list_per len"
				# print interval,"=== interval"
				
				print "end ===",count_end
			#count_start+=interval
			#count_end+=interval


#main

#arcpy.env.extent = arcpy.Extent(68.0, 8.0,0,0)
imd_path = arcpy.GetParameterAsText(0)#r'D:\BiasCorrection\Raw_Data\PeejushData\IMDExtended\2014'
imd_extension = arcpy.GetParameterAsText(1)
list_imd = listdir_fullpath(imd_path,imd_extension)
arr_imd = np.array([arcpy.RasterToNumPyArray(x,nodata_to_value=np.nan) for x in list_imd])
imd_extent = str(arcpy.Describe(list_imd[0]).Extent).split(' ')

per_path = arcpy.GetParameterAsText(2)#r'D:\BiasCorrection\Raw_Data\PeejushData\PERSIAN_SA_Extended\2014'
per_extension = arcpy.GetParameterAsText(3)
list_per = listdir_fullpath(per_path,per_extension)
arr_per =np.array([arcpy.RasterToNumPyArray(y,nodata_to_value=-np.nan) for y in list_per])
threshold_m = arcpy.GetParameterAsText(4)
threshold_f = arcpy.GetParameterAsText(5)
suffix = arcpy.GetParameterAsText(6)
# interval = arcpy.GetParameterAsText(5)
output_path = arcpy.GetParameterAsText(7)

raster_big_cor = get_dataframe(list_per[0])
raster_small_cor= get_dataframe(list_imd[0])

# matching the extent 
x_extent = get_index(raster_big_cor[1],raster_small_cor[1])
y_extent = get_index(raster_big_cor[0],raster_small_cor[0])


get_raster(imd_extent,list_per,list_imd,arr_imd,arr_per,output_path,suffix,x_extent,y_extent)
print "starting persian"

#temp(list_per,arr_per)

"""
        out_ras_imd = arcpy.NumPyArrayToRaster(imd_mean,arcpy.Point(67.5, 8.0),0.25,0.25,value_to_nodata=0)
        outfile_imd ="D:/BiasCorrection/OutputRaster/Mean/IMD/"+str(count_start)+".img"
        out_ras_imd .save(outfile_imd)
        arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))

        out_ras_imd = arcpy.NumPyArrayToRaster(per_mean,arcpy.Point(67.5, 8.0),0.25,0.25,value_to_nodata=0)
        outfile_imd ="D:/BiasCorrection/OutputRaster/Mean/Persian/"+str(count_start)+".img"
        out_ras_imd .save(outfile_imd)
        arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))

        out_ras_imd = arcpy.NumPyArrayToRaster(testing,arcpy.Point(67.5, 8.0),0.25,0.25,value_to_nodata=0)
        outfile_imd ="D:/BiasCorrection/OutputRaster/Mean/Division/"+str(count_start)+".img"
        out_ras_imd .save(outfile_imd)
        arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))
 """
