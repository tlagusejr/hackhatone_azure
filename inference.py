from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, \
    Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = "https://cropsclassificationinstance-prediction.cognitiveservices.azure.com/"
training_key = "caf5658a51004555a0437ae5c204a826"
prediction_key = "c12dc0a24d76499d81dad2b9e41f0d63"
prediction_resource_id = "/subscriptions/ce4ffcb6-a4a0-4527-800c-e99012407d50/resourceGroups/test-resource/providers/Microsoft.CognitiveServices/accounts/cropsclassificationinstance-Prediction"
publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
project_name = '2f5f68c8-6990-4b1a-91de-f7536ccb6cb3'
project_id = '071a9fdf-ddfe-4f27-9ec8-740ef4e8feaf'


# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open('C:\\Users\\starc\\PycharmProjects\\codingtest\\gocu\\image\\test\\test.png', "rb") as image_contents:
    results = predictor.classify_image(
        project_id, publish_iteration_name, image_contents.read())


    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))

