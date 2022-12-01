import os
import shutil
import re

for root, subdir, filenames in os.walk ("Lego/Sets/"):
    for file in filenames:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            setid = file[0:file.index(" ")]
            s = file[file.index(" ")+1:].replace(".md","")
            setname = " ".join(word[0].upper()+word[1:] for word in s.split(" ")).lower()
            setyear = file_path.split("/")[2] 
            print(f'ID: {setid} Year: {setyear} Name: {setname}')
            newheader = f"""---
hide:
  - footer
title: {setname} ({setid})
---

"""
            dst = f"Lego/Sets2/{setyear}/{setname}.md".replace(" - ","-").replace(" ","_").replace("'","")
            with open(file_path, 'r') as r, open(dst, 'w') as w:
                data = r.read()
                w.write(newheader)
                w.write(data)

                

# for root, subdir, filenames in os.walk("./"):
#     for file in filenames:
#         if file.endswith(".md"):
#             file_path=os.path.join(root,file)
#             setid = file[0:file.index(" ")]
#             s = file[file.index(" ")+1:].replace(".md","")
#             setname = " ".join(word[0].upper()+word[1:] for word in s.split(" "))
#             setyear = file_path.split("/")[1]
#             print(setid)
#             print(setname)
#             print(setyear)
#             dst = f"/Users/hal/Documents/brickmanagement/new/{setyear}/{s}.md".replace(" ","_")
#             print(dst)
#             print("---")
#             #copy the file to a new location
#             shutil.copyfile(file_path, dst)
#             # replace text in those newly copied files
#             with open(dst, 'r') as file:
#                 data = file.read()
#                 #Remove Tag cloud:
#                 # for t in tagcloud:
#                 #     print(f'Replacing {t}')
#                 #     data = data.replace(t,"")
#                 data = data.replace(tagcloud,"")
#                 data = data.replace("----", "---")
#                 k = f"""---
# hide:
#   - footer
# title: {setname} ({setid})"""
#                 l = f"""---
# title: {setid} {setname}"""
#                 data = data.replace(l,k)
#                 data = re.sub(r"creation-date:.*","",data)
#                 data = re.sub(r"modification-date:.*","",data)
#             with open(dst, 'w') as file:
#                 file.write(data)
