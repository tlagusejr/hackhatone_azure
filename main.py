from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, \
    Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = 
training_key = 
prediction_key = 
prediction_resource_id = 
publish_iteration_name = "

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
project_name = 
project_id = 

# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

'''
'''
from typing import List
from PIL import Image

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import io
app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    content = """
    """
    for file in files:
        request_object_content = await file.read()
        img = Image.open(io.BytesIO(request_object_content))
        img.save('test.jpg')
        with open('test.jpg', "rb") as image_contents:
            results = predictor.classify_image(
                project_id, publish_iteration_name, image_contents.read())
            for prediction in results.predictions:
                results_prediction = 'prediction.tag_name' + ": {0:.2f}%".format(prediction.probability * 100)
                print("\t" + prediction.tag_name +
                      ": {0:.2f}%".format(prediction.probability * 100))

    return [prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100) for prediction in results.predictions]


@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
