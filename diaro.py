#!/usr/bin/python3
"""
    This program reads a Dairo [android diary app] xml "like" file and extracts 
    data for output. It uses the Pythons xml library.
    
    By: Bill Blasingim
    On: 03/26/2019

"""
import os
import string, datetime
import xml.etree.ElementTree as et
FILEOUT = "Diaro.txt"
fo = open(FILEOUT, "w")
fn="DiaroBackup.xml"
full_file=os.path.abspath(os.path.join('data',fn))
tree=et.parse(full_file)
valid=["date", "title", "text"]
root=tree.getroot()
for child in root:
    if child.attrib['name'] != "diaro_entries":
        continue
    for element in child:
        for el in element:
            fld1=el.tag
            fld2=""
            if fld1 in valid:   # Check for valid tags
                if el.text != None:
                    fld2=el.text
                if fld1=="date":
                    fo.write("\n")
                    # Convert Diaro Unix date format
                    dt=int(fld2)
                    dt=datetime.datetime.fromtimestamp(dt/1000.0)
                    fld2=str(dt)[:10]

                fo.write(fld1+": "+fld2+"\n")

fo.close()
