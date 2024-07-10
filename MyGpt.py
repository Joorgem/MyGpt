import streamlit as st
import uuid
from utils_openai import retorna_resposta_modelo
from utils_files import *

#INICIALIZAÇÃO =======================================

def inicializacao():
    if 'mensagens' not in st.session_state:
        st.session_state.mensagens = []
    if 'conversa_atual' not in st.session_state:
        st.session_state.conversa_atual = ''
    if 'modelo' not in st.session_state:
        st.session_state.modelo = 'gpt-3.5-turbo'
    if 'api_key' not in st.session_state:
        st.session_state.api_key = le_chave()
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())


# PÁGINA PRINCIPAL ====================================

def pagina_principal():
    mensagens = ler_mensagens(st.session_state.mensagens)

    st.header('🤖 My GPT', divider=True)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])

    prompt = st.chat_input('Fale com o chat')
    if prompt:
        if st.session_state['api_key'] == '':
            st.error('Adicione uma chave de API na aba de configurações')
        else:
            nova_mensagem = {'role': 'user', 'content': prompt}
            chat = st.chat_message(nova_mensagem['role'])
            chat.markdown(nova_mensagem['content'])
            mensagens.append(nova_mensagem)

            chat = st.chat_message('assistant')
            placeholder = chat.empty()
            resposta_completa = ''

            respostas = retorna_resposta_modelo(mensagens,
                                                st.session_state['api_key'],
                                                model=st.session_state['modelo'],
                                                stream=True)
            for resposta in respostas:
                for choice in resposta.choices:
                    if hasattr(choice.delta, 'content') and choice.delta.content is not None:
                        resposta_completa += choice.delta.content
                        placeholder.markdown(resposta_completa + "▌")

            placeholder.markdown(resposta_completa)

            nova_mensagem = {'role': 'assistant', 'content': resposta_completa}
            mensagens.append(nova_mensagem)

            st.session_state.mensagens = mensagens
            salvar_mensagens(mensagens)

#TABS =================================================

def tab_conversas(tab):
    tab.button('➕ Nova Conversa',
               on_click=seleciona_conversa,
               args=('',),
               use_container_width=True)
    tab.markdown('')
    conversas = listar_conversas()
    for nome_arquivo in conversas:
        nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
        if len(nome_mensagem) == 30:
            nome_mensagem += '...'
        tab.button(nome_mensagem,
                   on_click=seleciona_conversa,
                   args=(nome_arquivo,),
                   disabled=nome_arquivo == st.session_state['conversa_atual'],
                   use_container_width=True)

def seleciona_conversa(nome_arquivo):
    if nome_arquivo == '':
        st.session_state.mensagens = []
    else:
        mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo)
        st.session_state.mensagens = mensagem
        st.session_state['conversa_atual'] = nome_arquivo

def tab_configuracoes(tab):
    modelo_escolhido = tab.selectbox('Selecione o modelo',
                                     ['gpt-3.5-turbo', 'gpt-4'])
    st.session_state['modelo'] = modelo_escolhido

    chave = tab.text_input('Adicione sua api key', value=st.session_state['api_key'])
    if chave != st.session_state['api_key']:
        st.session_state['api_key'] = chave
        salva_chave(chave)
        tab.success('Chave salva com sucesso')

# MAIN =================================================

def main():
    inicializacao()
    pagina_principal()
    tab1, tab2 = st.sidebar.tabs(['Conversas', 'Configurações'])
    tab_conversas(tab1)
    tab_configuracoes(tab2)

if __name__ == '__main__':
    main()
