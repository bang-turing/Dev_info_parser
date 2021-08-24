# Dev Info extractor
Interface for extract developer information from Turing database

User can paste code to jupyter in colab 

```
!git clone https://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@github.com/bang-turing/Dev_info_parser
%cd Dev_info_parser

from parsers import devinfo
from utils import querygbq
from sql_source import dev_resumes

df_resume = querygbq(dev_resumes)
a = devinfo(df_resume, 30)
```
