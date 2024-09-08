# Iris Dataset Classification

## Overview

This project predicts the species of Iris flowers using classification models. We explored a variety of algorithms and examined feature importance to assess model performance.

## Problem Statement

The task is to classify the species of an Iris flower based on its sepal and petal measurements. The goal is to build robust models and investigate the behavior of features in driving predictions.

## Dataset

The Iris dataset consists of 150 samples with 4 features (sepal length, sepal width, petal length, petal width) and 3 species.

## Methodology

- **EDA**: Visualized data distribution and feature relationships.
- **Models**: Used Logistic Regression, Decision Tree, SVM, Random Forest, and Gradient Boosting.
- **Evaluation**: Measured performance using accuracy, precision, recall, and F1-score.

## Results

The Random Forest and Gradient Boosting classifiers performed the best with accuracy scores exceeding 95%. The most important feature was petal width.

## How to Run

1. Clone this repository.
2. Set up the environment using `environment.yml`.
3. Run the Jupyter notebooks in the `notebooks/` directory.
4. Use scripts in `src/` to train models and generate plots.

## Dependencies

- Python 3.8+
- scikit-learn
- pandas
- matplotlib
- seaborn

## License

MIT License