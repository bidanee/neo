# import my_yt_tran
# import my_text_sum
# import streamlit as st
# import openai
# import os
# import tiktoken
# import textwrap
# import deepl
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

# def calc_token_num(text, model="gpt-3.5-turbo"):
#   enc= tiktoken.encoding_for_model(model)
#   encoded_text = enc.encode(text)
#   token_num = len(encoded_text)
  
#   return token_num

# def divide_text(text, token_num):
#   req_max_token = 2000
  
#   divide_num = int(token_num / req_max_token) + 1
#   divide_char_num = int(len(text) / divide_num)
#   divide_width = divide_char_num + 20
  
#   divide_text_list = textwrap.wrap(text, width=divide_width)
  
#   return divide_num, divide_text_list

# def summarize_youtube_video(video_url, selected_lang, trans_method):
#   if selected_lang == '영어': 
#     lang = 'en'
#   else:
#     lang = 'ko'
    
#   st.video(video_url, format='video/mp4')
  
#   video_info = my_yt_tran.get_youtube_video_info(video_url)
#   yt_title = video_info['title']
#   yt_duration = video_info['duration']
  
#   st.write(f'[제목] {yt_title}, [길이(분:초)] {yt_duration}')
  
#   try:
#     yt_transcript = my_yt_tran.get_transcript_from_youtube(video_url, lang)
#   except NoTranscriptFound:
#     st.error('자막을 찾을 수 없습니다. 다른 영상으로 시도해주세요.')
#     return
#   except TranscriptsDisabled:
#     st.error('이 동영상의 자막이 비활성화되어 있습니다.')
#     return
#   except Exception as e:
#     st.error(f'자막을 가져오는 중 오류가 발생했습니다. : {str(e)}')
#     return
  
#   token_num = calc_token_num(yt_transcript)
  
#   div_num, divide_yt_transcripts = divide_text(yt_transcript, token_num)
  
#   st.write('유튜브 동영상 내용 요약 중입니다. 잠시 기다려 주세요...')

#   summaries = []
  
#   for divide_yt_transcript in divide_yt_transcripts:
#     summary = my_text_sum.summarize_text(divide_yt_transcript, lang)
#     summaries.append(summary)
    
#   _, final_summary = my_text_sum.summariz_text_final(summaries, lang)
  
#   if selected_lang == '영어' :
#     shorten_num = 200
#   else:
#     shorten_num =120
    
#   shorten_final_summary = textwrap.shorten(final_summary, widhth=shorten_num, placeholder=' [...이하 생략...] ')
#   st.write('- 자막 요약(축약) : ', shorten_final_summary)
  
#   if selected_lang =='영어':
#     if trans_method =='OpenAI':
#       trans_result = my_text_sum.translate_english_to_korean_using_openAI(final_summary)
#     elif trans_method == 'DeepL':
#       trans_result = my_text_sum.translate_english_to_korean_using_deepL(final_summary)
      
#     shorten_final_summary = textwrap.shorten(trans_result, width=shorten_num, placeholder=' [...이하 생략...] ')
#     st.write('- 한국어 요약(축약) : ', shorten_final_summary)
    
  
# #  ------------------ Callback 함수 ------------------

# def button_callback():
#   st.session_state['input'] = ''

# #  ------------------ sidebar 구성 ------------------
# st.sidebar.title('요약 설정')
# url_text = st.sidebar.text_input("요약을 위한 동영상 URL을 입력해주세요.", key='input')

# clicked_for_clear = st.sidebar.button('URL 입력 내용 지우기', on_click=button_callback)

# yt_lang = st.sidebar.radio('유튜브 동영상 언어 선택', ['한국어', '영어'], index=1, horizontal=True)

# if yt_lang == '영어':
#   trans_method = st.sidebar.radio('번역 방법 선택', ['OpenAI', 'DeepL'], index=1, horizontal=True)
# else:
#   trans_method = ''

# clicked_for_sum = st.sidebar.button('동영상 내용 요약' )

# #  ------------------ Main View 구성 ------------------
# st.title('유튜브 동영상 내용 요약')

# if url_text and clicked_for_sum:
#   yt_video_url = url_text.strip()
#   summarize_youtube_video(yt_video_url, yt_lang, trans_method)


# ##------------------------------ 인철쓰 코드 ------------------------------##

# import my_yt_tran
# import my_text_sum
# import streamlit as st
# import openai 
# import os
# import tiktoken
# import textwrap
# import deepl
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

# def calc_token_num(text, model="gpt-3.5-turbo"):
#     enc = tiktoken.encoding_for_model(model)
#     encoded_text = enc.encode(text)
#     token_num = len(encoded_text)

