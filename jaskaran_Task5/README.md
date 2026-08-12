# Sales Prediction

## Project Overview
Predicting product sales based on advertising expenditures across different platforms (TV, Radio, Newspaper).

## Objective
To identify the most effective advertising medium and build a model that predicts sales accurately to optimize marketing budgets.

## Dataset Information
Advertising dataset. Ensure `Advertising.csv` is in `dataset/`.

## Technologies Used
- Python 3.12+
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-Learn

## Project Workflow
1. Dataset Loading & Statistics
2. EDA (Scatter plots, Correlation)
3. Model Training (Linear, RF, Polynomial Regression)
4. Model Evaluation (Residual analysis, R2, RMSE)
5. Coefficient Interpretation

## Results
TV advertising has the strongest correlation with Sales. Polynomial/Random forest captures non-linear synergies between TV and Radio better than simple linear models.

## Folder Structure
- `dataset/`: Place dataset here.
- `notebook/`: Contains the Jupyter Notebook.
- `images/`: Contains EDA charts.
- `models/`: Best model saved here.
- `outputs/`: For generated outputs.
