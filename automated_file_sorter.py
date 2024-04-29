#### automated file sorter 
import os
import shutil

path = "C:/Users/ghanmi/Desktop/bootcamp data/automate file sorter/"

# Dictionary mapping file extensions to folder names
folder_names = {
    '.png': 'png',
    '.xlsx': 'xlsx',
    '.pptx': 'pptx'
}

# Create folders if they don't exist
for folder in folder_names.values():
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

# Get a list of all files in the directory
file_names = os.listdir(path)

# Iterate over each file
for file in file_names:
    # Get the file extension
    _, ext = os.path.splitext(file)
    # Check if the file extension is in the dictionary
    if ext in folder_names:
        # Move the file to the corresponding folder
        src = os.path.join(path, file)
        dest = os.path.join(path, folder_names[ext], file)
        if not os.path.exists(dest):
            shutil.move(src, dest)


'''
import os , shutil 

path=r"C:/Users/ghanmi/Desktop/bootcamp data/automate file sorter/"

folder_names =['png' , 'xlsx','pptx']

for i in range(3):
    if not os.path.exists(path+folder_names[i]):
        os.makedirs(path+folder_names[i])


file_name = os.listdir(path)
print(file_name)

for file in file_name:
    if ".png" in file and not os.path.exists(path+"png/"+ file):
        shutil.move(path+file , path+"png/"+file)
    elif '.xlsx' in file and not os.path.exists(path+'xlsx/'+file):
        shutil.move(path+file , path+'xlsx/'+file)
    elif '.pptx' in file and not os.path.exists(path+'pptx/'+file):
        shutil.move(path+file , path+'pptx/'+file)'''