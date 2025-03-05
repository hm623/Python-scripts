import csv

f = open("/Users/tempguest/Documents/comp467/assignment3/a3.txt", "r")
results = []


for line in f:
words = line.split()
nums = []

for word in words:
if "\n" in word:
word = word.replace("\n", "")
if word.isdigit():
nums.append(int(word))

total = sum(nums)
results.append(total)
f.close()

csvfile = open("/Users/tempguest/Documents/comp467/assignment3/output.csv", "w", newline="")
writer = csv.writer(csvfile)
