from llama_index import LlamaIndex

# Exemplo de dados para o chatbot
faq = [
    {"pergunta": "Como resetar minha senha?", "resposta": "Você pode resetar sua senha na página de 'Esqueci minha senha'."},
    {"pergunta": "Como atualizar meu endereço de email?", "resposta": "Atualize seu email nas configurações de perfil."},
    # ... mais perguntas e respostas
]

# Criar e preencher o LlamaIndex com as perguntas
index = LlamaIndex()
for item in faq:
    index.add(item["pergunta"])

# Função para encontrar a resposta mais relevante
def obter_resposta(pergunta_usuario):
    perguntas_similares = index.search(pergunta_usuario)
    if perguntas_similares:
        pergunta_similar = perguntas_similares[0]
        for item in faq:
            if item["pergunta"] == pergunta_similar:
                return item["resposta"]
    return "Desculpe, não consegui encontrar uma resposta para sua pergunta."

# Exemplo de interação com o usuário
pergunta_usuario = "Como mudo meu email?"
resposta = obter_resposta(pergunta_usuario)
print(resposta)
