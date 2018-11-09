#!/usr/bin/env python

# run this locally to take FFMPEG packet files and get the actual timestamps for frames

import os, sys, re
#from PyRTF import *

#target = sys.argv[1]
#targetfiles = os.listdir(target + "/raw")
# print target
# print targetfiles

#v = "1614"

checkfile = open("checkfile.csv", "a")
checkfile.write("subid,last.frame,length\n")

#for f in filter(lambda a: a.find(".txt") != -1, targetfiles):
# print f
for filename in os.listdir("raw"):

   fin = open("raw/" + filename, "r")
   short_f = filename.split("_")[1] + ".csv"
   fout = open(short_f, "w")
   fout.write("frame,pkt_time,best_time\n")

   contents = fin.read().split("[FRAME]")
   m = None
   i = 1
   for c in contents:
       if c.find("media_type=video") != -1:
           m = re.search(r"pkt_pts_time=\d+.\d+", c) or None
	   n = re.search(r"best_effort_timestamp_time=\d+.\d+", c) or None
           fout.write(str(i) + "," + m.group(0).replace("pkt_pts_time=", "") + "," + n.group(0).replace("best_effort_timestamp_time=","") + "\n")
           i = i + 1

   checkfile.write("XS-" + short_f + "," + str(i - 1) + "," + m.group(0).replace("pkt_pts_time=", "") + "\n")


