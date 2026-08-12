# Iris Flower Classification

## Project Overview
This project classifies Iris flowers into three species (Setosa, Versicolor, Virginica) based on their sepal and petal dimensions.

## Objective
To build a robust machine learning model that accurately classifies Iris species and to identify the most discriminative features.

## Dataset Information
The dataset is loaded directly from `sklearn.datasets.load_iris()`.

## Technologies Used
- Python 3.12+
- Pandas, NumPy for Data Manipulation
- Matplotlib, Seaborn for Visualization
- Scikit-Learn for Machine Learning
- Joblib for Model Saving

## Project Workflow
1. Dataset Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering & Split
5. Model Training (Logistic Regression, KNN, Decision Tree, Random Forest)
6. Model Evaluation
7. Conclusion

## EDA Summary
- Setosa is easily separable from the others.
- Petal measurements have high correlation and are strong discriminators.

## Models Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

## Evaluation Metrics
- Accuracy, Precision, Recall, F1 Score, Confusion Matrix

## Results
All models achieve high accuracy. The Random Forest model is saved as the best overall generalized model.

## Future Scope
- Hyperparameter tuning for larger datasets.
- Deployment via Flask/FastAPI.

## Folder Structure
- `dataset/`: (Not used for this specific project as dataset is from sklearn)
- `notebook/`: Contains the Jupyter Notebook.
- `images/`: Contains EDA charts.
- `models/`: Saved model `.pkl` file.
- `outputs/`: For generated outputs.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Open `notebook/Iris_Classification.ipynb`
3. Run all cells.
