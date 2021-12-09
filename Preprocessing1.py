import sys
import os
import re
from PorterStemmer import PorterStemmer

if(len(sys.argv) !=4 ):
    raise ValueError('Enter valid arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]

for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()
    
    #to lower case
    lower_content=content.lower()

    #removing all punctuations
    punc_content=re.sub(r'[^\w\s]','',lower_content)

    #stopword removal
    stopwords=["a","for","many","of","at","as","each","and", "the", "is","this", "one", "more", "it", "can", 
        "to", "if", "well", "in", "or", "to","their","an","but","how","are"]
    query_words=punc_content.split()
    stopwords_removal= [word for word in query_words if word not in stopwords]
    processed_words=' '.join(stopwords_removal)
    print(processed_words)

    #stemming
    porter_stemmer = PorterStemmer()
    output=porter_stemmer.stem(processed_words,0,len(processed_words)-1)
    print(output)

    #file write
    f=open(os.path.join(output_folder_path,filename),'w')
    f.write(processed_words)    
    f.close()

       



