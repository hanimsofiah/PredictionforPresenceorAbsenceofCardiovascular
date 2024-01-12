# Prediction for Presence or Absence of Cardiovascular

This repository serves as a guideline for Reproducible Research process of Prediction for Presence or Absence of Cardiovascular Disease following the OSEMN(obtain,scrub,explore,model,interpret) framework. 

Final Data Product can be accessed via url [Cardiovascular Disease Prediction App](https://prediction-cardiovascular-wqd7001-group9.streamlit.app/). 

Raw Dataset can be accessed from cardio_data_processed.csv (retrieved from [Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/colewelkins/cardiovascular-disease/data))

# Table of Contents

1. [Obtain](#obtain)
2. [Scrub](#scrub)
3. [Explore](#explore)
4. [Model](#model)
5. [Interpret](#interpret)

## Obtain 
* Start with the obtain dataset.
  * Load the Raw Dataset. **data_science_assignment.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L25-L34

## Scrub
* Data Preprocessing
  * Involves cleaning the data, handling missing values. **data_science_assignment.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L36-L47
  
  * Feature selection, and engineering. Normalizing or scaling the data features, as performed with the Min-Max Scaler. **data_science_assignment.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L454-L480
    
  * After fitting the scaler to the data, export and save this scaler object so that can use the same scaling parameters later. This is done to ensure consistency in how data is processed before making predictions.
  * The scaler is saved as a .pkl file, which in case is the **min_max_scaler.pkl**

## Explore
* Data Exploration
  * Perform exploratory data analysis (EDA), which may include statistical summaries, correlation analyses, and visualization of data distributions. **data_science_assignment.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L49-L428

## Model
* Model Development
  * Splitting the data into training and testing sets, selecting algorithms, fitting models, and evaluating their performance. **data_science_assignment.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L454-L1093
    
* Model Serialization
  * The final chosen model(s) are saved (serialized) – the .keras file being created, which corresponds to the **cardio_model.keras** 

## Interpret
* Start with the **apps.py** as the entry point for the application
  * Specify Preprocessing tool (**min_max_scaler.pkl**) **apps.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/85fffa0e5af9caaafd7f5bad90852e9af7a873e1/apps.py#L9-L22
  * Sepecify Use the serialized model (**cardio_model.keras**) **apps.py**
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/85fffa0e5af9caaafd7f5bad90852e9af7a873e1/apps.py#L24-L27
 
# Set Up Environment
Install Python 3.11, Streamlit, and TensorFlow and run the application to serve the model.

* Download Python 3.11 from [Python Download Page](https://www.python.org/downloads/).
* Setup TensorFlow and Streamlit Installation
  
  * TensorFlow Installation in VSCode terminal:
  ```
  pip install tensorflow
  python -c "import tensorflow as tf; print(tf.__version__)"
  ```
  
  * Streamlit Installation in VSCode terminal:
  ```
  pip install streamlit
  streamlit --version
  ```
* Specify the Tensorflow and Streamlit Version in requirements.txt
  https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/requirements.txt#L1-L2
