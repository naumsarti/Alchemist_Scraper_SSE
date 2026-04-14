# Alchemist Scraper SSE
**Alchemist Scraper SSE** é um script em Python para raspagem de dados (web scraping) de poções e venenos da Wiki UESP (Skyrim), permitindo a busca rápida de combinações de ingredientes baseadas no efeito desejado. Inicialmente pensado para facilitar a vida dos alquimistas em *The Elder Scrolls V: Skyrim*. 

> Este projeto foi desenvolvido para um **estudo de caso prático**, com o objetivo de explorar o uso das bibliotecas `Requests` e `BeautifulSoup4`, junto ao estudo de **Web Scraping**.

## Funcionalidades

* **Busca Global:** Vasculha todas as tabelas de poções e venenos do UESP.
* **Busca por Efeito ou Ingrediente:** Encontre receitas digitando o nome do efeito (ex: *Invisibility*) ou um ingrediente específico (ex: *Giant's Toe*).

## Como Instalar e Rodar
> **Requisito:** Python 3.12 ou superior.
### 1. **Clone o repositório**
```bash
git clone https://github.com/naumsarti/Alchemist_Scraper_SSE.git
cd Alchemist_Scraper_SSE
```
### 2. **Crie um Ambiente Virtual**
- **Windows**
```bash
python -m venv .venv
.venv/Scripts/activate
```
- **Linux/macOS**
```bash
python -m venv .venv
source .venv/bin/activate
```
### 3. **Instale as Dependências**
```bash
pip install -r requirements.txt
```
### 4. **Execute o Arquivo**
```bash
python alchemist.py
```
