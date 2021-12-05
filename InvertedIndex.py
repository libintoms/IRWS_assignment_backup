import sys
import os

if(len(sys.argv) !=3 ):
    raise ValueError('Enter three arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]

all_terms=[]

for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()
    
    #split the words
    terms_docs=content.split(' ')  
    all_terms.append(terms_docs)

#Set of terms in individual documents
terms_doc1=all_terms[0]
terms_doc2=all_terms[1]
terms_doc3=all_terms[2]

#set of unique words from all documents
unique_words=set(terms_doc1).union(set(terms_doc2).union(set(terms_doc3)))

#count of terms in the document
numOfWords1=dict.fromkeys(unique_words,0)
for word in terms_doc1:
    numOfWords1[word]+=1
numOfWords2=dict.fromkeys(unique_words,0)
for word in terms_doc2:
    numOfWords2[word]+=1
numOfWords3=dict.fromkeys(unique_words,0)
for word in terms_doc3:
    numOfWords3[word]+=1

#print inverted index
list_of_unique_words=list(unique_words)
f=open(os.path.join(output_folder_path,'InvertedIndex_results.txt'),'w')
for one_term in list_of_unique_words:
    InvertIndexOutput=(one_term+'\t'+'D1['+str(numOfWords1[one_term])+']'+'\t'+
    'D2['+str(numOfWords2[one_term])+']'+'\t' 
    'D3['+str(numOfWords3[one_term])+']'+'\n')
    
    #file write
    f.write(InvertIndexOutput)    
f.close()

