# verif-ai
## 📊 Data Handling & Model Training
The model was trained using the **ISOT Fake News Dataset** (containing over 40,000 news articles). 

- **Optimization:** To keep the repository lightweight and efficient, the raw `True.csv` and `Fake.csv` files (approx. 100MB+) are excluded from this repository.
- **Persistence:** We use a pre-trained `model.pkl` file, which contains the serialized **Passive-Aggressive Classifier** and **TF-IDF Vectorizer**.
- **Preprocessing:** All training data was passed through a custom `wordopt` function to remove noise (URLs, HTML, special characters) before vectorization.
