import re
from pathlib import Path
import pickle
from unidecode import unidecode
import streamlit as st

PASTA_CONFIGURACOES = Path(__file__).parent / 'configuracoes'
PASTA_CONFIGURACOES.mkdir(existok=True)
PASTA_MENSAGENS = Path(__file__).parent / 'mensagens'
PASTA_MENSAGENS.mkdir(existok=True)
CACHE_DESCONVERTE = {}

def converte_nome_mensagem(nome_mensagem):
    nome_arquivo = unidecode(nome_mensagem)
    nome_arquivo = re.sub(r'\W+', '', nome_arquivo).lower()
    return nome_arquivo

def desconverte_nome_mensagem(nome_arquivo):
    if nome_arquivo not in CACHE_DESCONVERTE:
        caminho_arquivo = PASTA_MENSAGENS / nome_arquivo
        if caminho_arquivo.is_file():
            try:
                nome_mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo, key='nome_mensagem')
                CACHE_DESCONVERTE[nome_arquivo] = nome_mensagem
            except FileNotFoundError:
                return ""
        else:
            return ""
    return CACHE_DESCONVERTE[nome_arquivo]

def retorna_nome_mensagem(mensagens):
    nome_mensagem = ''
    for mensagem in mensagens:
        if mensagem['role'] == 'user':
            nome_mensagem = mensagem['content'][:30]
            break
    return nome_mensagem

def salvar_mensagens(mensagens):
    if len(mensagens) == 0:
        return False
    nome_mensagem = retorna_nome_mensagem(mensagens)
    nome_arquivo = converte_nome_mensagem(nome_mensagem)
    arquivo_salvar = {'nome_mensagem': nome_mensagem,
                      'nome_arquivo': nome_arquivo,
                      'mensagem': mensagens}
    with open(PASTA_MENSAGENS / nome_arquivo, 'wb') as f:
        pickle.dump(arquivo_salvar, f)

def ler_mensagem_por_nome_arquivo(nome_arquivo, key='mensagem'):
    caminho_arquivo = PASTA_MENSAGENS / nome_arquivo
    if caminho_arquivo.is_file():
        with open(caminho_arquivo, 'rb') as f:
            mensagens = pickle.load(f)
        return mensagens[key]
    else:
        raise FileNotFoundError(f"{nome_arquivo} não é um arquivo válido.")

def ler_mensagens(mensagens, key='mensagem'):
    if len(mensagens) == 0:
        return []
    nome_mensagem = retorna_nome_mensagem(mensagens)
    nome_arquivo = converte_nome_mensagem(nome_mensagem)
    with open(PASTA_MENSAGENS / nome_arquivo, 'rb') as f:
        mensagens = pickle.load(f)
    return mensagens[key]

def listar_conversas():
    conversas = list(PASTA_MENSAGENS.glob('*'))
    conversas = sorted(conversas, key=lambda item: item.stat().st_mtime_ns, reverse=True)
    return [c.stem for c in conversas]

def salva_chave(chave):
    with open(PASTA_CONFIGURACOES / 'chave', 'wb') as f:
        pickle.dump(chave, f)

def le_chave():
    if (PASTA_CONFIGURACOES / 'chave').exists():
        with open(PASTA_CONFIGURACOES / 'chave', 'rb') as f:
            return pickle.load(f)
    else:
        return ''
