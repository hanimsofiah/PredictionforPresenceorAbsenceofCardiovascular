# Prediction for Presence or Absence of Cardiovascular

This repository serves as a guideline for Reproducible Research process of Prediction for Presence or Absence of Cardiovascular Disease following the OSEMN(obtain,scrub,explore,model,interpret) framework. Final Data Product can be accessed via url [Cardiovascular Disease Prediction App](https://prediction-cardiovascular-wqd7001-group9.streamlit.app/). 

Raw Dataset can be accessed from cardio_data_processed.csv (retrieved from [Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/colewelkins/cardiovascular-disease/data))

# Table of Contents

1. [Obtain](#obtain)
2. [Scrub](#scrub)
3. [Explore](#explore)
4. [Model](#model)
5. [Interpret](#interpret)

## Obtain 
* Start with the **Data_Science_Assignment.ipynb** notebook.
  * Load the Raw Dataset.

## Scrub
* Data Preprocessing
  * Involves cleaning the data, handling missing values, feature selection, and engineering. Normalizing or scaling the data features, as performed with the Min-Max Scaler.
  * After fitting the scaler to the data, export and save this scaler object so that can use the same scaling parameters later. This is done to ensure consistency in how data is processed before making predictions.
  * The scaler is saved as a .pkl file, which in case is the **min_max_scaler.pkl**

## Explore
* Data Exploration
  * Perform exploratory data analysis (EDA), which may include statistical summaries, correlation analyses, and visualization of data distributions.

## Model
* Model Development
  * Splitting the data into training and testing sets, selecting algorithms, fitting models, and evaluating their performance.
* Model Serialization
  * The final chosen model(s) are saved (serialized) – the .keras file being created, which corresponds to the **cardio_model.keras** 

## Interpret
* Start with the **apps.py** as the entry point for a Streamlit application
  * Preprocessing tool (**min_max_scaler.pkl**)
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/85fffa0e5af9caaafd7f5bad90852e9af7a873e1/apps.py#L9-L22
  * Use the serialized model (**cardio_model.keras**) 
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/85fffa0e5af9caaafd7f5bad90852e9af7a873e1/apps.py#L24-L27
 
# Set Up Environment
Install Python 3.11, Streamlit, and TensorFlow and run the application to serve the model.
