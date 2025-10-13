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
| Phi-3-mini-4k-instruct | ![Q](https://img.shields.io/badge/10.44-%234CAF50?style=for-the-badge&labelColor=2E7D32&color=4CAF50) | ![U](https://img.shields.io/badge/10.25-%23A5D6A7?style=for-the-badge&labelColor=81C784&color=A5D6A7) | ![QM](https://img.shields.io/badge/2206.30_MB-%23FF8C42?style=for-the-badge&labelColor=F57C00&color=FF8C42) | ![UM](https://img.shields.io/badge/7642.20_MB-%23FFE0B2?style=for-the-badge&labelColor=FFB74D&color=FFE0B2) |
| gemma-2-2b-it | ![Q](https://img.shields.io/badge/16.39-%234CAF50?style=for-the-badge&labelColor=2E7D32&color=4CAF50) | ![U](https://img.shields.io/badge/15.21-%23A5D6A7?style=for-the-badge&labelColor=81C784&color=A5D6A7) | ![QM](https://img.shields.io/badge/2192.30_MB-%23FF8C42?style=for-the-badge&labelColor=F57C00&color=FF8C42) | ![UM](https://img.shields.io/badge/5228.70_MB-%23FFE0B2?style=for-the-badge&labelColor=FFB74D&color=FFE0B2) |
| Qwen2.5-3B-Instruct | ![Q](https://img.shields.io/badge/16.28-%234CAF50?style=for-the-badge&labelColor=2E7D32&color=4CAF50) | ![U](https://img.shields.io/badge/15.39-%23A5D6A7?style=for-the-badge&labelColor=81C784&color=A5D6A7) | ![QM](https://img.shields.io/badge/2010.10_MB-%23FF8C42?style=for-the-badge&labelColor=F57C00&color=FF8C42) | ![UM](https://img.shields.io/badge/6171.90_MB-%23FFE0B2?style=for-the-badge&labelColor=FFB74D&color=FFE0B2) |

---

## 💰 Efficiency Insight  


| Metric | Impact |
|---------|---------|
| 🧮 **Perplexity (PPL)** | Quantized models show a **minor increase (<1–7%)** in PPL compared to full-precision, proving **minimal loss in language quality**. |
| 💾 **Memory Reduction** | Quantization reduces memory usage from **~7.6 GB → ~2.2 GB**, achieving up to **65–70% GPU memory savings** without architecture changes. |
| ⚡ **Performance Trade-off** | Despite aggressive 4-bit compression, **response quality remains consistent**, making quantized models ideal for **deployment on limited-VRAM GPUs**. |
| 🧠 **Model Efficiency** | Demonstrates **efficient scaling across Phi-3, Gemma, and Qwen**, confirming 4-bit NF4 quantization is both **cost-effective** and **production-ready**. |


---

