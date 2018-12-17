# ZIP FILE извлечь все файлы с архива
import shutil
import os, sys
import zipfile
directory =         os.path.join('D:/','All_photos','20181215') #first source
outcome_directory = directory + r'_unzip'     #output manually cropping photo
just_photo = directory + r'_photo'
files = os.listdir(directory) #list of item in directory
#a=0
try:
    nf1 = os.makedirs(outcome_directory)
    nf2 = os.makedirs(just_photo)
    print('Folder(s) are creted')
except FileExistsError:
    print('Folder(s) already were creted')
    pass
def zip(directory, outcome_directory, files):
    for i in files:
        #TRY, DIDN'T CHECK!!!!!!
        try:
            z = zipfile.ZipFile(directory+'\\'+i, 'r')
            z.extractall(outcome_directory)
        except Exception:
            print(i)
        c=os.listdir(outcome_directory)  #список папок внутри которых фотки и json
    print('All files are extracted')
    return c
def move(outcome_directory, just_photo):
    for i in zip(directory, outcome_directory, files):
        v = os.listdir(outcome_directory + '\\' + i)
        shutil.move(outcome_directory + '\\' + i + '\\' + v[2], just_photo)
#zip(directory, outcome_directory, files)
try:
    move(outcome_directory, just_photo)
    print('Done')
except Exception:
    print('Some error')