import os

def rename_files():
    #(1) get file names from a folder
    file_list=os.listdir(r"C:\Users\Ckay\Desktop\python codes\rename\prank")
    print (file_list)
    
    #change directory
    saved_path=os.getcwd()
    os.chdir(r"C:\Users\Ckay\Desktop\python codes\rename\prank")
    
    #(2)for each file, rename filename
    for file_name in file_list:
        print("old name- "+file_name)
        os.rename(file_name,file_name.translate(None, "0123456789"))
        print("new name- "+file_name)
    os.chdir(saved_path)   
#executing it
rename_files()
