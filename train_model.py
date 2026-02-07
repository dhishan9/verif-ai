import pandas as pd
import re
import string
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# 1. Define the cleaning function
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# 2. Load the data
print("Loading data...")
fake = pd.read_csv('Fake.csv')
true = pd.read_csv('True.csv')

fake['label'] = 0
true['label'] = 1

# 3. Combine and shuffle
df = pd.concat([fake, true]).sample(frac=1).reset_index(drop=True)

# 4. Clean the text (This might take a minute)
print("Cleaning text...")
df["text"] = df["text"].apply(wordopt)

# 5. Split the data
x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)

# 6. Convert text to numbers (TF-IDF)
print("Vectorizing data...")
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(x_train)

# 7. Train the model
print("Training model...")
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)

# 8. Save the model and the vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump((tfidf_vectorizer, pac), f)

print("Success: model.pkl created!")