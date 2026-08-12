# Unemployment Analysis

## Project Overview
Analyzing the unemployment rate in India, especially during the COVID-19 pandemic.

## Objective
To understand unemployment trends regionally, state-wise, and temporally to extract insights regarding the pandemic's impact.

## Dataset Information
Kaggle "Unemployment in India" dataset. Ensure it's placed in `dataset/`.

## Technologies Used
- Python 3.12+
- Pandas, NumPy
- Matplotlib, Seaborn

## Project Workflow
1. Dataset Loading & Date Conversion
2. Handling Missing Values
3. Exploratory Data Analysis (EDA)
4. Pre-COVID vs Post-COVID Analysis
5. Key Findings & Policy Insights

## EDA Summary
- Time-series reveals massive spikes in unemployment around April/May 2020.
- Certain states show distinct vulnerability compared to national averages.

## Future Scope
- Integration with economic indices like GDP or inflation data.

## Folder Structure
- `dataset/`: Place `Unemployment.csv` here.
- `notebook/`: Contains the Jupyter Notebook.
- `images/`: Contains EDA charts.
- `models/`: Not used here.
- `outputs/`: For generated outputs.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Add dataset to `dataset/`
3. Run the notebook `Unemployment_Analysis.ipynb`
