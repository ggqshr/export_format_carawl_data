from pymongo import MongoClient
import pandas as pda
from pathlib import Path

client = MongoClient("119.23.224.186",19985)
# client.get_database("admin").authenticate("jason#619","jason#619")
name = "ZLSchool"
col = client.get_database(name).get_collection(name)

fields_list = list(filter(None,Path("./fields.txt").read_text().split("\n")))
all_data = []
for item in col.find({},{"_id":False},limit=100):
    # if item['advantage'] != '空':
    #     item['advantage'] = "_".join(item['advantage'])
    # item['job_content'] = "_".join(item['job_content']).strip()
    # item['company_address'] = "_".join(item['company_address'])
    # item['company_size'] = "_".join(item['company_size'])
    # item['company_industry'] = "_".join(item['company_industry'])
    # item['job_name'] = item['job_name'].strip()
    all_data.append(item)

dd = pda.DataFrame(all_data)
dd[fields_list].to_csv("%s.csv" % name,index=False)