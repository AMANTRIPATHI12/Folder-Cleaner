import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

def removeEmptyFolders(folder):
    # Check if the folder is empty
    if not os.listdir(folder):
        os.rmdir(folder)

def Create_And_Put():
    files = os.listdir()
    files.remove("Folder cleaner.py")

    # Create necessary folders
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Python')
    createIfNotExist('Excel')
    createIfNotExist('Zip Files')
    createIfNotExist('Others')

    # Define file extensions for categorization
    imgExts = [".png", ".jpg", ".jpeg"]
    docExts = [".txt", ".docx", ".doc", ".pdf", ".csv", ".pptx", ".ppt", ".html"]
    mediaExts = [".mpeg", ".mp4", ".mp3", ".flv", ".wav", ".wma", ".aac", ".mp4a"]
    pythonExts = [".py"]
    excelExts = [".xlsx", ".xlsb", ".xls"]
    zipExts = [".rar", ".zip", ".cab", ".arj", ".lzh", ".ace", ".tar", ".gzip", ".uue", ".bz2", ".jar", ".iso"]

    # Sort files into categories
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    python = [file for file in files if os.path.splitext(file)[1].lower() in pythonExts]
    excel = [file for file in files if os.path.splitext(file)[1].lower() in excelExts]
    zipFiles = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in zipExts) and (ext not in excelExts) and (ext not in pythonExts) and os.path.isfile(file):
            others.append(file)

    # Move files to respective folders
    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Python", python)
    move("Excel", excel)
    move("Zip Files", zipFiles)
    move("Others", others)

    # Remove empty folders
    for folder in ['Images', 'Docs', 'Media', 'Python', 'Excel', 'Zip Files', 'Others']:
        removeEmptyFolders(folder)

if __name__ == '__main__':
    Create_And_Put()
