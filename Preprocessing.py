import sys
import os
import re
from PorterStemmer import PorterStemmer

if(len(sys.argv) !=4 ):
    raise ValueError('Enter valid arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]
StopWord_filename=sys.argv[3]

#Convert list to string
def listToString(s): 
    str1 = " " 
    return (str1.join(s))

#Stopword removal function
def StopWordRemoval(string_words):
    f=open(os.path.join(sys.path[0], StopWord_filename),'r')
    file_contents=f.read()
    stopwords=file_contents.split()
    query_words=string_words.split()
    stopwords_removal= [word for word in query_words if word not in stopwords]
    output=' '.join(stopwords_removal)
    return output

#Porter Stemmer function
def Stemming(string):
    split_words=string.split()
    p=PorterStemmer()
    stemmed_words_list=[]
    for word in split_words:
        x=p.stem(word,0,len(word)-1)
        stemmed_words_list.append(x)
    output=listToString(stemmed_words_list)
    return output

for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()
    
    #to lower case
    lower_content=content.lower()

    #removing all punctuations
    punc_content=re.sub(r'[^\w\s]','',lower_content)

    #stopword removal
    processed_words=StopWordRemoval(punc_content)
    
    
    #stemming
    Preprocessed_output=Stemming(processed_words)
            
    print(Preprocessed_output)
    

    #file write
    f=open(os.path.join(output_folder_path,filename),'w')
    f.write(Preprocessed_output)    
    f.close()


       



