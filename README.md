# Verif-AI 🛡️

Verif-AI is a machine learning–based system designed to analyze news text and estimate the **risk of misinformation**.  
Rather than declaring content as absolutely “true” or “false,” the system provides a probabilistic assessment to support informed decision-making.

## Project Overview 📝
The project focuses on identifying linguistic and contextual patterns commonly associated with misleading or unreliable news using classical NLP and machine learning techniques.  
Verif-AI is intended as a **decision-support tool**, not a fact-checking authority.

## How It Works ⚙️
1. User-provided news text is cleaned using a custom preprocessing pipeline.
2. Text features are extracted using **TF-IDF vectorization**.
3. A **Passive Aggressive Classifier** evaluates whether the input resembles known misinformation patterns.
4. A pre-trained model is used for inference without requiring retraining.

## Data & Model Details 📊
- **Dataset:** ISOT Fake News Dataset (40,000+ labeled news articles)  
- **Vectorization:** TF-IDF  
- **Classifier:** PassiveAggressiveClassifier  

To keep the repository lightweight and GitHub-friendly:  
- Raw dataset files (`True.csv`, `Fake.csv`, ~100MB+) are excluded.  
- A pre-trained model is serialized and loaded only for inference.

## Text Preprocessing ⚡
All input text is passed through a custom `wordopt` function that removes:
- URLs
- HTML tags
- Special characters
- Unnecessary noise

This preprocessing improves feature quality and model consistency.

## Ethical Considerations & Limitations ⚖️
- Verif-AI estimates **misinformation risk**, not factual correctness.
- Predictions depend on training data and may not generalize across all domains.
- Outputs should not be used as the sole basis for decision-making.

## Getting Started & Usage 🚀
Clone the repository and navigate to the project folder, then run inference:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to directory
cd verif-ai
# Run inference script
python predict.py "Enter your news text here"
```
## Future Enhancements 🛠️
- [ ] **Explainability:** Integrate SHAP or LIME to show which words triggered the risk flag.
- [ ] **Multi-language Support:** Expand beyond English using multilingual embeddings.
- [ ] **API Access:** Wrap the model in a FastAPI or Flask wrapper for web integration.
- [ ] **Real-time Scraping:** Add a feature to verify news directly from a URL.

---
## Contributors 👥
This project is developed and maintained by:
* **[Dhishan](https://github.com/dhishan9)**
* **[Alaka](https://github.com/Alaka1467)**

### Project Contributions
The team collaborated on the following technical areas:
* **Model Development:** Design of the machine learning pipeline and Passive-Aggressive classifier optimization.
* **Technical Documentation:** Creation of the project framework, README, and contributing guidelines.
* **UI/UX Concepts:** Design of the web interface logic and user interaction flow.
* **Ethical AI Design:** Implementation of the risk-assessment framework and bias mitigation strategies.

