import os,shutil

s=os.chdir("Downloads")
current = os.getcwd()

files=os.listdir(current)

images=[".jpeg",".png",".jpg",".gif", ".svg"]
sounds=[".mp3",".wav",".m4a"]
applications=[".exe",".lnk"]
code = [".c",".py",".java",".cpp",".js",".html",".css",".php"]
torrents = [".torrent"] 

print("Sorting the files...")

for file in files:
    dest = ""
    for ex in images:
        if file.endswith(ex):
            dest='./Pictures'
            shutil.move(file,dest)
            break
    for ex in sounds:
        if file.endswith(ex):
            dest='./Sound'
            shutil.move(file,dest)
            break

    for ex in applications:
        if file.endswith(ex):
            dest= './Setups'
            shutil.move(file,dest)
            break

    for ex in code:
        if file.endswith(ex):
            dest= './Code'
            shutil.move(file,dest)
            break

    for ex in torrents:
        if file.endswith(ex):
            dest= './Torrents'
            shutil.move(file,dest)
            break

print("Sorting Completed...")