#     return token_num

# def divide_text(text, token_num):
#     req_max_token = 2000

#     divide_num = int(token_num / req_max_token) + 1
#     divide_char_num = int(len(text) / divide_num)
#     divide_width = divide_char_num + 20

#     divide_text_list = textwrap.wrap(text, width=divide_width)

#     return divide_num, divide_text_list

# def summarize_youtube_video(video_url, selected_lang, trans_method):
#     if selected_lang == '영어':
#         lang = 'en'
#     else:
#         lang = 'ko'
    
#     st.video (video_url, format='video/mp4')

#     video_info = my_yt_tran.get_youtube_video_info(video_url)
#     yt_title = video_info['title']
#     yt_duration = video_info['duration']

#     st.write(f'[제목] {yt_title}, [길이(분:초)] {yt_duration}')

#     try:
#         yt_transcipt = my_yt_tran.get_transcript_from_youtube(video_url, lang)
#     except NoTranscriptFound:
#         st.error('자막을 찾을 수 없습니다. 다른 동영상을 시도해주세요.')
#         return
#     except TranscriptsDisabled: 
#         st.error('이 동영상의 자막이 비활성화되어 있습니다..')
#         return
#     except Exception as e:
#         st.error(f'자막을 가져오는 중 오류가 발생했습니다. : {str(e)}')
#         return
    
#     token_num = calc_token_num(yt_transcipt)
    
#     div_num, divide_yt_transcipts = divide_text(yt_transcipt, token_num)

#     st.write('유튜브 동영상 내용 요약 중입니다. 잠시만 기다려 주세요...')

#     summries = []

#     for divide_yt_transcipt in divide_yt_transcipts:
#         summary = my_text_sum.summarize_text(divide_yt_transcipt, lang)
#         summries.append(summary)

    
#     _, final_summary = my_text_sum.summariz_text_final(summries, lang)

#     if selected_lang == '영어':
#         shorten_num = 200
#     else:
#         shorten_num = 120

#     shorten_final_summary = textwrap.shorten(final_summary, width=shorten_num, placeholder=' [...이하 생략...]')
#     st.write('- 자막 요약(축약) : ', shorten_final_summary)

#     if selected_lang == '영어':
#         if trans_method == 'OpenAI':
#             trans_result = my_text_sum.translate_english_to_korean_using_openAI(final_summary)
#         elif trans_method == 'DeepL':
#             trans_result = my_text_sum.translate_english_to_korean_using_deepL(final_summary)

#         shorten_final_summary = textwrap.shorten(trans_result, width=shorten_num, placeholder=' [...이하 생략...]')
#         st.write('- 한국어 요약(축약) : ', shorten_final_summary)

# # ------------------ Callback 함수 ---------------------- #
# def button_callback():
#     st.session_state['input'] = ''

# # ------------------ sidebar 구성 ---------------------- #
# st.sidebar.title('요약 설정')
# url_text = st.sidebar.text_input("요약을 위한 동영상 URL를 입력해주세요.", key='input')

# clicked_for_clear = st.sidebar.button('URL 입력 내용 지우기', on_click=button_callback)

# yt_lang = st.sidebar.radio('유튜브 동영상 언어 선택', ['한국어', '영어'], index=1, horizontal=True)

# if yt_lang == '영어':
#     trans_method = st.sidebar.radio('번역 방법 선택', ['OpenAI', 'DeepL'], index=1, horizontal=True)
# else:
#     trans_method = ''

# clicked_for_sum = st.sidebar.button('동영상 내용 요약')

# # ------------------ Main View 구성 ---------------------- #
# st.title('유튜브 동영상 내용 요약')

# if url_text and clicked_for_sum:
#     yt_video_url = url_text.strip()
#     summarize_youtube_video(yt_video_url, yt_lang, trans_method)


import my_yt_tran  # 유튜브 동영상 정보와 자막을 가져오기 위한 모듈 임포트
import my_text_sum # 텍스트를 요약하기 위한 모듈
import streamlit as st
import openai
import os
import tiktoken
import textwrap
import deepl
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

