import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filepath", help="the path to the text file")

parser.add_argument("--verbose", action="store_true", help="print each line")

args = parser.parse_args()


document = open(args.filepath, "r")
lines = document.readlines()
document.close()


if(args.verbose):
print("Lines in the text file: ")
for line in lines:
print(line)


line_count = len(lines)
print("Line count: "+str(line_count))
