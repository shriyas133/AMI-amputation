import pandas as pd
import os

myfiles = []
source_directory = "."
for file in os.listdir(source_directory):
    if file.endswith(".csv"):
        myfiles.append(os.path.join(source_directory, file))
myfiles

new_folder = "exg_csv_processed"

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

s = input("Enter exg Streams to Keep: ")
exgStreamsToKeep = list(map(int, s.split()))
keep = ["Time", "Events","Digi"]
for i in range(len(exgStreamsToKeep)):
    exgi = "ExG" + str(exgStreamsToKeep[i])
    keep.append(exgi)

for i in range(len(myfiles)):
    myfile = myfiles[i]
    df = pd.read_csv(myfile, skiprows=0, error_bad_lines = False,
    	             warn_bad_lines=False, low_memory=False)
    
  
    df = df[keep]
    df.to_csv(os.path.join(source_directory, new_folder + myfile[1:]), index=False)

