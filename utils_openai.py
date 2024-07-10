from openai import OpenAI

def retorna_resposta_modelo(mensagens, api_key, model='gpt-3.5-turbo', temperature=0, stream=False):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        messages=mensagens,
        model=model,
        temperature=temperature,
        stream=stream
    )
    return response
