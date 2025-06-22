from pvq_scoring import *
from bfi_scoring import *
from gpt_structure import pvq_summary_gpt4, bfi_summary_gpt4

def past_profile_generate(main_test):
  lib_file = './data/prompt_template/past_profile.txt'
  f = open(lib_file, "r")
  past_profile_template = f.read()
  f.close()
  past_profile = past_profile_template(
    MAIN_DIFFICULTIES = main_test.iloc[0,62],
    BIGGEST_WORRY = main_test.iloc[0,63],
    EMOTIONAL_MENTAL_STATE = main_test.iloc[0,64],
    DAILY_LIFE_ENVIRONMENT = main_test.iloc[0,65],
    FAMILY_RELATIONSHIPS = main_test.iloc[0,66],
    SUPPORT_OR_COPING = main_test.iloc[0,67],
    INTERESTS_HOBBIES_EFFORTS = main_test.iloc[0,68],
  )
  return past_profile
 
def daily_life_generate(main_test):
  lib_file = './data/prompt_template/daily_life.txt'
  f = open(lib_file, "r")
  daily_life_template = f.read()
  f.close()
  daily_life = daily_life_template.format(
    WEEKDAYS = main_test.iloc[0,75],
    WEEKENDS = main_test.iloc[0,76],
  )
  return daily_life

def past_letter_generate(main_test):
  lib_file = './data/prompt_template/past_letter.txt'
  f = open(lib_file, "r")
  past_letter_template = f.read()
  f.close()
  past_letter = past_letter_template.format(
    LETTER = main_test.iloc[0,77],
  )
  return past_letter


def love_hate_generate(main_test):
  lib_file = './data/prompt_template/love_hate.txt'
  f = open(lib_file, "r")
  love_hate_template = f.read()
  f.close()
  love_hate = love_hate_template.format(
    LOVE1 = main_test.iloc[0,69],
    LOVE2 = main_test.iloc[0,70],
    LOVE3 = main_test.iloc[0,71],
    HATE1 = main_test.iloc[0,72],
    HATE2 = main_test.iloc[0,73],
    HATE3 = main_test.iloc[0,74],
  )
  return love_hate


def demo_generate(main_test):
  lib_file = './data/prompt_template/demo.txt'
  f = open(lib_file, "r")
  demo_template = f.read()
  f.close()
  demo = demo_template.format(
    AGE = 2025 - main_test.iloc[0,2],
    DIF_START = main_test.iloc[0,3],
    DIF_LENGTH = main_test.iloc[0,4],
    SEX = main_test.iloc[0,5],
    DIS_STATUS = main_test.iloc[0,6],
    DIS_TYPE = main_test.iloc[0,7],
    DIS_IMPACT = main_test.iloc[0,8],
    NAT = main_test.iloc[0,9],
    RES = main_test.iloc[0,10],
    EDU = main_test.iloc[0,11],
    MAIN_ACT = main_test.iloc[0,12],
    SCH_LEVEL = main_test.iloc[0,13],
    ACT_DETAIL = main_test.iloc[0,14],
    MAIN_TASK = main_test.iloc[0,15],
    SAT_INC = main_test.iloc[0,16],
    PER_CLASS = main_test.iloc[0,17],
    LIV = main_test.iloc[0,18],
    SIB = main_test.iloc[0,19],
    POL_VIEW = main_test.iloc[0,20],
    REL = main_test.iloc[0,21],
  )
  return demo

def bfi_generate(main_test, client):
  bfi_intro = '''

**[Big 5 Personality Traits in 2025]**
The following section presents an overview of the person's personality within five key domains, showcasing their traits spectrum and the extent of their qualities in each area. Each domain comprises several facets that provide deeper insights into their unique personality traits.

'''
  new_column_names = [f'D1PB-{i}' for i in range(1, 31)]
  bfi_raw = main_test.iloc[:, 22:52]
  bfi_raw.columns = new_column_names
  bfi_1st = bfi_calculate_scores(bfi_raw)
  bfi_summary = bfi_summary_gpt4(bfi_1st, client)
  bfi_summary_final = bfi_intro + bfi_summary
  return bfi_summary_final

def pvq_generate(main_test, client):
  pvq_intro = '''

**[Life-guiding Principles in 2025]**
The information provided below is the values that reflect the relative importance this person places on different aspects of life, guiding their decisions, actions, and perspectives. These values are fundamental components of their personality and play a crucial role in shaping who this person is.

'''
  new_column_names = [f'D2LP-{i}' for i in range(1, 11)]
  pvq_raw = main_test.iloc[:, 52:62]
  pvq_raw.columns = new_column_names
  pvq_1st = generate_pvq_prompt(pvq_raw)
  pvq_summary = pvq_summary_gpt4(pvq_1st, client)
  pvq_summary_final = pvq_intro + pvq_summary
  return pvq_summary_final

