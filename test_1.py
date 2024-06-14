import os

folders = input('ENTHER THE FOLDER NAMES WITH SPACES IN BETWEEN :').split()

for folder in folders:

    try:
        files = os.listdir(folder)
        print('===============' + folder + ' list=================' )
    except FileNotFoundError: 
        print('plese enter valid folder name :')
        continue s

    for file in files:
        print(file)