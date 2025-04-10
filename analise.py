from transformers import pipeline
import csv

# Carrega o modelo multilíngue
analisador = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Caminhos dos arquivos
arquivo_txt = "reclame.txt"
arquivo_csv = "resultado_sentimentos.csv"

# Lista para guardar os resultados
resultados = []

# Lê as linhas do .txt
with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Analisa cada linha
for linha in linhas:
    frase = linha.strip()
    if frase:
        analise = analisador(frase)[0]
        estrelas = int(analise['label'][0])
        score = analise['score']

        # Classificação do sentimento
        if estrelas <= 2:
            sentimento = "NEGATIVO"
        elif estrelas == 3:
            sentimento = "NEUTRO"
        else:
            sentimento = "POSITIVO"

        resultados.append([frase, sentimento, round(score, 2)])

# Salva no .csv com separador |
with open(arquivo_csv, "w", newline="", encoding="utf-8") as csvfile:
    escritor = csv.writer(csvfile, delimiter="|")
    escritor.writerow(["frase", "sentimento", "confianca"])
    escritor.writerows(resultados)

print(f"✅ Arquivo '{arquivo_csv}' gerado com sucesso (usando separador '|')!")
