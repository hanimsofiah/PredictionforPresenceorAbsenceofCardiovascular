# Prediction for Presence or Absence of Cardiovascular Disease

This repository serves as a guideline for Reproducible Research process of Prediction for Presence or Absence of Cardiovascular Disease following the OSEMN(obtain,scrub,explore,model,interpret) framework. 

Final Data Product can be accessed via url [Cardiovascular Disease Prediction App](https://prediction-cardiovascular-wqd7001-group9.streamlit.app/). 

Raw Dataset can be accessed from cardio_data_processed.csv (retrieved from [Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/colewelkins/cardiovascular-disease/data))

# Set Up Environment
Install Python 3.11, Streamlit, and TensorFlow.

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


# Table of Contents

1. [Obtain](#obtain)
2. [Scrub](#scrub)
3. [Explore](#explore)
4. [Model](#model)
5. [Interpret](#interpret)

## Obtain 
* Start with the obtain dataset -  **data_science_assignment.py**
  * Load the Raw Dataset 
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L25-L34
    
## Scrub
* Data Preprocessing -  **data_science_assignment.py**
  * Involves check missing data 
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L36-L47

## Explore
* Data Exploration -  **data_science_assignment.py**
  * Perform exploratory data analysis (EDA), which may include statistical summaries, correlation analyses, and visualization of data distributions
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L49-L428

## Model
* Model Development -  **data_science_assignment.py**
  * Feature selection - removes the 'bp_category' and 'id' columns from the dataframe df to eliminate features that are not needed for the model.
  * Encoding Categorical Data - uses an OrdinalEncoder() to transform the 'bp_category_encoded' column into numerical values which is crucial for machine learning algorithms as they require numerical input.
  * Scaling the data features - apply MinMaxScaler() to the training and testing sets, which scales the feature data.
  * After fitting the scaler to the data, export and save this scaler object so that can use the same scaling parameters later to ensure consistency in how data is processed before making predictions.
  * The scaler is saved as a .pkl file, which in case is the **min_max_scaler.pkl**.
  * Splitting the data - into training and testing sets, selecting algorithms, create models, and evaluating their performance.
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/52b2f578690b61918588148a66da831b6c27c38b/data_science_assignment.py#L454-L1093

## Interpret
* Model Serialization
  * The final chosen model(s) are saved (serialized) – the .keras file being created, which corresponds to the **cardio_model.keras** 

# Deploy 
* Start with the **apps.py** as the entry point to deploy and run application
  * Specify Preprocessing tool (**min_max_scaler.pkl**) 
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/85fffa0e5af9caaafd7f5bad90852e9af7a873e1/apps.py#L9-L22
  * Specify the serialized model (**cardio_model.keras**)
    https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/blob/85fffa0e5af9caaafd7f5bad90852e9af7a873e1/apps.py#L24-L27

 # 🚀 Try It Out!

 * Example of Prediction Output : Normal
   
![image](https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/assets/155748091/1a1cce41-ee81-4fbb-9008-c210a7a31e92)

* Example of Prediction Output : Hypertension 1
  
![image](https://github.com/hanimsofia/Prediction-for-Presence-or-Absence-of-Cardiovascular/assets/155748091/151aee13-0fa4-4866-878d-fc7e280d5bd5)


 
 
