# 🧠 LLM Quantization Performance Benchmark  

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)  
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)  
![BitsAndBytes](https://img.shields.io/badge/BitsAndBytes-4bit_Quantization-green.svg)  
![CUDA](https://img.shields.io/badge/Accelerated_with-CUDA_12.4-orange.svg)  
![Category](https://img.shields.io/badge/Domain-AI_|_LLM_Optimization-red.svg)  

---

## 🎯 Overview  

This project demonstrates **Quantization of Large Language Models (LLMs)** to achieve major **memory savings** while keeping **language understanding performance** nearly intact.  
It evaluates **Microsoft Phi-3**, **Google Gemma**, and **Qwen 2.5** models using **BitsAndBytes 4-bit quantization** and compares them against their **full-precision (FP16)** counterparts.  

---

## ⚙️ Features  

✅ **Quantized vs. Unquantized comparison** for perplexity (PPL) and memory footprint  
✅ Uses **4-bit NF4 quantization** via `BitsAndBytesConfig`  
✅ Benchmarks **3 leading open-source LLMs**  
✅ Built with **PyTorch**, **Transformers**, and **Accelerate**  
✅ Visualized results using **pandas styled DataFrame**   

---

## 🧩 Tech Stack  

| Category | Tools / Frameworks |
|-----------|--------------------|
| **Language** | Python 3.10+ |
| **Libraries** | Transformers, BitsAndBytes, Torch, Accelerate, Pandas, Matplotlib |
| **Models Tested** | `microsoft/Phi-3-mini-4k-instruct`, `google/gemma-2-2b-it`, `Qwen/Qwen2.5-3B-Instruct` |
| **Hardware** | CUDA 12.4 (GPU accelerated) |
| **Concepts** | LLM Quantization, Memory Optimization, NLP Evaluation, Model Efficiency |

---

## ⚡ Workflow  

🌍 Load Model → ⚙️ Quantize with BitsAndBytes → 🔡 Compute Perplexity → 💾 Measure Memory → 📊 Compare Results

---

## 📊 Output Preview  


| Model | Quantized PPL | Unquantized PPL | Quantized Memory (MB) | Unquantized Memory (MB) |
|--------|----------------|----------------|------------------------|--------------------------|
| Phi-3-mini-4k-instruct | **10.44** | **10.25** | **2.2 GB** &nbsp;&nbsp; ⬇️**71% smaller** | **7.6 GB** |
| gemma-2-2b-it | **16.39** | **15.21** | **2.1 GB** &nbsp;&nbsp; ⬇️**58% smaller** | **5.2 GB** |
| Qwen2.5-3B-Instruct | **16.28** | **15.39** | **2.0 GB** &nbsp;&nbsp; ⬇️**67% smaller** | **6.1 GB** |

---

## 💰 Efficiency Insight  


| Metric | Impact |
|---------|---------|
| 🧮 **Perplexity (PPL)** | Quantized models show a **minor increase (<1–7%)** in PPL compared to full-precision, proving **minimal loss in language quality**. |
| 💾 **Memory Reduction** | Quantization reduces memory usage from **~7.6 GB → ~2.2 GB**, achieving up to **65–70% GPU memory savings** without architecture changes. |
| ⚡ **Performance Trade-off** | Despite aggressive 4-bit compression, **response quality remains consistent**, making quantized models ideal for **deployment on limited-VRAM GPUs**. |
| 🧠 **Model Efficiency** | Demonstrates **efficient scaling across Phi-3, Gemma, and Qwen**, confirming 4-bit NF4 quantization is both **cost-effective** and **production-ready**. |


---

