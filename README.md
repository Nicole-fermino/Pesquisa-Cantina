# 🎣 Simulação de Phishing: Pesquisa Cantina IFRO

## 📖 Sobre o Projeto
Este repositório contém o código-fonte de uma simulação prática de **Phishing e Engenharia Social**, desenvolvida como parte do Trabalho de Segurança da Informação. O objetivo do experimento é analisar o comportamento dos usuários (alunos) e testar a hipótese de que *a promessa de uma recompensa aumenta a probabilidade de interação com links maliciosos ou suspeitos*.

O cenário construído utiliza um contexto escolar direto: uma falsa pesquisa de satisfação sobre a cantina do Instituto Federal de Rondônia (IFRO), oferecendo um "cupom de desconto" como gatilho mental para atrair as vítimas.

## 👥 Equipe
* **Componentes:** Nicole Fermino, Yasmim Machado, Maria Luiza Gomes, Ana Carolina Dantas e João Vitor Barros.
* **Turma:** 3ºB Informática
* **Instituição:** Instituto Federal de Rondônia (IFRO) - *Trabalho Acadêmico*

## 🛠️ Tecnologias Utilizadas
O projeto foi desenvolvido utilizando tecnologias web padrão e um backend leve:
* **Backend:** Python e Flask (Microframework)
* **Frontend:** HTML5, CSS3, e Jinja2 (Template Engine)
* **Banco de Dados:** SQLite (Armazenamento local/embutido)
* **Hospedagem:** PythonAnywhere (Deploy em nuvem para acesso via QR Code)

## ⚙️ Como funciona o fluxo da simulação?
1. **Atração:** A vítima escaneia um QR Code presente em cartazes espalhados pelo campus.
2. **Coleta de Dados (Simulada):** O usuário é direcionado para um formulário solicitando informações básicas e opiniões sobre a cantina.
3. **Armazenamento:** Os dados submetidos são salvos localmente no arquivo estruturado `dados_phishing.db`.
4. **Educação e Alerta:** Ao clicar em "Enviar", em vez de receber o cupom, a vítima é redirecionada para uma página educativa contendo um aviso em vídeo.

## ⚠️ Aviso Ético e de Privacidade
**Este projeto tem fins estritamente educacionais e de conscientização.** 
Durante a aplicação deste experimento, adotamos medidas rigorosas de ética e segurança:
* Nenhuma informação sensível real (senhas, CPF, dados bancários) é solicitada ou coletada.
* A página de destino revela imediatamente a natureza do teste para evitar qualquer dano aos participantes.
