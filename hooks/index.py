import pandas as pd
import os
import re

# The directory of files to iterate through:
directory='Lego/Sets'

def updategallery(path, setid):
    pass
    # with open(path, 'w+') as file:
    #     re.sub('\n<!-- Begin Gallery -->.*?<!-- End Gallery -->','',file, flags=re.DOTALL)

def bricksetparser(*args, **kwargs):
    """
    Export a csv from brickset.com and 'massage' it as needed
    """
    
    data = pd.read_csv('Brickset-Sets.csv')
    
    #Dropping columns I don't want to display
    data.drop(['Pieces', 'RRP (GBP)','RRP (USD)','RRP (CAD)','RRP (EUR)','EAN','UPC','Width','Height',
                'Depth','Weight','Notes','Qty owned','Qty owned new','Qty owned used','Wanted','Qty wanted',
                'Priority','Flag 1 not used','Flag 2 not used','Flag 3 not used','Flag 4 not used','Flag 5 not used',
                'Instagrammed','Flag 7 not used','Flag 8 not used','Value new (USD)','Value used (USD)','Launch date','Exit date'], inplace=True, axis=1)
    
    # Replacing Nan values with 0
    data['Minifigs'].fillna(0,inplace=True)
    data['Subtheme'].fillna('',inplace=True)
    
    #ToDo: Adding a column for images
    ## data['Imnages']=0
    
    # Get the Set ID for each set and update the pandas DataFrame record
    for root, subdir, filenames in os.walk(directory):
        for file in filenames:
            # We only care about files with the MarkDown extensions
            if file.endswith(".md"):
                file_path=os.path.join(root,file)
                setid=''
                with open(file_path, 'r') as file:
                    for line in file:
                        # In my format I get the Set ID from the title Meta field
                        if line.startswith("title:"):
                            try:
                                #Update the Dataframe (CSV) with a Link to the page
                                path = str(file_path).replace(".md","").replace("Lego/","/")
                                setid = line.split("(",1)[1].replace(")","").replace("\n","")
                                index = data.index[data['Number'] == f'{setid}-1'].tolist()[0]
                                data.at[index,'Number']=f'<a href="{path}">{setid}</a>'

                                # Update the Gallery tags with images in the /Lego/Resources/<setid>
                                updategallery(file_path, setid)
                            except:
                                pass    # Record not formatted correctly
    data.to_csv('index.csv', index=False)


# def buildindexcsv(*args, **kwargs):
#     """
#     This function generates the index.csv file in the root directory
#     which in turn is being used by the table-reader plugin to display
#     all sets on the home page.
#     """
#     with open('index.csv','w') as f:
#         # Initialize the writer
#         writer=csv.writer(f)
#         # Setting the header row for the index
#         header=['Set Name','Set ID', 'Set Year', 'Photos','MiniFigs']
#         writer.writerow(header)
#         print("Generating Index")
#         # Iterate through every directory specified above
#         for root, subdir, filenames in os.walk(directory):
#             for file in filenames:
#                 # We only care about files with the MarkDown extensions
#                 if file.endswith(".md"):
#                     file_path=os.path.join(root,file)
#                     print(file_path)
#                     # Get the set name (replace _ with space)
#                     setname = "[[{}]]".format(file.replace('.md',''))
#                     setid=''
#                     with open(file_path, 'r') as file:
#                         setyear = ''
#                         # In my case the setyear is the subfolder the file is in
#                         setyear = subdir
#                         for line in file:
#                             # In my format I get the Set ID from the title Meta field
#                             if line.startswith("title:"):
#                                 try:
#                                     setid = line.split("(",1)[1].replace(")","").replace("\n","")
#                                     print(setid)
#                                 except:
#                                     print("record not formatted correctly")
#                     data=[setname,setid,setyear,'x','x']
#                     writer.writerow(data)