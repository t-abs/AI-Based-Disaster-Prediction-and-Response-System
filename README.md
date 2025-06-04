# AI-Based-Disaster-Prediction-and-Response-System-
![image](https://github.com/user-attachments/assets/23a3bc7a-fc18-4cfa-b570-344a286f169d)


Overview

The AI-Based Disaster Prediction and Response System is designed to leverage the power of Artificial Intelligence and Machine Learning to predict natural disasters and enhance response efforts. This project focuses on forecasting floods, earthquakes, and hurricanes, and provides tools to identify and assist victims post-disaster.

#Features
Predictive Models for Natural Disasters:

1.Flood Prediction Model: Analyzes historical weather patterns, river levels, and precipitation data to forecast potential flooding events.

![Screenshot 2025-05-28 123053](https://github.com/user-attachments/assets/4953b177-b20e-430e-a3e4-1ddd5ca7cbd3)



2.Earthquake Prediction Model: Utilizes seismic activity and geological data to predict earthquake occurrences and their potential impacts.

![Screenshot 2024-07-24 114757](https://github.com/user-attachments/assets/bbe4fd0a-c724-4aa3-8505-ede55302aaac)


3.Hurricane Prediction Model: Uses atmospheric data, ocean temperatures, and historical storm patterns to predict hurricane formations and trajectories.
![Screenshot 2024-07-24 114849](https://github.com/user-attachments/assets/46f18315-8708-47b6-a59f-b8cb50114b1a)


Chatbase API Integration:

Integrated with Chatbase API to offer an interactive chat-based interface. Users can receive real-time responses and information related to flood scenarios and safety measures.

![Screenshot 2024-07-24 114905](https://github.com/user-attachments/assets/fce1185b-6016-47c4-be24-04040dc4b104)


YOLOv5 Model for Post-Disaster Response:

Deployed YOLOv5 (You Only Look Once) object detection model to analyze post-disaster imagery and videos. This model helps in locating and identifying victims, aiding in efficient rescue operations.

![Screenshot 2024-07-24 114922](https://github.com/user-attachments/assets/8ad80c30-0a40-49bc-8ec0-2f94fb85e8a0)

Input video- https://drive.google.com/file/d/1JavezBw-sL8aN0rA28tajhg9rKx9-IJC/view

Output video- https://drive.google.com/file/d/1m8MW_zcCqczPru_CO85Y5WTe3nfdc9zE/view?pli=1


Technology Stack

Machine Learning Models: Developed using Python, pandas, numpy, and scikit-learn.

Chatbase API: Provides a responsive chat interface for user interaction.

YOLOv5: Utilized for real-time object detection and victim identification in disaster-stricken areas.

Html,css,js and NodeJs: For creating Frontend and Backend Website Integration with AI/ML.

How It Works

Prediction Phase:

1.Data Collection: Gathers relevant data from various sources, including weather stations, seismic sensors, and oceanographic data.

2.Model Training: Uses historical data to train machine learning models capable of predicting floods, earthquakes, and hurricanes.

3.Prediction: The models generate forecasts based on current data inputs, providing early warnings for potential disasters.

This repository contains large files tracked by Git LFS. To properly download and set up the project, follow these steps:

Prerequisites
Git

Git LFS

Python

pip

Node.js

npm

Installation

Install Git LFS If you don't have Git LFS installed, download and install it from the Git LFS installation page.

Clone the repository

git clone  https://github.com/t-abs/AI-Based-Disaster-Prediction-and-Response-System

cd Predicaster

Set up the Predicaster backend

cd Predicater/Predicaster

pip install -r requirements.txt

python app.py

Set up the Client (in a new terminal window)

cd ../client

npm i

npm start


#Response Phase:

1.Chat Interface: Users interact with the system through a chat interface powered by Chatbase API to get real-time updates and safety advice.

2.Victim Detection: Post-disaster, the YOLOv5 model processes images and videos to identify and locate victims, streamlining rescue operations.

