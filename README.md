# Exemplo didático - API com FastAPI

Este repositório contém um exemplo simples de API em Python usando FastAPI.

A ideia é mostrar:
- como criar uma rota GET;
- como receber um parâmetro pela URL;
- como consumir uma API externa;
- como retornar dados em JSON;
- como tratar erro básico.

## Como rodar

Instale as dependências:

```bash
pip install -r requirements.txt

## Como executar o projeto

### 1. Instalar as dependências

## Como executar o projeto

No terminal, execute:

```bash
pip install -r requirements.txt

## Caso dê erro, tente executar manualmente
pip install fastapi uvicorn requests

##Com o arquivo main.py na pasta do projeto, execute:

uvicorn main:app --reload


##Se aparecer erro dizendo que uvicorn não foi encontrado, tente:
python -m uvicorn main:app --reload

##Abrir no navegador

http://127.0.0.1:8000/docs

##Se estiver usando GitHub Codespaces, abra o link gerado na porta 8000 e adicione /docs no final. Exemplo

https://seu-codespace-8000.app.github.dev/docs