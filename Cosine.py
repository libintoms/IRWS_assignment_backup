import sys
import os
import math

if(len(sys.argv) !=3):
    raise ValueError('Enter three arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]

#arrays to hold document values
doc1_freq=[]
doc2_freq=[]
doc3_freq=[]

#cosine similarity function
def Cos_Sim(v1,v2):
    dot_prod = sum(n1 * n2 for n1, n2 in zip(v1, v2))
    vector1 = math.sqrt(sum(n**2 for n in v1))
    vector2 = math.sqrt(sum(n**2 for n in v2))
    cross_prod = vector1*vector2
    return (dot_prod/cross_prod)

for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()
    
    #removal of junk chararcters
    single_array=content.splitlines(True)
    # print(single_array)
    new_array=[x[:-1] for x in single_array]
    # print(new_array)
    total_items=len(new_array)
    for i in range(total_items):
        items_array=new_array[i].split("\t")
        # print(items_array[1])
        doc1_freq.append(items_array[1])
        doc2_freq.append(items_array[2])
        doc3_freq.append(items_array[3])

#Converting string to int
doc1_freq=[float(a) for a in doc1_freq]
doc2_freq=[float(a) for a in doc2_freq]
doc3_freq=[float(a) for a in doc3_freq]

print("Frequencies in document 1:")
print(doc1_freq)
print("*"*20)
print("Frequencies in document 2:")
print(doc2_freq)
print("*"*20)
print("Frequencies in document 3:")
print(doc3_freq)
print("*"*20)

squared_freq_doc1=[n**2 for n in doc1_freq]
print(squared_freq_doc1)
squared_freq_doc2=[n**2 for n in doc2_freq]
print(squared_freq_doc2)
squared_freq_doc3=[n**2 for n in doc3_freq]
print(squared_freq_doc3)

sum_freq_doc1=sum(squared_freq_doc1)
print(sum_freq_doc1)
sum_freq_doc2=sum(squared_freq_doc2)
print(sum_freq_doc2)
sum_freq_doc3=sum(squared_freq_doc3)
print(sum_freq_doc3)

sqrt_doc1=math.sqrt(sum_freq_doc1)
print(sqrt_doc1)
sqrt_doc2=math.sqrt(sum_freq_doc2)
print(sqrt_doc2)
sqrt_doc3=math.sqrt(sum_freq_doc3)
print(sqrt_doc3)

CrossProd_d1_d2=sqrt_doc1*sqrt_doc2
CrossProd_d2_d3=sqrt_doc2*sqrt_doc3
CrossProd_d1_d3=sqrt_doc1*sqrt_doc3
print("The denominator for d1 & d2:"+str(CrossProd_d1_d2))
print("The denominator for d2 & d3:"+str(CrossProd_d2_d3))
print("The denominator for d1 & d3:"+str(CrossProd_d1_d3))

#Dot product code
DotProd_d1_d2= sum(n1*n2 for n1, n2 in zip(doc1_freq, doc1_freq))
print(DotProd_d1_d2)
DotProd_d2_d3= sum(n1*n2 for n1, n2 in zip(doc2_freq, doc3_freq))
print(DotProd_d2_d3)
DotProd_d1_d3= sum(n1*n2 for n1, n2 in zip(doc1_freq, doc3_freq))
print(DotProd_d1_d3)

#final output










