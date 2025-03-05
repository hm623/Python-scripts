import csv  

# open files
f1 = open(r"/Users/tempguest/Documents/comp467/project1/Xytech_spring2025.txt", "r")
xytech = f1.readlines()
f1.close()  # Manually close the file

f2 = open(r"/Users/tempguest/Documents/comp467/project1/Baselight_export_spring2025.txt", "r")
baselight_export = f2.readlines()
f2.close()  # Manually close the file

# function to remove '/' and separate the paths
# example: /hpsans13/production/dogman/reel1/partA/1920x1080 becomes [hpsans13, production, dogman, reel1, partA, 1920x1080]
def pathSplitter(locs):
    new_list = []  
    for item in locs:  
        if item.strip():  
            split_path = item.split("/")  
            new_list.append(split_path)  
    return new_list

# function to remove '\n' 
# example: "Xytech Workorder 1169\n" becomes  "Xytech Workorder 1169"
def removeNextline(locs):
    lst = []  # Create an empty list

    for item in locs: 
        items = item.strip()  
        lst.append(items)  
    return lst  

# remove the \n 
xytech = removeNextline(xytech)
baselight_export = removeNextline(baselight_export)

# locate location:
locIndex_xytech = xytech.index("Location:")

# extract all lines after "Location:" as the list of locations
xytech_locations = pathSplitter(xytech[locIndex_xytech + 1:])

# baselight locs and frames
baselightLoc = []
baselightFrames = []

for line in baselight_export:  
    parts = line.split(" ", 1)  
    baselightLoc.append(parts[0])  
    if len(parts) > 1:  
        baselightFrames.append(parts[1])  
    else:  
        baselightFrames.append("")  

baselightLoc = pathSplitter(baselightLoc)  

# create new paths 
for i in range(len(baselightLoc)):
    baselightLoc[i] = baselightLoc[i][3:]  

for i in range(len(baselightLoc)):
    for j in range(len(xytech_locations)):
        if all(element in xytech_locations[j] for element in baselightLoc[i]):
            baselightLoc[i] = xytech_locations[j]

# frames to ranges
def convertToRanges(frame_list):
    frames = [int(num) for num in frame_list.split()]
    frames.sort()
    ranges = []
    start = frames[0]
    prev = frames[0]

    for num in frames[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{prev}")
            start = num
            prev = num

    if start == prev:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{prev}")

    return ", ".join(ranges)

baselightFrames = [convertToRanges(frames) for frames in baselightFrames if frames]

# output 

output = [[",".join(paths), frame_ranges] for paths, frame_ranges in zip(baselightLoc, baselightFrames)]

csv_out = open(r"/Users/tempguest/Documents/comp467/output.csv", "w", newline="")
writer = csv.writer(csv_out)


writer.writerow(["Location", "Frames to Fix"])

writer.writerows(output)


csv_out.close()

print("Exported successfully to /Users/tempguest/Documents/output.csv")
