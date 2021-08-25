# Dev Info extractor
Interface for extract developer information from Turing database

This repo need google authentication in order to run. 
```
!git clone https://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@github.com/bang-turing/Dev_info_parser
%cd Dev_info_parser

from parsers import devinfo
from utils import querygbq
from sql_source import dev_resumes

df_resume = querygbq(dev_resumes)
# change breakpoint to None to extract all data 
df_info = devinfo(df_resume, break_point=30)
print(df_info)
```
