

# **QuickEats: A Foodie Solution**
![Foodie Solution](images/readme/food-101.jpg)

This project is a part of the ADS-599 course in the Applied Data Science Program at the University of San Diego.

### **Contributors**
* Ivan Chavez
* Lane Whitmore
* Uyen Pham

## Project Status: Active

## Installation
To use and run this project on your machine, follow these steps: (pending)

### Step 1 Downloading the image data:
As the dataset too large to upload to GitHub, we suggest following FastAI's download protocol.
Assuming FastAI has been installed in your Python environment of choice, you can follow these steps:
1. Import the neccessary packages:
   from fastai.vision.all import URLs, get_image_files, untar_data
2. Download the Food-101 dataset:
   path = untar_data(URLs.FOOD)
3. Print the path:
   path.ls()
   Count the images in path (should be 101,000):
   files = get_image_files(path/"images")
   print("Number of Food Images:", len(files))


## Project Intro/Objective
The main purpose of this project is to leverage machine learning techniques to develop a reliable and convenient solution for food enthusiasts. We aim to build an image recognition system for food integrated with a recipe API, simplifying the process of identifying food and providing accurate recipe recommendations. Our goal is to enhance the culinary experience for users, inspiring them to explore new dishes and flavors easily.

## Methods Used
- Machine Learning
- Data Engineering
- Data Visualization
- Image Processing

## Technologies
- Python
- HTML
- CSS

## Project Description
Our project focuses on developing an image recognition system for food using convolutional neural networks (CNNs) on the Food101 dataset. The Food101 dataset consists of a diverse collection of food images representing different food items.

To achieve our goal, we will preprocess the images and utilize transfer learning to train the CNN model. The trained model will then be integrated into a user-friendly web application, allowing users to easily upload food images through the user interface.

Once the user uploads an image, the application will use the trained model to accurately classify the food type in the image. Additionally, the application will fetch relevant recipe recommendations from a recipe API based on the identified food type, providing users with a delightful culinary experience.

Throughout the project, we anticipate challenges related to data quality, model performance, and the seamless integration of the recipe API. We will address these challenges by iteratively improving the model, optimizing hyperparameters, and fine-tuning the integration process.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
We would like to express our gratitude to our course instructor for providing valuable guidance and support throughout the project. 
