from openai import OpenAI, OpenAIError
import streamlit as st

def retorna_resposta_modelo(mensagens, api_key, model='gpt-3.5-turbo', temperature=0, stream=False):
    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            messages=mensagens,
            model=model,
            temperature=temperature,
            stream=stream
        )
        return response
    except OpenAIError as e:
        st.error(f"OpenAI API Error: {e}")
        return None
