import os
import arcpy
from arcpy import env
from arcpy.sa import *

def add_new_method():
	print "testing this change"
	
def listdir_fullpath(d,format):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith(format)]

#main
in_path = arcpy.GetParameterAsText(0)
shape_file = arcpy.GetParameterAsText(1)
suffix = arcpy.GetParameterAsText(2)
extension = arcpy.GetParameterAsText(3)
out_path = arcpy.GetParameterAsText(4)

arcpy.AddMessage("in_path ==="+in_path)
arcpy.AddMessage("shape_file ==="+shape_file)
arcpy.AddMessage("suffix ==="+suffix)
arcpy.AddMessage("extension ==="+extension)
arcpy.AddMessage("out_path ==="+out_path)

# shell inputs 
# shape_file = r'D:\MaharashtraIDSI\Maharashtra\pune1.shp'
# in_path = r'D:\BiasCorrection\Verify_clip_batch\2001'
# out_path = r'D:\BiasCorrection\Verify_clip_batch\Python_loop'
# suffix = "python_shell"
# extension = ".img"
# arcpy.env.extent = arcpy.Extent(60,3,100,40)


list_data = listdir_fullpath(in_path,extension)
for x in list_data:
    file_name = os.path.basename(x)

    out_path_final = out_path+"\\"+os.path.splitext(file_name)[0]+"_"+suffix+extension
    arcpy.AddMessage(out_path_final)
    arcpy.Clip_management(x,None,out_path_final,shape_file,None,"ClippingGeometry",None)
    #temp = Con(arcpy.Raster(x) == arcpy.Raster(x),arcpy.Raster(x),"D:/BiasCorrection/Fishnet/FishnetNan/fishnetNan.img")
    #temp.save(out_path+"/Extended_"+os.path.basename(x))


