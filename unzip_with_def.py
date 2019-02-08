# ZIP FILE извлечь все файлы с архива
import shutil
import os, sys
import zipfile
directory =         os.path.join('/Users','olehpryshliak','Documents','All_photos','20190103') #first source
outcome_directory = directory + r'_unzip'
just_photo = directory + r'_photo'
files = os.listdir(directory) #list of item in directory
#a=0 /Users/olehpryshliak/Documents/All_photos/20190123
#     'Users/olehpryshliak/Documents/All_photos/20190123'
try:
    os.makedirs(outcome_directory)
    os.makedirs(just_photo)
    print('Folder(s) are creted')
except FileExistsError:
    print('Folder(s) already were creted')
    pass
def zip(directory, outcome_directory, files):
    for i in files:
        if not i.startswith('.'):
        #TRY, DIDN'T CHECK!!!!!!
            z = zipfile.ZipFile(directory+'//'+i, 'r')
            z.extractall(outcome_directory)
            c=os.listdir(outcome_directory)  #список папок внутри которых фотки и json
    print('All files are extracted')
    return c
def move(outcome_directory, just_photo):
    for i in zip(directory, outcome_directory, files):
        v = os.listdir(os.path.join(outcome_directory,i))
        for item in v:
            if item.endswith('obj.0.1.jpg'):
                shutil.move(outcome_directory + '//' + i + '//' + item, just_photo)
#zip(directory, outcome_directory, files)
try:
    move(outcome_directory, just_photo)
    print('Done')
except Exception:
    print('Some error')
    pass