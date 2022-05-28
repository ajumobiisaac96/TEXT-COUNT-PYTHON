# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#Ask for the file name
file_name= input("Enter file name: \n")

#Function to open and read the file 
def read_file_content(file_name):
	text= open(file_name)
	
    #turn all the words to lower case bcos python is case sensitive
	text= text.read().lower()
	return text

#function to count the words 
def count_word():
	text= read_file_content(file_name)
	
    #remove all the punctuations 
	pun= [",",".","?"]
	for a in pun:
		text= text.replace(a, " ")
		text_splitted= text.split()
		
        #create an empty dictionary to add the words as they are beinh counted
		word_dic ={}
	for word in text_splitted:
		
        #if word not already found un dictionary, append it using the word as key and the count as value
		if word not in word_dic:
			word_dic[word]= text_splitted.count(word)
			#print the dictionary
	print (word_dic)

count_word()
