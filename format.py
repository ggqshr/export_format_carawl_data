import pandas as pda
from pathlib import Path
from io import StringIO

data = pda.read_excel("./data.xlsx",sheet_name="Sheet1",header=None,names=['name',"desc","note"])
data.fillna(" ",inplace=True)
data_dict = dict()
for item in data.iterrows():
    dd = item[1].to_dict()
    name = dd.pop("name")
    data_dict[name] = dd

this_file = StringIO()
this_file.write("index,name,desc,note\n")
content = filter(None,Path("fields.txt").read_text().split("\n"))
for index,line in enumerate(content):
    this_item = {}
    desc,note = "",""
    if line not in data_dict.keys():
        print("%s not in keys" % line)
        desc = input("input desc for %s" % line)
        note = input("input desc for %s" % line)
    else:
        desc = data_dict[line]['desc']
        note = data_dict[line]['note']
    this_file.write("%s,%s,%s,%s\n" % (index+1,line,desc,note))

this_file.seek(0)
data = pda.read_csv(this_file)
data.to_excel("format.xlsx",index=False)