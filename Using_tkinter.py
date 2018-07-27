# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import font
import  urllib.request
import urllib.parse
import ssl
import simplejson


def clicked():
    # SSLContext to avoid "SSL: CERTIFICATE_VERIFY_FAILED" Error
    ssl._create_default_https_context = ssl._create_unverified_context
    url = input.get()
    try:
        search = urllib.request.urlopen( url )
        json = simplejson.loads(search.read())
    except:
        versionTitle = ""
        version = "Invalid url"
        labelTitle.configure(text=version)
        labelVersion.configure(text="")
        labelLayerTitle.configure(text="")
        labelLayerName.configure(text="")

    layerTitle = ""
    layerName = ""
    version = ""
    versionTitle = ""

    try:
        versionTitle = "Version ArcGIS Server"
        version = str(json["currentVersion"])
        layerTitle = "Layers "

        for layer in json["layers"]:
            layerName = layerName + layer["name"] + "\n"

        labelTitle.configure(text=versionTitle)
        labelVersion.configure(text=version)
        labelLayerTitle.configure(text=layerTitle)
        labelLayerName.configure(text=layerName)

    except:
        versionTitle = ""
        version = "Invalid url"
        labelTitle.configure(text=version)
        labelVersion.configure(text="")
        labelLayerTitle.configure(text="")
        labelLayerName.configure(text="")

tk = Tk()
tk.geometry( "" )

fontBold = font.Font(family="Consolas", size=10, weight="bold")
fontNoBold = font.Font(family="Consolas", size=8)

# frame 1
Frame1 = Frame(tk, borderwidth=2, relief=GROOVE)
Frame1.pack(padx=10, pady=10, side=TOP, expand=1)

tk.title( "Description of map service" )

label = Label( Frame1, text="Rest url of map service : ", justify=LEFT, padx=10, pady=10, font=fontBold )
label.grid( column=0, row=0, sticky="W" )

input = Entry( Frame1, bd = 5, width = 110 )
input.insert( 0, "http://sampleserver6.arcgisonline.com/"
                "arcgis/rest/services/Hurricanes/MapServer?f=json")
input.grid(column=0, row=1, sticky="W", padx=10)

btn = Button( Frame1, text="Submit", command=clicked )
btn.grid( column=1, row=1, sticky="W", padx=10 )

label = Label( Frame1, text="Examples"
               , justify=LEFT, padx=10, pady=10, font=fontBold )
label.grid( column=0, row=2, sticky="W" )

label = Label( Frame1, text="http://sampleserver6.arcgisonline.com/arcgis/rest/services/Hurricanes/MapServer?f=json"
               , justify=LEFT, padx=10, pady=10, font=fontNoBold )
label.grid( column=0, row=3, sticky="W" )

label = Label( Frame1, text="http://sampleserver3.arcgisonline.com/ArcGIS/rest/services/SanFrancisco/311Incidents/MapServer?f=json"
               , justify=LEFT, padx=10, pady=10, font=fontNoBold )
label.grid( column=0, row=4, sticky="W" )

label = Label( Frame1, text="http://sampleserver6.arcgisonline.com/arcgis/rest/services/Military/MapServer?f=json"
               , justify=LEFT, padx=10, pady=10, font=fontNoBold )
label.grid( column=0, row=5, sticky="W" )

label = Label( Frame1, text="http://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer?f=json"
               , justify=LEFT, padx=10, pady=10, font=fontNoBold )
label.grid( column=0, row=6, sticky="W" )

label = Label( Frame1, text="http://sampleserver4.arcgisonline.com/ArcGIS/rest/services/HomelandSecurity/Incident_Data_Extraction/MapServer?f=json"
               , justify=LEFT, padx=10, pady=10, font=fontNoBold )
label.grid( column=0, row=7, sticky="W" )

labelTitle = Label( Frame1, text="", justify=LEFT, padx=10, pady=10, font=fontBold )
labelTitle.grid( column=0, row=8, sticky="W" )

labelVersion = Label( Frame1, text="", justify=LEFT, padx=10, pady=10, font=fontNoBold )
labelVersion.grid( column=0, row=9, sticky="W" )

labelLayerTitle = Label( Frame1, text="", justify=LEFT, padx=10, pady=10, font=fontBold)
labelLayerTitle.grid( column=0, row=10, sticky="W" )

labelLayerName = Label( Frame1, text="", justify=LEFT, padx=10, pady=10, font=fontNoBold)
labelLayerName.grid( column=0, row=11, sticky="W" )

tk.mainloop()
