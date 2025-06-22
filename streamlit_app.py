import streamlit as st
import pandas as pd
import os
import openai
from openai import OpenAI

# API 키 불러오기
openai_api_key = st.secrets["api_keys"]["openai_api_key"]
os.environ["OPENAI_API_KEY"] = openai_api_key

client = OpenAI(api_key = openai_api_key,)

from gpt_structure import dd_generate_gpt4_basic
from knowledge_structure import *

st.set_page_config(
    page_title="과거의 나 (Survey Items)",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items= {
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': '과거의 나 실험용 플랫폼',
    }
)

# @st.cache_data(ttl=30)
# def load_data(file_name):
#   df = pd.read_csv(file_name)
#   return df

maindf = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSe0WBLitUeLd1ABmi0gqAG3y8TkeI3ef0OB6eu3frGWBr5HJaFMRI1co7mdo8uRXOflurnxpceUhui/pub?gid=807022632&single=true&output=csv")

streamlit_style = """
			<style>
			@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

			html, body, [class*="css"],g {
			  font-family: Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
      }
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

st.title('과거의 나 (Survey Items)')
st.markdown('---')

with st.form('prompt_selector'):
  user_name = st.radio(
            "Select User Name 👉",
            key="user_name",
            options = maindf['참여자 코드를 입력해 주세요.'].unique()
  )

  submit = st.form_submit_button('Submit')

if submit:
  main_test = maindf[maindf['참여자 코드를 입력해 주세요.'] == user_name]
 
  with st.spinner('Wait for it...'):
    demo = demo_generate(main_test)
    bfi = bfi_generate(main_test, client)
    pvq = pvq_generate(main_test, client)
    past_profile = past_profile_generate(main_test)
    love_hate = love_hate_generate(main_test)
    daily_life = daily_life_generate(main_test)
    past_letter = past_letter_generate(main_test)
    
 
    knowledge = demo
    knowledge += "\n"
    knowledge += bfi
    knowledge += "\n"
    knowledge += pvq
    knowledge += "\n"	
    knowledge += past_profile
    knowledge += "\n"
    knowledge += love_hate
    knowledge += "\n"
    knowledge += daily_life
    knowledge += "\n"
    knowledge += past_letter
    #knowledge += "\n"
    
    

    st.subheader("Knowledge")
    st.write(knowledge)