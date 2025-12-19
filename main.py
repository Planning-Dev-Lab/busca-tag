import pandas as pd
from pyscript import document

# Carrega e limpa os dados
df = pd.read_csv("tags.csv", encoding='latin1', sep=None, engine='python')
df['nova'] = df['nova'].astype(str).str.split(' \(').str[0].str.strip()
df['antiga'] = df['antiga'].astype(str).str.strip()

# Remove o loader e mostra o conteúdo
loader = document.getElementById("loading-overlay")
content = document.getElementById("main-content")
loader.style.display = "none"
content.classList.remove("content-hidden")

def adicionar_ao_historico(texto, tipo):
    lista = document.getElementById("listaHistorico")
    novo_item = document.createElement("div")
    novo_item.className = f"historico-item item-{tipo}"
    novo_item.innerHTML = texto
    lista.insertBefore(novo_item, lista.firstChild)
    if lista.children.length > 5:
        lista.removeChild(lista.lastChild)

def verificar_tag(event):
    if event.key == "Enter":
        tag_digitada = document.getElementById("inputTag").value.strip().upper()
        resultado_div = document.getElementById("resultado")
        if not tag_digitada: return

        busca_antiga = df[df['antiga'].str.upper() == tag_digitada]
        busca_nova = df[df['nova'].str.upper() == tag_digitada]
        resultado_div.style.display = "block"

        if not busca_antiga.empty:
            tag_nova = busca_antiga.iloc[0]['nova']
            resultado_div.className = "antiga"
            resultado_div.innerHTML = f"TAG ANTIGA<br>Nova: {tag_nova}"
            adicionar_ao_historico(f"Antiga: {tag_digitada} → Nova: {tag_nova}", "antiga")
        elif not busca_nova.empty:
            tag_antiga = busca_nova.iloc[0]['antiga']
            resultado_div.className = "atual"
            resultado_div.innerHTML = f"TAG JÁ ATUAL<br><small>Antiga era: {tag_antiga}</small>"
            adicionar_ao_historico(f"Atual: {tag_digitada} (Antiga: {tag_antiga})", "atual")
        else:
            resultado_div.className = "erro"
            resultado_div.innerHTML = "TAG NÃO ENCONTRADA"

        document.getElementById("inputTag").value = ""