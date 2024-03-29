

# **QuickEats: A Foodie Solution**
![Foodie Solution](images/readme/food-101.jpg)

This project is a part of the ADS-599 course in the Applied Data Science Program at the University of San Diego.

### **Contributors**
* Ivan Chavez
* Lane Whitmore
* Uyen Pham

## Project Status: Active

## Installation
To use and run this project locally on your machine, follow these steps after cloning the repository:

### Step 1 Downloading the pretrained model:
Please download and replace the MobileNet [model_full_tune](models/mobilenet) with the latest mobilenet trained model found [Here](https://drive.google.com/drive/folders/1hBn4oSHoF-_NIgX_vMoFUq7cWmtriQX9?usp=sharing)

### Step 2 Register with API Ninjas
An account with API Ninjas is needed in order to obtain the necessary API Key for Recipe Generation. Please follow the steps listed below to correctly configure your key. <br>
1. Create a free account with API Ninjas [Here](https://api-ninjas.com/register)
2. Once your account is created navigate to your account dashboard and copy your API Key
3. Finally, inside [index.html](templates/index.html) at line 68 (Reference Image Below) replace the value for X-Api-Key with your API Key:
<img src="images/readme/codesnip.png" alt="Image Alt Text" width="800"/>

### Step 3 Run the QuickEats app
2. Open a command line interface and navigate to the directory of the cloned repository.

3. Ensure that all dependencies are installed. If not use `pip install -r requirements.txt`

4. Run the following command to start the local server: `uvicorn main:app --reload`

5. Once the server is running, open your web browser and enter the following URL: http://127.0.0.1:8000

6. Users will be directed to the API application interface as below:

   ![Foodie Solution](images/readme/interface.png) 

   Click **Upload Food Image** button to upload a random food image dowloaded from the internet

   Click the **Classify** button to initiate the prediction
   
   The API will process the image and provide the the name of the food, the probability of the predicted class and three corresponding recipes. Below is an example of the output
   
   ![Foodie Solution](images/readme/pancake.png)

## Project Intro/Objective
The main purpose of this project is to leverage machine learning techniques to develop a reliable and convenient solution for food enthusiasts. We aim to build an image recognition system for food integrated with a recipe API, simplifying the process of identifying food and providing accurate recipe recommendations. Our goal is to enhance the culinary experience for users, inspiring them to explore new dishes and flavors easily.

## Methods Used
- Machine Learning
- Data Engineering
- Data Visualization
- Image Processing

## Technologies
- Python
- FastAPI
- HTML
- CSS

## Project Description
Our project focuses on developing an image recognition system for food using convolutional neural networks (CNNs) on the Food101 dataset. The Food101 dataset consists of a diverse collection of food images representing different food items.

To achieve our goal, we will preprocess the images and utilize transfer learning to train the CNN model. The trained model will then be integrated into a user-friendly web application, allowing users to easily upload food images through the user interface.

Once the user uploads an image, the application will use the trained model to accurately classify the food type in the image. Additionally, the application will fetch relevant recipe recommendations from a recipe API based on the identified food type, providing users with a delightful culinary experience.

Throughout the project, we anticipate challenges related to data quality, model performance, and the seamless integration of the recipe API. We will address these challenges by iteratively improving the model, optimizing hyperparameters, and fine-tuning the integration process.


## Downloading the Food-101 Image Dataset:
As the dataset too large to upload to GitHub, we suggest following FastAI's download protocol.
Assuming FastAI has been installed in your Python environment of choice, you can follow these steps:
1. Import the neccessary packages: <br>
   from fastai.vision.all import URLs, get_image_files, untar_data
2. Download the Food-101 dataset: <br>
   path = untar_data(URLs.FOOD)
3. Print the path: <br>
   path.ls()
   <br>
   Count the images in path (should be 101,000):
   <br>
   files = get_image_files(path/"images")
   <br>
   print("Number of Food Images:", len(files))

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We sincerely thank Professor Mikael Graindorge and Dr. Ebrahim Tarshizi for their guidance. We are grateful for the support from the Applied Data Science Master’s Program at the University of San Diego. Lastly, our appreciation goes to the creators of the Food-101 dataset, which formed the bedrock of our study. 

