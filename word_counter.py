myfile = open('/Users/Christian Ezeoba/Desktop/new/mbox-shorts.txt',"r")
#opens up the file and prints out its content to be seen
print ('---THE SOURCE EMAILS AND DATES EXTRACTED FROM THIS FILE ARE:---')
for line in myfile:
    line = line.rstrip()
    word = line.split( )
    # guardian check to prevent code blowing up
    if len(word) < 1 or word[0] != 'From':
        continue
    

    print ('SOURCE EMAIL ADDRESS -----', word[1], '    ---', 'ITS RELEVANT DATE -----', word[2])
print('---these are some relevant source email addresses and their associated dates detected in this file---')
for line in myfile:
    line = line.rstrip()
    word = line.split( )
    if len(word) < 3 or word[0]!= 'Received:':
        continue
    print (word[2])
print()
print()
print()
file = open('/Users/Christian Ezeoba/Desktop/new/mbox-shorts.txt',"r")
count = 0
number = 0
content = file.read()
mark = content.split("\n")
#this sets the atmosphere for reading number of lines in the text file
for i in mark:
    if i:
        count += 1 
#this counts the number of lines in the opened file

words = content.split(" ")
for i in words:
    number += 1
#this counts the number of words in the opened file
    
print("there are ", count , " number of lines in this file")
print("there are ", number , " number of words in this file")

print("you may like to exit now")


