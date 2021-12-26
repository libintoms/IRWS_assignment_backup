import sys
import csv

#
hresult_file = input("Enter the name of historic results file? eg: testresult.csv\n")

#variables to store the values
hresult_dict={}


#reading historic file
try: 
    with open(hresult_file, 'r', encoding='utf-8-sig') as f:
        csvreader = csv.reader(f)
        print(csvreader)
        for row in csvreader:
            key=row[0]
            if key in hresult_dict:
                pass
            hresult_dict[key]=row[1:]
            
        
        print("Total no. of rows: %d"%(csvreader.line_num))
       
except:
    raise Exception("File " + hresult_file + " not found")


length=len(hresult_dict["A1"])
print(length)
list_array=hresult_dict['A1']


# User input to divide historic data into segments
segments = input("Enter the number of segments? chose between 0-99\n")
print("Entered segment is: "+str(segments))
segments=int(segments)
itemCount_each_seg=int(length/segments)
print("items in each segment:"+str(itemCount_each_seg))

#function to divide data into equal segments
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# print(list(chunks(list_array, segments)))
r=0   #count of 'R' in each segment
c=0   #count of segment items for eg: 25 items if seg=4
rating_dict={}
for key in hresult_dict:
    hresult_dict[key]=(list(chunks(hresult_dict[key], itemCount_each_seg)))
    for i in range(segments):
        for j in hresult_dict[key][i]:
            if j=='R':
                r=r+1
            c=c+1
        # print(c)
        # print(r)
            if c==segments:
                rating=(r/itemCount_each_seg)
                # print(rating)
                for x in range(segments):
                    rating_dict["K{}".format(x)+key] = rating
                r=0
                c=0
# print(rating_dict)

sorted_keys = sorted(rating_dict)
res, ind = dict(), 0

while ind<len(rating_dict):
    temp = []

    for i in range(ind, ind+3):
        temp.append(rating_dict[sorted_keys[i]])
    else:
        res[sorted_keys[i][:3]] = temp
        ind += 3

print(res)
for x in range(segments):
    print (x)
    print(res['K'+str(x)+"A"])




