import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer
import tiktoken

# --------------------------
# 1. Fetch Website Text
# --------------------------
def fetch_website_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove scripts/styles
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    text = " ".join(text.split())  # clean spaces/newlines
    return text

url = "https://clay.global/blog/web-design-guide/long-scrolling-websites"
text = fetch_website_text(url)

# --------------------------
# 2. Define Tokenizers
# --------------------------

# Hugging Face tokenizer
hf_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", use_fast=True)


# OpenAI tokenizer (GPT-3.5/4)
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Naive whitespace tokenizer
phi3_tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# --------------------------
# 3. Count Tokens
# --------------------------
phi3_tokens = phi3_tokenizer.encode(text)
hf_tokens = hf_tokenizer.encode(text)
openai_tokens = enc.encode(text)

print("🔹 Token Counts")
print(f"Microsoft (Phi-3): {len(phi3_tokens)} tokens")
print(f"Hugging Face (BERT): {len(hf_tokens)} tokens")
print(f"OpenAI (GPT-3.5): {len(openai_tokens)} tokens")

# --------------------------
# 4. Cost Estimation
# --------------------------
def calc_cost(token_count, price_per_1k=0.001):  
    """Default: $0.001 per 1K tokens (example, GPT-3.5 input)"""
    return (token_count / 1000) * price_per_1k

print("\n🔹 Cost Estimation (GPT-3.5 input: $0.001 per 1K tokens)")
print(f"Microsoft: ${calc_cost(len(phi3_tokens)*1000000):.4f}")
print(f"Hugging Face: ${calc_cost(len(hf_tokens)*1000000):.4f}")
print(f"OpenAI tiktoken: ${calc_cost(len(openai_tokens)*1000000):.4f}")