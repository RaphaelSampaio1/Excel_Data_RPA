import random
import csv

paises = ["Brasil", "Portugal", "Angola"]
generos = ["Masculino", "Feminino"]

nomes_br = ["João Silva", "Maria Santos", "Pedro Costa", "Ana Oliveira", "Carlos Souza"]
nomes_pt = ["Miguel Ferreira", "Sofia Rodrigues", "Tiago Martins", "Cláudia Pereira", "Ricardo Lopes"]
nomes_ao = ["Manuel António", "Teresa João", "Francisco Pedro", "Isabel Maria", "José Paulo"]

def gerar_dados():
    dados = []
    for i in range(20):
        pais = random.choice(paises)
        
        if pais == "Brasil":
            nome = random.choice(nomes_br)
            ddi = "+55"
        elif pais == "Portugal":
            nome = random.choice(nomes_pt)
            ddi = "+351"
        else:
            nome = random.choice(nomes_ao)
            ddi = "+244"
        
        genero = random.choice(generos)
        email = f"{nome.lower().replace(' ', '.')}@email.com"
        telefone = f"{ddi} {random.randint(900000000, 999999999)}"
        
        dados.append({
            "Nome": nome,
            "Email": email,
            "Telefone": telefone,
            "Gênero": genero,
            "Nacionalidade": pais
        })
    
    return dados

# Salvar em CSV
dados = gerar_dados()

with open('dados.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Nome", "Email", "Telefone", "Gênero", "Nacionalidade"])
    writer.writeheader()
    writer.writerows(dados)

print("Arquivo dados.csv gerado com sucesso!")