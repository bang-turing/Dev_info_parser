# Source data for multiple choice questions results
dev_mcq = '''SELECT * FROM `turing-230020.analytics_views.dev_mcq_data`'''

# Source data for technical interview results
dev_ti = '''SELECT * FROM `turing-230020.analytics_views.dev_ti_result`'''

"""
Developer general 
• Phase 1 developers = signed up but haven’t passed technical vetting yet.
• Phase 2 developers = passed technical vetting but haven’t started working with us yet (either customer or internal).
• Phase 3 developers = have started working with us. 
"""
# NOTE: This table contains all the developers that singed up(so it is phase 1, 2, 3 combine)
dev_phase1 = '''SELECT * FROM `turing-230020.analytics_views.phase1_dev_level_data`'''
# NOTE: Generate by checking any matching process is happening with this developers
dev_phase2 = '''SELECT * FROM `turing-230020.analytics_views.phase2_dev_level_data`'''

# Resume parsed of developers signed up (This is create by third party OCR service :
# First by https://www.sovren.com
# Now switch to https://www.rchilli.com due to price )
dev_resumes = '''SELECT * FROM `turing-230020.devdb_mirror.dv2_parsed_resume_link`'''

# Note : there are 2 type of resume
# We only concern about dict with "ResumeParserData"(Rchilli) key and ignore dict with "Resume"(Sovren) key

ops_data = '''SELECT * FROM turing-230020.analytics_views.Opportunities_data'''
