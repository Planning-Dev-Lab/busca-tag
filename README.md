# 🔍 Buscador de Tags - Planning Dev Lab

Ferramenta corporativa para consulta e de-para de nomenclaturas de ativos (TAGS), facilitando a transição entre sistemas legados e o novo padrão de planejamento.

## 🔗 Link de Acesso
Acesse o buscador em tempo real aqui:
👉 **[https://planning-dev-lab.github.io/busca-tag/](https://planning-dev-lab.github.io/busca-tag/)**

---

## 🚀 Funcionalidades Principais
* **Busca Inteligente**: Localiza Tags Novas a partir de Antigas e vice-versa.
* **Tratamento de Dados**: Limpeza automática de caracteres especiais e parênteses redundantes.
* **Histórico de Sessão**: Lista as últimas consultas realizadas para conferência rápida.
* **Interface Progressiva**: Exibe um sinal visual de carregamento enquanto processa o banco de dados.

## 🛠️ Tecnologias Utilizadas
* **Python (Pandas)**: Motor de busca e filtragem de dados.
* **PyScript/Pyodide**: Tecnologia que permite rodar Python direto no navegador.
* **HTML5 & CSS3**: Interface responsiva com design focado em produtividade.

## 📂 Estrutura do Repositório
* `index.html`: Interface do usuário.
* `style.css`: Estilização e animações (Loader/Spinner).
* `main.py`: Lógica de busca e manipulação do DOM via Python.
* `tags.csv`: Base de dados (deve ser mantida com as colunas `antiga` e `nova`).

## 📥 Como Atualizar as Tags
1. Exporte sua planilha de tags no formato **CSV (separado por vírgulas)**.
2. Certifique-se de que o arquivo se chama exatamente `tags.csv`.
3. Faça o upload do arquivo para a branch `develop` para testes.
4. Após validar, realize o merge para a branch `main` para atualizar o site oficial.

## ⏱️ Nota de Performance
Por utilizar o motor Pandas via WebAssembly, o site leva cerca de **10 a 15 segundos** para inicializar no primeiro acesso. Aguarde o círculo de carregamento sumir para iniciar as buscas.

---
**Equipe de Planejamento - Planning Dev Lab**