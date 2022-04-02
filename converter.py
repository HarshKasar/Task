from typing import Type
import xml.etree.ElementTree as ETree
import pandas as pd
# load the input file
tree=ETree.parse('C:\input.xml')
root=tree.getroot()# xml parse done
a=[]# Assign empty list to use later
for ele in root:
    b={}
    for i in list(ele):
        b.update({i.tag:i.text})
        if VCHTYPE=="Recepit":
            a.append(b)
df=pd.DataFrame(a)
df.drop_duplicates(keep='first', inplace=True)
df.reset_index(drop=True,inplace=True)
writer=pd.ExcelWriter("c:/output1.xlsx",engine='xlsxwriter')
df.to_excel(writer,sheet_name='sheet1')
writer.save()
print("xml to excel converted successfully...")
