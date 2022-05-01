from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, \
    Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = 
training_key 
prediction_key =
prediction_resource_id = 
publish_iteration_name = 

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
project_name = '2f5f68c8-6990-4b1a-91de-f7536ccb6cb3'
project_id = '071a9fdf-ddfe-4f27-9ec8-740ef4e8feaf'

print ("Training...")
iteration = trainer.train_project(project_id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project_id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 60 seconds...")
    time.sleep(60)
trainer.publish_iteration(project_id, iteration.id, publish_iteration_name, prediction_resource_id)


