import os, random
            
def shuffle(dir: str):
    dirName = os.path.basename(dir)
    dirParentPath = os.path.dirname(dir)
    shuffledPath = rf"{dirParentPath}\Shuffled {dirName}"
    
    files = os.scandir(dir)
    shuffledFiles = list()

    #Defines the order of the videos
    for file in files:
        shuffledFiles.append(file.path)
    random.shuffle(shuffledFiles)

    if not os.path.isdir(shuffledPath):
        os.mkdir(shuffledPath)
    
    for index, file in enumerate(shuffledFiles):
        os.rename(file, rf"{shuffledPath}\{index}{os.path.splitext(file)[1]}")
        

# Main
shuffle(r"C:\Users\Davi\Downloads\cu")
