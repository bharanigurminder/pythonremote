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


def listdir_fullpath(d,format):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith(format)]

def get_raster(imd_extent,list_per,arr_imd_data,arr_per_data,interval,output_path,suffix,x_extent,y_extent):
    #interval = 4
    #count_imd = len(list_data)
    count_start = 0
    count_end = interval
    count_per = 0
    for x in list_per:
        if count_start > 365:
            break

        print count_start,count_end
        arcpy.AddMessage(str(arr_per_data.shape)+" x_extent ==="+str(x_extent)+" y_extent ==="+str(y_extent)+" count_start ==="+str(count_start)+" count_end ==="+str(count_end))
        imd_mean = arr_imd_data[count_start:count_end].mean(axis=0)
        per_mean= arr_per_data[count_start:count_end,x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1].mean(axis=0)
        #per_mean = per_filter[per_filter==np.nan]
        #testing = imd_mean/per_mean

        """
        out_ras_imd = arcpy.NumPyArrayToRaster(imd_mean,arcpy.Point(60.0, 3.0),0.25,0.25,value_to_nodata=np.nan)
        outfile_imd ="D:\\BiasCorrection\\OutputRaster\\Mean\\IMD\\2014V2\\"+str(count_start)+".img"
        out_ras_imd .save(outfile_imd)
        arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))


        out_ras_imd = arcpy.NumPyArrayToRaster(per_mean,arcpy.Point(60.0, 3.0),0.25,0.25,value_to_nodata=np.nan)
        outfile_imd ="D:\\BiasCorrection\\OutputRaster\\Mean\\Persian\\2014V2\\"+str(count_start)+".img"
        out_ras_imd .save(outfile_imd)
        arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))


        out_ras_imd = arcpy.NumPyArrayToRaster(testing,arcpy.Point(60.0, 3.0),0.25,0.25,value_to_nodata=0)
        outfile_imd ="D:/BiasCorrection/OutputRaster/Mean/Division/Division_"+str(count_start)+".img"
        out_ras_imd .save(outfile_imd)
        arcpy.DefineProjection_management(outfile_imd, arcpy.SpatialReference(4326))
        """

        for y in range(interval):
            print "count per ===",count_per

            if count_per >= 365:
                break
            per_day = arcpy.RasterToNumPyArray(list_per[count_per])
            bias_corrected = per_day[x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1] * (imd_mean/per_mean)

            #for taking care of underestimation
            ind = per_day[x_extent[0]:x_extent[1]+1,y_extent[0]:y_extent[1]+1]  == 0
            arr_imd_data_ind = arr_imd_data[count_per]
            bias_corrected[ind] = arr_imd_data_ind[ind]

            out_ras_per = arcpy.NumPyArrayToRaster(bias_corrected,arcpy.Point(imd_extent[0],imd_extent[1],imd_extent[2],imd_extent[3]),0.25,0.25,value_to_nodata=np.nan)
            file_name = os.path.basename(list_per[count_per])
            out_path_final = output_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+".img"

            #outfile_per =r"D:\BiasCorrection\OutputRaster\ReultsDisplay\2014_Persiann_vs_IMD_statoin_interpolated_4DayV2/BiasCorrected_"+os.path.basename(list_per[count_per])
            out_ras_per.save(out_path_final)
            arcpy.DefineProjection_management(out_path_final, arcpy.SpatialReference(4326))
            print list_per[count_per]," is corrected"
            count_per+=1
        print "start ===",count_start
        print len(list_per),"=== list_per len"
        print interval,"=== interval"

        print "end ===",count_end
        count_start+=interval
        count_end+=interval


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

suffix = arcpy.GetParameterAsText(4)
interval = arcpy.GetParameterAsText(5)
output_path = arcpy.GetParameterAsText(6)

raster_big_cor = get_dataframe(list_per[0])
raster_small_cor= get_dataframe(list_imd[0])


x_extent = get_index(raster_big_cor[1],raster_small_cor[1])
y_extent = get_index(raster_big_cor[0],raster_small_cor[0])


get_raster(imd_extent,list_per,arr_imd,arr_per,int(interval),output_path,suffix,x_extent,y_extent)
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
