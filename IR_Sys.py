import sys
import os
import re
import math
from PorterStemmer import PorterStemmer

if(len(sys.argv) !=5):
    raise ValueError('Enter four arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]
StopWord_filename=sys.argv[3]
Query_words=sys.argv[4]

#Convert list to string
def listToString(s): 
    str1 = " " 
    return (str1.join(s))

#Code to read query file
print("The query words are:")
print(Query_words)

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

#cosine similarity function
def Cos_Sim(v1,v2):
    dot_prod = sum(n1 * n2 for n1, n2 in zip(v1, v2))
    vector1 = math.sqrt(sum(n**2 for n in v1))
    vector2 = math.sqrt(sum(n**2 for n in v2))
    cross_prod = vector1*vector2
    return (dot_prod/cross_prod)

files_dict={}
all_files=os.listdir(input_folder_path)
print(all_files)

#reading the files from folder
for file in all_files:
    f=open(os.path.join(input_folder_path, file),'r')
    content=f.read()
    files_dict["{}".format(file)]=content

#arrays to store values
all_terms=[]


for key in files_dict:
    file_data= files_dict[key]

    #to lower case
    lower_content=file_data.lower()

    #removing all punctuations
    punc_content=re.sub(r'[^\w\s]','',lower_content)
    print(punc_content)

    #stopword removal
    processed_words=StopWordRemoval(punc_content)
    
    
    #stemming
    Preprocessed_output=Stemming(processed_words)        
    print(Preprocessed_output)

    #split the words
    terms_docs=Preprocessed_output.split(' ')  
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

#all the unique terms from the documents
list_of_unique_words=list(unique_words)

#final inverted index output
array_for_IINDX=[]
for one_term in list_of_unique_words:
    
    # InvertIndexOutput=("{terms}\tD1[{count1}]\tD2[{count2}]\tD3[{count3}]\n".format(terms=one_term, count1=numOfWords1[one_term],count2=numOfWords2[one_term],count3=numOfWords3[one_term]))
    InvertIndexOutput=(numOfWords1[one_term],numOfWords2[one_term],numOfWords3[one_term])
    # print(InvertIndexOutput)
    array_for_IINDX.append(InvertIndexOutput)

    

#TF-IDF calculations here
#to store frequencies of each document
freq_doc1=[]
freq_doc2=[]
freq_doc3=[]
TF_doc1=[]
TF_doc2=[]
TF_doc3=[]
for i in range(len(array_for_IINDX)):
    freq_doc1.append(array_for_IINDX[i][0])
    freq_doc2.append(array_for_IINDX[i][1])
    freq_doc3.append(array_for_IINDX[i][2])


#code for TF calculation
for j in freq_doc1:
    TF_doc1.append(j/max(freq_doc1))
TF_doc1=[float(a) for a in TF_doc1]
print("Term frequency in Doc1: ")
print(TF_doc1)

for k in freq_doc2:
    TF_doc2.append(k/max(freq_doc2))
TF_doc2=[float(a) for a in TF_doc2]
print("Term frequency in Doc2: ")
print(TF_doc2)

for l in freq_doc3:
    TF_doc3.append(l/max(freq_doc3))
TF_doc3=[float(a) for a in TF_doc3]
print("Term frequency in Doc3: ")
print(TF_doc3)

#code for TF-IDF 
TF_IDF_doc1=[]
TF_IDF_doc2=[]
TF_IDF_doc3=[]
for n in range(len(freq_doc1)):
    count=0
    if freq_doc1[n]>0:
        count+=1
    if freq_doc2[n]>0:
        count+=1
    if freq_doc3[n]>0:
        count+=1
    
    no_of_docs =3
        
    TF_IDF_doc1.append(round(TF_doc1[n]*math.log10(no_of_docs/count),3))
    TF_IDF_doc2.append(round(TF_doc2[n]*math.log10(no_of_docs/count),3))
    TF_IDF_doc3.append(round(TF_doc3[n]*math.log10(no_of_docs/count),3))




#code for processing of Query words below
print("="*20)
#Preprocessing of query words
#to lower case
lower_content=Query_words.lower()

#removing all punctuations
punc_content=re.sub(r'[^\w\s]','',lower_content)

#stopword removal
processed_words=StopWordRemoval(punc_content)

#stemming
Preprocessed_query=Stemming(processed_words)        
print(Preprocessed_query)

#inverted index
list=Preprocessed_query.split(" ")
print(list)
query_set=set(list)
print(query_set)



#Query words



