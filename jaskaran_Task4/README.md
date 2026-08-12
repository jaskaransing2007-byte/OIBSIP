# Email Spam Detection

## Project Overview
Classifying SMS/Email messages as 'Spam' or 'Ham' using NLP techniques.

## Objective
To accurately filter out unwanted spam messages, enhancing user experience and security.

## Dataset Information
SMS Spam Collection dataset. Ensure it's placed in `dataset/`.

## Technologies Used
- Python 3.12+
- Scikit-Learn for ML
- NLTK for text preprocessing
- WordCloud for visualization

## Project Workflow
1. Text Preprocessing (Lowercase, remove punctuation, stopwords)
2. EDA & WordClouds
3. TF-IDF Feature Extraction
4. Model Training (Naive Bayes, Logistic Regression, SVM)
5. Model Evaluation (Focus on Recall)
6. Conclusion

## Folder Structure
- `dataset/`: Place `spam.csv` here.
- `notebook/`: Contains the Jupyter Notebook.
- `images/`: Contains WordClouds and charts.
- `models/`: Saved vectorizer and best model.
- `outputs/`: For generated outputs.
