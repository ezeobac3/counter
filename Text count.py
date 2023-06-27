import os
textContent = []
myCollection = []


"""response = input("please enter the fullname name of a parsable text document you want to process:>>> ")
directpath = os.path.abspath(response)"""

response = input("Please help us find the text documents by providing a path to the text document:>>> ")

# while PathError: (trying to figure the specific name for this value return case error) 

if FileNotFoundError:
    response = input("Path does not exist. Please specify accurately:>>> ") 
    while FileExistsError:
        file_path = input("please enter the full path to .txt (text) file": )
        response = f"/Users/{file_path}/Desktop/project/samplemessage.txt"


files = open(response, "r")
files_list = [file for file in files]
print(files_list)
input("which file would you like too process?:>>> ")


if input not in files_list:
    input("file not found. Try another file:>>> ")
else:
    wordsInText = []       
    linesInText = []
    def text_words(text_document):
        wordcount = 0
        linecount = 0
        docProcessing = open(text_document)
        content = text_document.read()
        word_split = content.read(" ")
        line_split = content.split("\n")

        #this sets the parameters for reading number of lines in the text file
        
        for snippet in word_split:
            wordsInText.append(snippet)
            wordcount += 1

        #this counts the number of words in the document

        for word_line in line_split:
            linesInText.append(word_line)
            linecount += 1

        #this counts the number of lines in the opened file

        text30Words = []
        for num in range(29):
            text30Words.append(wordsInText[num])
        print(f"there are {wordcount} number of words and {linecount} number of lines in this document")
        print(f"the first 30 words in this document are {text30Words}")
        return







    