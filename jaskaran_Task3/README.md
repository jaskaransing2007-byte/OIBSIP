# Car Price Prediction

## Project Overview
Predicting the selling price of used cars based on various features like year, fuel type, transmission, etc.

## Objective
To build regression models that accurately estimate used car prices, facilitating fair market transactions.

## Dataset Information
Vehicle Dataset from CarDekho. Ensure `car_data.csv` is placed in `dataset/`.

## Technologies Used
- Python 3.12+
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-Learn
- Joblib

## Project Workflow
1. Dataset Loading & Cleaning
2. Feature Engineering (Car Age)
3. EDA & Visualizations
4. Encoding Categorical Variables
5. Model Training (Linear, RF, Gradient Boosting)
6. Model Evaluation (MAE, RMSE, R2)
7. Conclusion

## Models Used
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

## Results
Gradient Boosting and Random Forest generally perform best at predicting non-linear price depreciation.

## Folder Structure
- `dataset/`: Place dataset here.
- `notebook/`: Contains the Jupyter Notebook.
- `images/`: Contains EDA charts.
- `models/`: Best model saved here.
- `outputs/`: For generated outputs.
