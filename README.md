# Quora Question Pairs: Identifying Question Pairs with the Same Intent

This project is aimed at solving the problem of identifying question pairs that have the same intent, based on the Kaggle competition [Quora Question Pairs](https://www.kaggle.com/competitions/quora-question-pairs). The dataset contains pairs of questions, and the goal is to predict whether they have the same meaning or not.

## Project Overview

The objective of this project is to classify question pairs as either **duplicate** (same intent) or **not duplicate**. The solution uses various text similarity measures and machine learning techniques to model the problem.

## Technologies Used

- **Python**
- **Scikit-learn**: For machine learning model training and evaluation.
- **fuzzywuzzy**: For fuzzy string matching between the question pairs.
- **Streamlit**: For building a web interface to interact with the model.
  
## Key Components

This repository contains the following key files:

- **`app.py`**: Main Streamlit application that allows you to input question pairs and predict whether they are duplicates or not.
- **`helper.py`**: Helper functions that preprocess text, extract features from the question pairs, and create input vectors for the machine learning model.
- **`cv.pkl`**: The vectorizer file used for converting the input questions into feature vectors for the model.
- **`model.pkl`**: The trained machine learning model used to classify question pairs as duplicates or not.
- **`stopwords.pkl`**: A list of stopwords used in preprocessing.
- **`requirements.txt`**: Lists all the required Python libraries for this project.
- **`setup.sh`**: Script to configure the environment for running the app.
- **`Procfile`**: Used by Heroku to set up the environment for deployment.
- **`readme.txt`**: A separate text file containing additional instructions (if any).
- **`.gitattributes`**: Git configuration file to ensure proper handling of certain file types.
  
## How to Run Locally

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/Quora-Question-Pairs.git
    cd Quora-Question-Pairs
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app locally:

    ```bash
    streamlit run app.py
    ```

5. The app will be accessible at `http://localhost:8501/`.

## Known Issues

- The **Heroku deployment** is currently encountering errors. The following message is returned during deployment: `An error occurred in the application and your page could not be served`. Please check the logs for more details:
  
    ```
    heroku logs --tail
    ```

    This error may be related to specific dependencies or configuration issues with Heroku. We are actively working on resolving this and will update the README accordingly.

## Project Files

- **`app.py`**: Main application for user interaction.
- **`cv.pkl`**: Pre-trained vectorizer used to convert text into numerical features.
- **`helper.py`**: Contains functions for feature extraction and text preprocessing.
- **`model.pkl`**: Trained machine learning model to classify question pairs.
- **`requirements.txt`**: Lists necessary Python packages for this project.
- **`Procfile`**: Contains Heroku setup for deploying the app.
- **`stopwords.pkl`**: A file containing common stopwords used for text preprocessing.

## Kaggle Competition

This project is based on the [Quora Question Pairs competition](https://www.kaggle.com/competitions/quora-question-pairs). You can find more details about the dataset and competition on Kaggle.

## Contributions

Feel free to open issues or submit pull requests if you'd like to contribute to the project. Contributions are always welcome!