# 텍스트의 토큰 수를 계산하는 함수(모델: "gpt-3.5-turbo")
def calc_token_num(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    encoded_list = enc.encode(text) # 텍스트 인코딩해 인코딩 리스트 생성
    token_num = len(encoded_list)    # 인코딩 리스트의 길이로 토큰 개수 계산
    
    return token_num

# 토큰에 따라 텍스트를 나눠 분할하는 함수
def divide_text(text, token_num):
    req_max_token = 2000 # 응답을 고려해 설정한 최대 요청 토큰
    
    divide_num = int(token_num / req_max_token) + 1 # 나눌 계수를 계산
    divide_char_num = int(len(text) / divide_num) # 나눌 문자 개수 
    divide_width = divide_char_num + 20 # wrap() 함수로 텍스트 나눌 때 여유분 고려해 20 더함

    divided_text_list = textwrap.wrap(text, width=divide_width)
    
    return divide_num, divided_text_list

# 유튜브 동영상을 요약하는 함수
def summarize_youtube_video(video_url, selected_lang, trans_method):
    
    if selected_lang == '영어':
        lang = 'en' 
    else:
        lang = 'ko' 
    
    # 유튜브 동영상 플레이
    st.video(video_url, format='video/mp4') # st.video(video_url) 도 동일

    # 유튜브 동영상 제목 가져오기
    _, yt_title, _, _, yt_duration = my_yt_tran.get_youtube_video_info(video_url)
    st.write(f"[제목] {yt_title}, [길이(분:초)] {yt_duration}") # 제목 및 상영 시간출력
    
    # 유튜브 동영상 자막 가져오기
    try:
        yt_transcript = my_yt_tran.get_transcript_from_youtube(video_url, lang)
    except NoTranscriptFound:
        st.error("자막을 찾을 수 없습니다. 다른 동영상을 시도해 주세요.")
        return
    except TranscriptsDisabled:
        st.error("이 동영상의 자막이 비활성화되어 있습니다.")
        return
    except Exception as e:
        st.error(f"자막을 가져오는 중 오류가 발생했습니다: {str(e)}")
        return

    # 자막 텍스트의 토큰 수 계산
    token_num = calc_token_num(yt_transcript)
    
    # 자막 텍스트를 분할해 리스트 생성
    div_num, divided_yt_transcripts = divide_text(yt_transcript, token_num)

    st.write("유튜브 동영상 내용 요약 중입니다. 잠시만 기다려 주세요.") 
    
    # 분할 자막의 요약 생성
    summaries = []
    for divided_yt_transcript in divided_yt_transcripts:
        summary = my_text_sum.summarize_text(divided_yt_transcript, lang) # 텍스트 요약
        summaries.append(summary)
        
    # 분할 자막의 요약을 다시 요약     
    _, final_summary = my_text_sum.summarize_text_final(summaries, lang)

    if selected_lang == '영어':
        shorten_num = 200 
    else:
        shorten_num = 120 
        
    shorten_final_summary = textwrap.shorten(final_summary, width=shorten_num, placeholder=' [..이하 생략..]')
    st.write("- 자막 요약(축약):", shorten_final_summary) # 최종 요약문 출력 (축약)
    # st.write("- 자막 요약:", final_summary) # 최종 요약문 출력

    if selected_lang == '영어': 
        if trans_method == 'OpenAI':
            trans_result = my_text_sum.translate_english_to_korean_using_openAI(final_summary)
        elif trans_method == 'DeepL':
            trans_result = my_text_sum.translate_english_to_korean_using_deepL(final_summary)

        shorten_trans_result = textwrap.shorten(trans_result, width=120, placeholder=' [..이하 생략..]')
        st.write("- 한국어 요약(축약):", shorten_trans_result) # 한국어 번역문 출력 (축약)
        # st.write("- 한국어 요약:", trans_result) # 한국어 번역문 출력
        
# ------------------- 콜백 함수 --------------------
def button_callback():
    st.session_state['input'] = ""
    
# ------------- 사이드바 화면 구성 --------------------------  
st.sidebar.title("요약 설정 ")
url_text = st.sidebar.text_input("유튜브 동영상 URL을 입력하세요.", key="input")

clicked_for_clear = st.sidebar.button('URL 입력 내용 지우기', on_click=button_callback)

yt_lang = st.sidebar.radio('유튜브 동영상 언어 선택', ['한국어', '영어'], index=1, horizontal=True)
    
if yt_lang == '영어':
    trans_method = st.sidebar.radio('번역 방법 선택', ['OpenAI', 'DeepL'], index=1, horizontal=True)
else:
    trans_method = ""

clicked_for_sum = st.sidebar.button('동영상 내용 요약')

# ------------- 메인 화면 구성 --------------------------     
st.title("유튜브 동영상 요약")

# 텍스트 입력이 있으면 수행
if url_text and clicked_for_sum: 
    yt_video_url = url_text.strip()
    summarize_youtube_video(yt_video_url, yt_lang, trans_method)