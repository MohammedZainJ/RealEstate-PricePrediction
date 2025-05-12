Real Estate Price Prediction using Machine Learning

This project predicts housing prices in Bengaluru based on parameters like location, square footage, number of bedrooms (BHK), and bathrooms. It combines data preprocessing, model training, and a user-friendly Tkinter GUI for real-time price prediction.

Objective

Build a machine learning model to predict property prices and deploy it using a desktop GUI (Tkinter), making it easy for users to input features and get an estimated price instantly.

Project Structure

data:
 -Bengaluru_House_Data_original.csv – Original dataset
 -Preprocessed.csv – Preprocessed dataset

visuals/
 -rajaji_nagar_outlier.png – Rajaji Nagar outlier visualization
 -hebbal_outlier.png – Hebbal outlier visualization
 -user_interface.png – Tkinter GUI screenshot
 -accuracy_and_prediction.png – GUI prediction output

-_Realestate_Priceprediction.ipynb – Data cleaning + model training

-gui_app.py – GUI application script

-real_estate_price_model.pkl – Trained model

-columns.pkl – Model feature columns

-requirements.txt – Required packages

-README.md – Project description

- Original Source: [Kaggle – Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- Features used:  
  - `location`  
  - `total_sqft`  
  - `bath`  
  - `bhk`
- Target: `price` (in Lakhs)

Data Preprocessing

- Created `bhk` column from textual `size`
- Removed outliers based on per-sqft price and logical inconsistencies
- Handled missing values
- Converted categorical features using One-Hot Encoding
- Reduced rare locations to `other` category
- Final cleaned dataset saved as `preprocessed.csv`


Visualizations (Located in `visuals/` folder)

- `rajaji_nagar_outlier.png` – Outlier detection for high-end properties in Rajaji Nagar  
- `hebbal_outlier.png` – Price trend vs. sqft for Hebbal locality  
- `user_interface.png` – Screenshot of the Tkinter user interface  
- `accuracy_and_prediction.png` – Sample prediction output shown via GUI

Model Training

- Algorithm: Linear Regression
- Library: Scikit-learn
- Used GridSearchCV for tuning and cross-validation
- Input features from `columns.pkl`
- Trained model saved using `joblib` as `bengaluru_home_prices_model.pkl`

GUI App (Tkinter)

A simple desktop GUI built with Tkinter allows users to input:
- Location
- Total Square Footage
- Number of Bedrooms (BHK)
- Number of Bathrooms

...and get a price prediction using the trained model.

Run the app:
python gui_app_tkinter.py

Installation

Clone the repository:
git clone https://github.com/MohammedZainJ/RealEstate-PricePrediction.git

Install required packages:
pip install -r requirements.txt

Run the model training notebook:
jupyter notebook _Realestate_Priceprediction.ipynb

Launch the GUI:
python gui_app_tkinter.py
