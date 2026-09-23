# Titanic Survival Prediction

## Project Overview

This project uses Machine Learning algorithms to predict whether a passenger survived the Titanic disaster or not.

The main objective of this project is to perform data analysis, data preprocessing, train different classification models, evaluate their performance, compare the results, save the best model, and make predictions using a Python script.

---

## Dataset

The dataset used in this project is the Titanic dataset.

The dataset contains information about passengers including:

* Passenger Class
* Sex
* Age
* Number of Siblings/Spouses
* Number of Parents/Children
* Fare
* Embarked

### Target Variable

* Survived

  * 0 = Did not survive
  * 1 = Survived

---

## Project Workflow

### 1. Data Loading

* Loaded Titanic train and test datasets.
* Checked dataset shape, columns, and information.

### 2. Exploratory Data Analysis (EDA)

Performed analysis and visualization:

* Survival rate by gender
* Survival rate by passenger class
* Age distribution
* Average age by survival
* Survival count

All visualizations are saved in the `images` folder.

---

## Data Preprocessing

The following preprocessing steps were performed:

* Handled missing values
* Filled missing Age values using median
* Filled missing Embarked values
* Converted categorical variables into numerical format
* Removed unnecessary columns

---

## Machine Learning Algorithms

The following classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine (SVM)
5. K-Nearest Neighbors (KNN)
6. Gaussian Naive Bayes

---

## Model Comparison

| Model                | Accuracy | Precision | Recall | F1-Score |
| -------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression  | 79.89%   | 77%       | 73%    | 75%      |
| Decision Tree        | 79.89%   | 75.68%    | 75.68% | 75.68%   |
| Random Forest        | 82.68%   | 81.16%    | 75.68% | 78.32%   |
| SVM                  | 65.36%   | 75%       | 24.32% | 36.73%   |
| KNN                  | 71%      | 70%       | 52%    | 60%      |
| Gaussian Naive Bayes | 77%      | 72%       | 72%    | 72%      |

---

## Best Performing Model

Random Forest achieved the best performance among all tested models.

**Accuracy: 82.68%**

The trained model was saved and used for making predictions through a Python script.

---

## Model Evaluation

The final model was evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-score
* Confusion Matrix

Confusion Matrix:

```
[[89 16]
 [20 54]]
```

---

## Prediction Demo

The trained model can be tested using the prediction script.

Run:

```bash
python predict.py
```

### Sample Output

```
Passenger is predicted to Survive
```

This demonstrates that the saved machine learning model can successfully make predictions on new passenger data.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Project Structure

```
Titanic_Survival_Prediction
│
├── data
│   ├── train.csv
│   └── test.csv
│
├── images
│   ├── survival_rate_by_gender.png
│   ├── survival_rate_by_class.png
│   ├── age_distribution.png
│   ├── average_age_by_survival.png
│   └── survival_count.png
│
├── notebooks
│   └── Titanic_Survival_Prediction.ipynb
│
├── model
│   └── model.pkl
│
├── predict.py
│
├── README.md
│
└── requirements.txt
```

---

## How to Run the Project

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Open the Jupyter Notebook

Open:

```
Titanic_Survival_Prediction.ipynb
```

Run all cells to perform:

* Data analysis
* Data preprocessing
* Model training
* Model evaluation

### 3. Run Prediction Script

After the model is saved, run:

```bash
python predict.py
```

The script will load the trained model and generate a survival prediction.

---

## Conclusion

This project demonstrates a complete Machine Learning workflow including data loading, exploratory data analysis, preprocessing, model training, evaluation, model saving, and prediction.

The Random Forest model provided the best results for Titanic survival prediction, and the final project includes a working prediction script for testing the trained model.

