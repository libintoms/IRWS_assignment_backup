import sys
import os
import re

if(len(sys.argv) !=3 ):
    raise ValueError('Enter valid arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]
# StopWord_filename=sys.argv[3]

files_dict={}
all_files=os.listdir(input_folder_path)
print(all_files)
for file in all_files:
    f=open(os.path.join(input_folder_path, file),'r')
    content=f.read()
    files_dict["{}".format(file)]=content

for key in files_dict:
    file_data= files_dict[key]

    #to lower case
    lower_content=file_data.lower()

    #removing all punctuations
    punc_content=re.sub(r'[^\w\s]','',lower_content)
    print(punc_content)

        