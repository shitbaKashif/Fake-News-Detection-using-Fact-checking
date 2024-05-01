import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import requests


class FactCrescendo:
  def get_debunked_news():
    # Get the API endpoint for the debunked news stories.
    api_endpoint = "https://factcrescendo.com/api/v1/fact-checks"

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Create a list of debunked news stories.
      debunked_news_stories = []
      for fact_check in response_data:
        debunked_news_stories.append({
          "title": fact_check["title"],
          "url": fact_check["url"],
          "is_fake": fact_check["is_fake"],
        })

      # Return the list of debunked news stories.
      return debunked_news_stories
    else:
      # Raise an error.
      raise Exception("Error getting debunked news stories from Fact Crescendo: {}".format(
          response.status_code))

class FactCrescendo:
  def get_debunked_news():
    """
    Returns a list of debunked news stories from Fact Crescendo.
    """
    # Get the API endpoint for the debunked news stories.
    api_endpoint = "https://factcrescendo.com/api/v1/fact-checks"

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Create a list of debunked news stories.
      debunked_news_stories = []
      for fact_check in response_data:
        debunked_news_stories.append({
          "title": fact_check["title"],
          "url": fact_check["url"],
          "is_fake": fact_check["is_fake"],
        })

      # Return the list of debunked news stories.
      return debunked_news_stories
    else:
      # Raise an error.
      raise Exception("Error getting debunked news stories from Fact Crescendo: {}".format(
          response.status_code))


class TheNewsLens:
  def get_debunked_news():
    """
    Returns a list of debunked news stories from The News Lens.
    """
    # Get the API endpoint for the debunked news stories.
    api_endpoint = "https://thenewslens.com/api/v1/fact-checks"

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Create a list of debunked news stories.
      debunked_news_stories = []
      for fact_check in response_data:
        debunked_news_stories.append({
          "title": fact_check["title"],
          "url": fact_check["url"],
          "is_fake": fact_check["is_fake"],
        })

      # Return the list of debunked news stories.
      return debunked_news_stories
    else:
      # Raise an error.
      raise Exception("Error getting debunked news stories from The News Lens: {}".format(
          response.status_code))


class DunyaKhabar:
  def get_debunked_news():
    """
    Returns a list of debunked news stories from Dunya Khabar.
    """
    # Get the API endpoint for the debunked news stories.
    api_endpoint = "https://dunyakhabar.com/api/v1/fact-checks"

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Create a list of debunked news stories.
      debunked_news_stories = []
      for fact_check in response_data:
        debunked_news_stories.append({
          "title": fact_check["title"],
          "url": fact_check["url"],
          "is_fake": fact_check["is_fake"],
        })

      # Return the list of debunked news stories.
      return debunked_news_stories
    else:
      # Raise an error.
      raise Exception("Error getting debunked news stories from Dunya Khabar: {}".format(
          response.status_code))


class Awaz:
  def get_debunked_news():
    """
    Returns a list of debunked news stories from Awaz.
    """
    # Get the API endpoint for the debunked news stories.
    api_endpoint = "https://awaz.pk/api/v1/fact-checks"

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Create a list of debunked news stories.
      debunked_news_stories = []
      for fact_check in response_data:
        debunked_news_stories.append({
          "title": fact_check["title"],
          "url": fact_check["url"],
          "is_fake": fact_check["is_fake"],
        })

      # Return the list of debunked news stories.
      return debunked_news_stories
    else:
      # Raise an error.
      raise Exception("Error getting debunked news stories from Awaz: {}".format(
          response.status_code))


class FactFocus:
  def get_debunked_news():
    """
    Returns a list of debunked news stories from Fact Focus.
    """
    # Get the API endpoint for the debunked news stories.
    api_endpoint = "https://factfocus.pk/api/v1/fact-checks"

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Create a list of debunked news stories.
      debunked_news_stories = []
      for fact_check in response_data:
        debunked_news_stories.append({
          "title": fact_check["title"],
          "url": fact_check["url"],
          "is_fake": fact_check["is_fake"],
        })

      # Return the list of debunked news stories.
      return debunked_news_stories
    else:
      # Raise an error.
      raise Exception("Error getting debunked news stories from Fact Focus: {}".format(
          response.status_code))

  def get_fact_check(self, fact_check_id):
    """
    Returns a specific fact-check from Awaz.
    """
    # Get the API endpoint for the specific fact-check.
    api_endpoint = "https://awaz.pk/api/v1/fact-checks/{}".format(
        fact_check_id)

    # Make a request to the API endpoint.
    response = requests.get(api_endpoint)

    # Check if the request was successful.
    if response.status_code == 200:
      # Get the response data.
      response_data = response.json()

      # Return the fact-check data.
      return response_data
    else:
      # Raise an error.
      raise Exception("Error getting fact-check from Awaz: {}".format(
          response.status_code))



# Gather Pakistani news from fact-checkers
fact_checkers = ["Fact Crescendo", "The News Lens", "Dunya Khabar", "Awaz", "Fact Focus"]

# Create a dictionary that maps each fact-checker name to a fact-checker object
fact_checker_objects = {
    "Fact Crescendo": FactCrescendo(),
    "The News Lens": TheNewsLens(),
    "Dunya Khabar": DunyaKhabar(),
    "Awaz": Awaz(),
    "Fact Focus": FactFocus(),
}

news_data = []
for fact_checker_name in fact_checkers:
    fact_checker = fact_checker_objects[fact_checker_name]
    news_data.extend(fact_checker.get_debunked_news())

# Label the news stories
news_data["label"] = [1 if news_story["is_fake"] else 0 for news_story in news_data]

# Clean the data
news_data = news_data.dropna()

# Split the data into training and test sets
train_data, test_data = train_test_split(news_data, test_size=0.2)

# Train the machine learning model
model = LogisticRegression()
model.fit(train_data["text"], train_data["label"])

# Evaluate the machine learning model
predictions = model.predict(test_data["text"])
accuracy = np.mean(predictions == test_data["label"])

print("Accuracy:", accuracy)

