import os
def rename_files():
    #1. get file names from folder
    file_list=os.listdir(r"C:\Users\Rajeshwar Rao P\Desktop\Shivani\infosys\prank") #r stands for raw
    print(file_list)
    #saved_path=os.getcwd()
    #print(saved_path)
    os.chdir(r"C:\Users\Rajeshwar Rao P\Desktop\Shivani\infosys\prank")
    #2. for each file name remove numbers
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
rename_files()
