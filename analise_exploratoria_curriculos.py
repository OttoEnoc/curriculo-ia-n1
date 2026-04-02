"""
Projeto: Sistema Inteligente para Geração Automática de Currículos em PDF com Uso de IA
Disciplina: Inteligência Artificial – 7ºN CC – Noite
Instituição: Universidade Presbiteriana Mackenzie

Integrantes:
- Otto Enoc Hermano Smeland de Oliveira – RA 10402128
- Eduardo Figueira Losco – RA 10416650

Síntese do conteúdo:
Este arquivo realiza a leitura do dataset de currículos em formato JSON e executa
uma análise exploratória inicial, incluindo quantidade de registros, distribuição
por senioridade, frequência de habilidades e verificação de consistência dos campos.

Histórico de alterações:
- 02/04/2026 – Eduardo Figueira Losco – Criação da estrutura inicial do arquivo.
- 02/04/2026 – Otto Enoc Hermano Smeland de Oliveira – Inclusão das métricas e organização da análise.
"""

import json
from collections import Counter

with open("../dataset/curriculos_dataset.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print("Quantidade de currículos:", len(dados))

senioridades = [item.get("senioridade", "não informado") for item in dados]
print("Distribuição por senioridade:")
print(Counter(senioridades))

habilidades = []
for item in dados:
    for hab in item.get("habilidades", []):
        habilidades.append(hab.lower())

print("Habilidades mais frequentes:")
print(Counter(habilidades).most_common(10))

campos_obrigatorios = ["nome", "email", "telefone", "resumo_profissional", "experiencias", "formacao", "habilidades", "idiomas"]
faltantes = 0

for item in dados:
    for campo in campos_obrigatorios:
        if campo not in item:
            faltantes += 1

print("Quantidade total de campos obrigatórios ausentes:", faltantes)
