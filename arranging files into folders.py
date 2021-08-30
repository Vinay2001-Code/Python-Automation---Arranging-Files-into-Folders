import os

def ArrangeFiles(path):
    files = os.listdir(path) 
    extension = []
    
    for file in files:
        #print(os.path.splitext(file)[1][1:])  to get only the extensions 
        #ext = os.path.splitext(file)[1][1:]   to remove the duplicates and append in ext 
        ext = os.path.join(path,os.path.splitext(file)[1][1:]) # With path 

        if ext not in extension:
            extension.append(ext)   

    for folder in extension:
        try:
            os.mkdir(folder)
        except:
            pass    
        
        for file in files:
            if os.path.split(folder)[1] == os.path.splitext(file)[1][1:]:
                os.rename(os.path.join (path,file),os.path.join(folder,file))  # rename moving files from one path to another

if __name__=='__main__':
    path = r"C:\Users\91917\Desktop\Project"
    ArrangeFiles(path)
