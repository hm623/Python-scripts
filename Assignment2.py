import array  

f = open("/Users/tempguest/Documents/ingest_this.txt", "r")
count = 0  

for line in f:
    words = line.split()

    numbers = array.array('i')  

    for word in words:
        if word.isdigit():
            numbers.append(int(word))  

    for num in numbers:  
        print(num, end=" ")  
        count += 1  

        #every 3 numbers printed, goes to next line. Not sure how to do this efficiently
        if count == 3:  
            print()  
            count = 0  

f.close()