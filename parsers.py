import json
import pandas as pd
import urllib.request

from utils import querygbq, clean_duplicates, gen_dict_list, update_dict_list, extract_resume_data
from sql_source import dev_mcq, dev_ti, dev_resumes


def devinfo(df_resume, break_point=1e15, pre_load=None):
    df_resume = clean_duplicates(df_resume)
    all_dev = None
    
    for i, (idu, res) in enumerate(zip(df_resume["user_id"], df_resume["url"])):
        with urllib.request.urlopen(res) as url:
            data = url.read()
            resume = json.loads(data.decode())
        if "ResumeParserData" in resume:
            dev_info = extract_resume_data(resume)
            dev_info["dev_id"] = idu
            if all_dev is None:
                all_dev = gen_dict_list(dev_info.keys())
            all_dev = update_dict_list(dev_info, all_dev)
        else:
            pass
        if i > break_point:
            print(i)
            break
    return pd.DataFrame(all_dev)

    
if __name__ == '__main__':
    df = devinfo(None, 30)
    print(df)