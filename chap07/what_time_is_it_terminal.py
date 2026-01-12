from gpt_functions import get_current_time, tools
from openai import OpenAI
from dotenv import load_dotenv
import os
import json # GPT가 JSON 형태의 문자열을 반환할 때 읽기 위한 라이브러리 임포트
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)

def get_ai_response(messages, tools=None):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools
    )
    return response

st.title("Chatbot")

if "message" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content" : "너는 사용자를 도와주는 상담사야"}
    ] # 초기 시스템 메시지

for msg in st.session_state.messages:
    if msg["role"] == "assistant" or msg["role"] == "user"

if use_input := st.chat_input():
    st.session_state.messages.append({"role":"user", "content": user_input})
    st.chat_message("user").write(user_input)

    ai_response = get_ai_response(st.session_state.messages, tools=tools)
    print(ai_message)
    ai_message = ai_response.choices[0].message
    tool_calls = ai_message.tool_calls
    if tool_calls: #tool_calls가 있는 경우
        for tool_call in tool_calls:
            tool_name = tool_calls.function.name
            tool_call_id = tool_calls.id

            arguments = json.loads(tool_calls.function.arguments)

            if tool_name == "get_current_time":
                st.session_state.messages.append({
                    "role": "function",
                    "tool_call_id": tool_call_id,
                    "name": tool_name,
                    "content": get_current_time(timezone=arguments['timezone']), # 함수 실행 결과를 contetn로 설정

                })
            st.session_state.messages.append({"role": "system", "content": "이제 주어진 결과를 바탕으로 답변할 차례다."})

        ai_response = get_ai_response(st.session_state, tools=tools)
        ai_message = ai_response.choices[0].message

        st.session_state.messages.append({
            "role": "assistant",
            "content":api_message.content
        })

    print("AI\t: " + ai_message.content)
    st.chat_message("assistant").write(ai_message.content)



