import sys
import os

if(len(sys.argv) !=3):
    raise ValueError('Enter three arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]

for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()

    chars_row=content.splitlines(True)
    newtest = [x[:-1] for x in chars_row]
    # print(newtest)
    total_count=len(newtest)
    print("The total items in array newtest: "+str(total_count))

    for i in range(total_count):
        split_chars_row=newtest[i].split("\t")
        print(split_chars_row)

    print(split_chars_row[0])