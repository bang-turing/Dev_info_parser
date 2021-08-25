import pandas as pd


def querygbq(query, project_id='turing-230020'):
    df = pd.io.gbq.read_gbq(query, project_id=project_id)
    return df


def clean_duplicates(df_data, clean_id="user_id", sort="created_date"):
    """
    Clean all the duplicates, keep the latest data
    Args:
        df_data (pd.DataFrame): Data with duplicates row
        clean_id (str): Column name for checking duplicates
        sort (str): Column name for date time(to sort)

    Returns: Clean DataFrame

    """
    df_data = df_data.sort_values(sort, ascending=False)
    df_data = df_data.drop_duplicates(subset=clean_id, keep='first')
    return df_data


def gen_dict_list(keys):
    """Init a dictionary with list of keys. Initialize all key with list structure"""
    gen_dict = dict()
    for key in keys:
        gen_dict[key] = list()
    return gen_dict


def update_dict_list(in_dict, dict_list):
    """Expand a dictionary by append all data from an input dictionary to the same keys . This will create data
    structures that can be easily convert to pandas Dataframe """
    for key in dict_list:
        dict_list[key].append(in_dict[key])
    return dict_list


def extract_resume_data(resume, idu):
    """
    Parse dev data from Rchilli data output(download from link in dv2_parsed_resume_link table)
    Args:
        resume (Dict): Rchilli resume parser output

    Returns: Dictionary of extracted data

    """
    info = dict()
    info["dev_id"] = idu
    resume = resume["ResumeParserData"]

    language_data = resume["LanguageKnown"]
    list_lang = [la["LanguageCode"] for la in language_data]

    info["Languages"] = "_".join(list_lang)
    info["NumLanguage"] = len(list_lang)

    country = resume["ResumeCountry"]
    info["Country"] = ''
    if "Country" in country:
        info["Country"] = country["Country"]

    info["Nationality"] = resume["Nationality"]
    info["FullName"] = resume["Name"]["FullName"]
    info["MaritalStatus"] = resume["MaritalStatus"]
    info["DateOfBirth"] = resume["DateOfBirth"]
    info["VisaStatus"] = resume["VisaStatus"]

    webl = resume["WebSite"]

    info["WebGit"] = 0
    info["WebStackoverflow"] = 0
    info["WebLinkedin"] = 0
    info["WebFacebook"] = 0
    info["WebTwitter"] = 0
    info["WebScholar"] = 0

    for web in webl:
        if web["Type"] == "Github":
            info["WebGit"] = 1
        elif web["Type"] == "Stackoverflow":
            info["WebStackoverflow"] = 1
        elif web["Type"] == "Linkedin":
            info["WebLinkedin"] = 1
        elif web["Type"] == "Facebook":
            info["WebFacebook"] = 1
        elif web["Type"] == "Twitter":
            info["WebTwitter"] = 1
        elif "scholar" in web["Url"]:
            info["WebScholar"] = 1

    info["Email"] = 0
    if resume["Email"][0]["EmailAddress"] != '':
        info["Email"] = 1

    info["Category"] = resume["Category"]
    info["SubCategory"] = resume["SubCategory"]

    info["CurrentEmployer"] = resume["CurrentEmployer"]

    # job name
    info["JobProfile"] = resume["JobProfile"]

    info["WorkedPeriod"] = resume["WorkedPeriod"]["TotalExperienceInYear"]

    # Gap
    info["GapPeriod"] = resume["GapPeriod"]

    info["AverageStay"] = resume["AverageStay"]

    info["LongestStay"] = resume["LongestStay"]

    info["Summary"] = resume["Summary"]

    info["ExecutiveSummary"] = resume["ExecutiveSummary"]

    # management skill
    info["ManagementSummary"] = resume["ManagementSummary"]

    info["Availability"] = resume["Availability"]

    info["Achievements"] = resume["Achievements"]
    return info

