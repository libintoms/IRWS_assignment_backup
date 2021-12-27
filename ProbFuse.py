import sys
import csv

#input statement
hresult_file = input("Enter the name of historic results file? eg: testresult.csv\n")

#dictionary to store the historic data
hresult_dict={}


#reading historic file
try: 
    with open(hresult_file, 'r', encoding='utf-8-sig') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            key=row[0]
            if key in hresult_dict:
                pass
            hresult_dict[key]=row[1:]
            
        
        print("Total no. of rows: %d"%(csvreader.line_num))
       
except:
    raise Exception("File " + hresult_file + " not found")

#variables for calculation
length=len(hresult_dict["A1"])
list_array=hresult_dict['A1']


# User input to divide historic data into segments
segments = input("Enter the number of segments? chose between 0-99\n")
print("Entered segment is: "+str(segments))
segments=int(segments)
itemCount_each_seg=int(length/segments)
print("Items in each segment:"+str(itemCount_each_seg))

#function to divide data into equal segments
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


r=0     #count of 'R' in each segment
c=0     #count of iterations till segment end
k=0     #count of segment items for eg: 25 items if seg=4
rating_dict={}
for key in hresult_dict:
    hresult_dict[key]=(list(chunks(hresult_dict[key], itemCount_each_seg)))
    for i in range(segments):
        for j in hresult_dict[key][i]:
            if j=='R':
                r=r+1
            c=c+1
            if c==segments:
                rating=(r/itemCount_each_seg)
                rating_dict["K{}".format(k)+key] = rating
                k=k+1
                if k==segments:
                    k=0
                r=0
                c=0

# Getting probfuse value of each engine
sorted_keys = sorted(rating_dict)
res, ind = dict(), 0
while ind<len(rating_dict):
    temp = []

    for i in range(ind, ind+3):
        temp.append(rating_dict[sorted_keys[i]])
    else:
        res[sorted_keys[i][:3]] = temp
        ind += 3
for x in range(segments):
    res['K'+str(x)+"A"]=(round(sum(res['K'+str(x)+"A"])/len(res['K'+str(x)+"A"]),2))
    res['K'+str(x)+"B"]=round(sum(res['K'+str(x)+"B"])/len(res['K'+str(x)+"B"]),2)
    res['K'+str(x)+"C"]=round(sum(res['K'+str(x)+"C"])/len(res['K'+str(x)+"C"]),2)
    res['K'+str(x)+"D"]=round(sum(res['K'+str(x)+"D"])/len(res['K'+str(x)+"D"]),2)
print("The probfuse value of each engine is:")
print(res)

#input statement
liveresult_file = input("Enter the name of live results file? eg: testresult.csv\n")

#dictionary to store the live data
liveresult_dict={}

#reading live result file
try: 
    with open(liveresult_file, 'r', encoding='utf-8-sig') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            key=row[0]
            if key in liveresult_dict:
                pass
            liveresult_dict[key]=row[1:]


        print("Total no. of rows: %d"%(csvreader.line_num))
       
except:
    raise Exception("File " + liveresult_file + " not found")

for key in liveresult_dict:
    liveresult_dict[key]=(list(chunks(liveresult_dict[key], itemCount_each_seg)))

# print(liveresult_dict)
lresult_A=liveresult_dict['A']
# print(lresult_A)
lresult_B=liveresult_dict['B']
# print(lresult_B)
lresult_C=liveresult_dict['C']
# print(lresult_C)
lresult_D=liveresult_dict['D']
# print(lresult_D)

#input statement
fusion_input = input("What results to be fused out of A, B, C or D enter engine name comma seperated\n")
fusion_array = fusion_input.split(",")
print(fusion_array)

for engine in liveresult_dict:
    if engine in fusion_array:
        live_results_csv_dictionary_array = liveresult_dict[engine]
        print(live_results_csv_dictionary_array)
    






