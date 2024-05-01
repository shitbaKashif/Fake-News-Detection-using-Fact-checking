# Fake-news-detection
This Python script collects debunked news stories from various fact-checking organizations in Pakistan, trains a logistic regression model on this data, and evaluates the model's accuracy in classifying fake news. Overall, the purpose of this code is to automate the process of collecting debunked news stories, train a machine learning model to classify them, and evaluate the model's performance, thereby aiding in the identification of fake news.

**Dependencies:**
- Python 3
- pandas
- numpy
- scikit-learn
- requests
**Usage:**
Ensure you have Python 3 installed on your system.
Install the required dependencies using pip:
-    pip install pandas numpy scikit-learn requests
Run the Python script:
-    python P.py
**Description:**
The script collects debunked news stories from multiple fact-checking organizations in Pakistan, including Fact Crescendo, The News Lens, Dunya Khabar, Awaz, and Fact Focus. It utilizes each organization's API to fetch the latest debunked news stories.

These stories are then labeled based on whether they are fake or not. The script then cleans the data, splitting it into training and test sets.

A logistic regression model is trained on the training data to classify news stories as fake or not fake. Finally, the model's accuracy is evaluated using the test data.

**Classes:**
- FactCrescendo: Retrieves debunked news stories from Fact Crescendo.
- TheNewsLens: Retrieves debunked news stories from The News Lens.
- DunyaKhabar: Retrieves debunked news stories from Dunya Khabar.
- Awaz: Retrieves debunked news stories from Awaz.
- FactFocus: Retrieves debunked news stories from Fact Focus.
  
**Functions:**
- get_debunked_news(): Retrieves debunked news stories from the respective fact-checking organization's API.
- get_fact_check(fact_check_id): Retrieves a specific fact-check from Awaz.

**Data Collection:**
The script collects debunked news stories from multiple fact-checking organizations by making requests to their respective APIs. It then aggregates this data into a single dataset for training and evaluation.

**Model Training:**
A logistic regression model is trained on the collected data to classify news stories as fake or not fake based on their content.

**Evaluation:**
The accuracy of the trained model is evaluated using a separate test dataset, assessing its effectiveness in identifying fake news.


