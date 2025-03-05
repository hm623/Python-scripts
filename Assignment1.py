import random
import array

#create array
arrNum = array.array('i')

#put generated numbers in array. Not sure how to generate random numbers without creating a lower and upper bound so I just chose 1 to 1000
for i in range(25):
    genNum = random.randint(1,1000) 
    arrNum.append(genNum)
    
    
#finds the largest number and puts it in largeNum
largeNum = max(arrNum)


#output. shows the largest number
print("Largest number is ", largeNum)

