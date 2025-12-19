import pandas as pd
from pyscript import document

# --- CARREGAMENTO E LIMPEZA DE DADOS ---
df = pd.read_csv("tags.csv", encoding='latin1', sep=None, engine='python')
df['nova'] = df['nova'].astype(str).str.split(' \(').str[0].str.strip()
df['antiga'] = df['antiga'].astype(str).str.strip()

# --- INTERFACE INICIAL ---
loader = document.getElementById("loading-overlay")
content = document.getElementById("main-content")
if loader:
    loader.style.display = "none"
if content:
    content.classList.remove("content-hidden")

def adicionar_ao_historico(texto, tipo):
    """Adiciona uma entrada ao topo da lista de histórico e limita a 5 itens."""
    lista = document.getElementById("listaHistorico")
    novo_item = document.createElement("div")
    novo_item.className = f"historico-item item-{tipo}"
    novo_item.innerHTML = texto
    
    if lista.firstChild:
        lista.insertBefore(novo_item, lista.firstChild)
    else:
        lista.appendChild(novo_item)
        
    if lista.children.length > 5:
        lista.removeChild(lista.lastChild)
    
    # Mostra o botão se houver itens no histórico
    btn = document.getElementById("btnLimpar")
    if btn:
        btn.style.display = "block"

def limpar_tudo(event):
    """Limpa o histórico e a div de resultado."""
    # Limpa o Histórico
    lista = document.getElementById("listaHistorico")
    lista.innerHTML = ""
    
    # Limpa e esconde o resultado
    resultado_div = document.getElementById("resultado")
    resultado_div.innerHTML = ""
    resultado_div.style.display = "none"
    
    # Esconde o próprio botão
    btn = document.getElementById("btnLimpar")
    if btn:
        btn.style.display = "none"

def verificar_tag(event):
    """Função principal disparada ao pressionar Enter."""
    if event.key == "Enter":
        tag_digitada = document.getElementById("inputTag").value.strip().upper()
        resultado_div = document.getElementById("resultado")
        
        if not tag_digitada: 
            return

        busca_antiga = df[df['antiga'].str.upper() == tag_digitada]
        busca_nova = df[df['nova'].str.upper() == tag_digitada]
        
        resultado_div.style.display = "block"

        if not busca_antiga.empty:
            tag_nova = busca_antiga.iloc[0]['nova']
            resultado_div.className = "antiga"
            resultado_div.innerHTML = f"TAG ANTIGA<br>Nova: {tag_nova}"
            adicionar_ao_historico(f"Antiga: <b>{tag_digitada}</b> → Nova: <b>{tag_nova}</b>", "antiga")

        elif not busca_nova.empty:
            valor_antiga = busca_nova.iloc[0]['antiga']
            if pd.isna(valor_antiga) or str(valor_antiga).lower() == "nan" or valor_antiga.strip() == "":
                tag_antiga_display = "não registrada"
            else:
                tag_antiga_display = valor_antiga

            resultado_div.className = "atual"
            resultado_div.innerHTML = f"TAG JÁ ATUAL<br><small>Antiga: {tag_antiga_display}</small>"
            adicionar_ao_historico(f"Atual: <b>{tag_digitada}</b> → Antiga: <b>{tag_antiga_display}</b>", "atual")

        else:
            resultado_div.className = "erro"
            resultado_div.innerHTML = "TAG NÃO ENCONTRADA"

        document.getElementById("inputTag").value = ""