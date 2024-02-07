#Random logo function
import secrets
from os import listdir
from os.path import isfile, join

def randomLogo(listLogoFiles: str) -> str:

    logoNow = secrets.choice(listLogoFiles)

    return logoNow

def listAllFiles(pathFiles: str) -> list:
    listLogos = [f for f in listdir(pathFiles) if isfile(join(pathFiles, f))]

    return listLogos

#print(randomLogo(listAllFiles(r"D:\Python\practicas\pythonWeb\linkBio\assets\logos")))

