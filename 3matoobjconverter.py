#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:04:09 2023

@author: Gxiraudon

3d modeling app 3ma to obj converter

HOW TO USE:
    
    1. Find a way to put your 3ma file in a device that can run python
    2. Run this script with the filename as first parameter (takes about 1 sec or less. If it took 5 secs or more let me know and let me see your 3d model!)
    3. output is written to an .obj file next to it
    6. ENJOY!

"""

import json
import sys

filename_3ma = sys.argv[1]

file_3ma = open(filename_3ma)

fjile_3ma = json.loads(file_3ma.read())

fout = open(filename_3ma + ".obj","wt")

vertex_index = 0
prev_vertex_index = vertex_index

forward = 0

meshes = fjile_3ma["meshes"]

mesh_num = len(meshes)

for msh in range(mesh_num):
    
    fout.write("\ng \n")
    preciseFactor = meshes[msh]["preciseFactor"]
    prev_vertex_index = vertex_index
    for vtx in range(0,len(meshes[msh]["_positions"]),3):
        _pos_0 = meshes[msh]["_positions"][vtx]/preciseFactor 
        _pos_1 = meshes[msh]["_positions"][vtx+1]/preciseFactor 
        _pos_2 = (meshes[msh]["_positions"][vtx+2]*-1)/preciseFactor 
        vtx_string = "v "+str(_pos_0)+" "+str(_pos_1)+" "+str(_pos_2)+"\n"
        fout.write(vtx_string)
        vertex_index = vertex_index+1
        
    if msh>0:
        forward = 1
    
    UnivertsList = meshes[msh]["facesUnivertsList"]
    fout.write("\ng name"+str(msh)+" \n")
    for fcx in UnivertsList:
        fout.write("f")
        for fcx_ndx in fcx["u"]:
            fout.write(" "+str(fcx_ndx+1+(forward*prev_vertex_index)))
        fout.write("\n")    

file_3ma.close()
fout.close()
