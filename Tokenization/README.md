# 🚀 AI Tokenization & Cost Estimation Project  

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)  
![NLP](https://img.shields.io/badge/Domain-NLP-orange.svg)  
![Transformers](https://img.shields.io/badge/Library-Transformers-green.svg)  
![HuggingFace](https://img.shields.io/badge/HuggingFace-BERT-yellow.svg)  
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5/4-ff69b4.svg)  
![Microsoft](https://img.shields.io/badge/Microsoft-Phi--3-red.svg)  

---

## 🎯 Project Overview  

This project demonstrates how to:  
- 🌐 **Scrape & preprocess web content** using `requests` + `BeautifulSoup`  
- 🔡 **Tokenize text** with multiple industry-standard **tokenizers**  
- 📊 **Compare token counts** across **Microsoft Phi-3**, **Hugging Face BERT**, and **OpenAI GPT-3.5/4 (tiktoken)**  
- 💰 **Estimate LLM inference costs** (based on token usage)    

---

## 🛠️ Tech Stack  

- **Languages & Tools**: Python, Requests, BeautifulSoup, Transformers (Hugging Face), Tiktoken  
- **Models Used**:  
  - Microsoft **Phi-3 Mini Instruct**  
  - Hugging Face **BERT (bert-base-uncased)**  
  - OpenAI **GPT-3.5/4** Tokenizer (`tiktoken`)  
- **Concepts Applied**: Web scraping, Preprocessing, Tokenization, Cost Estimation, Large Language Models (LLMs), Natural Language Processing (NLP)  

---

## 📈 Token Counts & Cost Estimation  

### 🔹 Token Counts for sample website: https://clay.global/blog/web-design-guide/long-scrolling-websites
- Microsoft (Phi-3): **5193 tokens**  
- Hugging Face (BERT): **4742 tokens**  
- OpenAI (GPT-3.5): **4539 tokens**  

---

### 💰 Cost Estimation (Reference: For running 1 Million such websites at $0.001 per 1K tokens(GPT-3.5's cost)  

| Model | Tokens | Cost |
|-------|--------|------|
| Microsoft **Phi-3** | 5193 | ![High Cost](https://img.shields.io/badge/$5193-🔥-red?style=for-the-badge) |
| Hugging Face **BERT** | 4742 | ![Medium Cost](https://img.shields.io/badge/$4742-⚡-blue?style=for-the-badge) |
| OpenAI **GPT-3.5** | 4539 | ![Low Cost](https://img.shields.io/badge/$4539-✅-green?style=for-the-badge) |

---

## ⚡ Workflow  

🌍 Fetch Web Data → 🧹 Clean Text → 🔡 Tokenize with Models → 📊 Compare Token Counts → 💰 Estimate Costs


