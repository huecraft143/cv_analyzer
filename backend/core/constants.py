import re

CV_SAMPLE_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/cvs/Curriculum-def-booger.pdf'

# CSV paths
EN_CSV_SKILLS_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/data/skills_en.csv'
EN_CSV_JOB_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/data/occupations_en.csv'
EN_CSV_LANG_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/data/languageSkillsCollection_en.csv'

# JSON paths
EN_SKILLS_JSON_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/data/skills_en.json' 
EN_JOB_JSON_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/data/occupations_en.json' 
EN_LANG_JSON_PATH = '/Users/mattiapalano/Documents/cv_analyzer/backend/data/languageSkillsCollection_en.json'

# Regular expressions
EMAIL_RE = re.compile(r"[\w\.\-]+@[\w\-]+\.[\w\.-]+")
PHONE_RE = re.compile(r"(\+\d{1,3}\s?)?(\(?\d{2,4}\)?[\s.-]?)?\d{6,12}")