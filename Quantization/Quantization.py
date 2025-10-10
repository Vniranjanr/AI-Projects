!pip install -q --upgrade torch==2.5.1+cu124 torchvision==0.20.1+cu124 torchaudio==2.5.1+cu124 --index-url https://download.pytorch.org/whl/cu124
!pip install -q requests bitsandbytes==0.46.0 transformers==4.48.3 accelerate==1.3.0

from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer, BitsAndBytesConfig
import torch, math, gc, pandas as pd, matplotlib.pyplot as plt

# instruct models

models = [
    "microsoft/Phi-3-mini-4k-instruct",
    "google/gemma-2-2b-it",
    "Qwen/Qwen2.5-3B-Instruct"
]

messages = """Data scientists love working with large datasets
because they can discover patterns that humans would never notice.
However, cleaning and preparing data is often the hardest part!"""

# Quantization Config - this allows us to load the model into memory and use less memory

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4"
)

def compute_perplexity(model, tokenizer, text):
    enc = tokenizer(text, return_tensors="pt").to("cuda")
    with torch.no_grad():
        out = model(enc.input_ids, labels=enc.input_ids)
        loss = out.loss
    return math.exp(loss.item())

def compute_quantized(model_id, text):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        quantization_config=quant_config
    )

    ppl = compute_perplexity(model, tokenizer, text)
    mem = model.get_memory_footprint() / 1e6

    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    return ppl, mem

def compute_unquantized(model_id, text):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        torch_dtype=torch.float16
    )

    ppl = compute_perplexity(model, tokenizer, text)
    mem = model.get_memory_footprint() / 1e6

    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    return ppl, mem

results = []
for model_id in models:
    ppl_q, mem_q = compute_quantized(model_id, messages)
    ppl_fp, mem_fp = compute_unquantized(model_id, messages)
    results.append({
        "Model": model_id.split("/")[-1],
        "Quantized PPL": round(ppl_q, 2),
        "Unquantized PPL": round(ppl_fp, 2),
        "Quantized Memory (MB)": round(mem_q, 1),
        "Unquantized Memory (MB)": round(mem_fp, 1)
    })

df = pd.DataFrame(results)

def highlight_cols(val, column):
    """Apply fixed background colors for quantized/unquantized columns."""
    if "PPL" in column:
        if "Quantized" in column:
            return "background-color: #4CAF50;"
        else:
            return "background-color: #c8e6c9;"
    elif "Memory" in column:
        if "Quantized" in column:
            return "background-color: #FF8C42;"
        else:
            return "background-color: #ffe0b2;"
    return ""
styled = (
    df.style
      .apply(lambda s: [highlight_cols(v, s.name) for v in s], axis=0)
      .set_caption("Quantization vs Unquantized Model Performance")
      .format(precision=2)  # limit to 2 decimal points
      .set_table_styles([
          {"selector": "th", "props": [("background-color", "#424242"),
                                       ("color", "white"),
                                       ("font-weight", "bold")]}
      ])
)

display(styled)
