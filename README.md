# Automatic-Text-Summarization
An abstractive text summarization project using a fine-tuned BART model on the CNN/DailyMail dataset. It focuses on generating fluent, semantically accurate summaries for news articles, featuring data preprocessing, partial fine-tuning, and evaluation with ROUGE and BERTScore.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Methodology](#methodology)
- [Results](#results)
- [License](#license)

---

## 🔍 Overview
This project develops a **news article summarization system** using **BART (Bidirectional and Auto-Regressive Transformer)**. The goal is to create **concise, context-aware summaries** that preserve the meaning of long, complex articles.

---

## 📚 Dataset
We used the **CNN/DailyMail v3.0.0** dataset:
- 300K+ news articles with human-written summaries.
- Focused on **abstractive summarization** tasks.
- Preprocessed by cleaning text, removing extra spaces, and tokenizing sentences.

---

## 🧩 Model Architecture
The project uses **BART**, a Transformer-based encoder-decoder model:
- **Encoder:** 12 Transformer layers to capture context.
- **Decoder:** 12 Transformer layers with masked attention for text generation.
- Fine-tuned with partial layer freezing for better performance.

---

## 🔬 Methodology
1. **Data Preprocessing:** Clean, tokenize, and split data (90/5/5).
2. **Model Training:** Fine-tune BART using `Seq2SeqTrainer` with early stopping.
3. **Evaluation:** ROUGE and BERTScore metrics used to measure lexical and semantic accuracy.
4. **Beam Search:** For improved output quality.

---

## 📈 Results

| Metric                  | Score              | Notes |
|------------------------|------------------|------|
| **BERTScore**          | **0.8849**       | High semantic similarity |
| **ROUGE-1 / ROUGE-2**  | Moderate         | Lower due to abstractive nature |
| **Training Loss**      | 2.69 → 0.54      | Significant decrease |
| **Validation Loss**    | 0.62 → 0.59      | Small gap, no overfitting |

**Analysis:**
- Generated summaries are fluent, concise, and contextually accurate.
- Fine-tuning improved semantic understanding while avoiding overfitting.
- Model effectively condensed 500+ word articles into 3-4 sentence summaries.

---

## 📜 License
This project is for **showcase purposes only**. Reproduction, modification, or commercial use without explicit permission is prohibited.
