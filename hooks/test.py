import os

delnext=False
with open('Lego/Sets/2015/AT-AT_Microfighter.md') as file:
    print("starting")
    for line in file:
        if delnext==True:
            line=""
            print(f"Deleting {line}")
        else:
            print("nothing")
        
        if line.contains('<!-- Begin Gallery -->'):
            print("T")
            delnext=True
        elif line.contains('<!-- End Gallery -->'):
            print("F")
            delnext=False