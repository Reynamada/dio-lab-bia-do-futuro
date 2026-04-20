import os

# ========= CONFIGURAÇÕES OPENROUTER ==============
MODELO = "openai/gpt-oss-120b:free"
API_KEY = "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"

# ========= CAMINHOS DE DADOS ==============
# Ajustado para encontrar a pasta data fora da pasta src
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

CAMINHO_PERFIL = os.path.join(DATA_DIR, 'perfil_investidor.json')
CAMINHO_EDU = os.path.join(DATA_DIR, 'material_educativo.json')
CAMINHO_CSV = os.path.join(DATA_DIR, 'receitas_despesas.csv')