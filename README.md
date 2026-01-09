# AI Interview Simulator

A simple Streamlit app that helps users practice interview questions and get instant feedback based on clarity, relevance, keywords, and filler words.

## Features

- Choose from predefined interview topics
- Analyze text answers for:
  - Clarity
  - Relevance
  - Filler words
  - Keyword coverage
- Receive structured feedback

## Installation

```bash
git clone https://github.com/<your-username>/AI-Interview-Simulator.git
cd AI-Interview-Simulator
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install streamlit numpy scikit-learn spacy
python -m spacy download en_core_web_sm 
# Run
streamlit run app.py
```
## Project Files

- app.py — Streamlit UI
- evaluator_module.py — Logic for scoring and feedback
- questions.py — Interview questions and keywords
