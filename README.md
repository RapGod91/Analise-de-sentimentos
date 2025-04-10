# Análise de Sentimentos em Avaliações e Suporte Técnico

Este projeto é um estudo sobre **análise de sentimentos aplicada a textos de avaliações, manifestações e interações em chats de suporte técnico** de **provedores de internet**.

## 🎯 Objetivo

O objetivo deste estudo é identificar e classificar automaticamente sentimentos expressos em mensagens de clientes, com foco em:

- Avaliações de atendimento e serviço
- Reclamações ou manifestações registradas
- Conversas em chats de suporte técnico

Essa análise pode ajudar empresas a:

- Monitorar a satisfação do cliente em tempo real
- Detectar falhas de atendimento
- Direcionar melhorias nos serviços prestados

## 🧠 Tecnologias Utilizadas

- [Transformers 🤗](https://huggingface.co/transformers/) — para análise de sentimentos
- Modelo utilizado: `nlptown/bert-base-multilingual-uncased-sentiment` (compatível com textos em português)
- Python 3
- Bibliotecas:
  - `transformers`
  - `torch`
  - `csv`

## 📝 Como Funciona

1. O script lê um arquivo `.txt` contendo uma frase por linha.
2. Cada linha é analisada por um modelo de linguagem treinado em múltiplos idiomas.
3. O sentimento é classificado em três categorias:
   - **POSITIVO**
   - **NEUTRO**
   - **NEGATIVO**
4. Os resultados são salvos em um arquivo `.csv` com separador `|`, contendo:
   - A frase original
   - O sentimento detectado
   - A confiança da classificação

## 📁 Exemplo de saída `.csv`

