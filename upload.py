from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = 
training_key = 
prediction_key = 
prediction_resource_id = 
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
project_name = uuid.uuid4()
project = trainer.create_project(project_name)

# Make two tags in the new project
nomal_tag = trainer.create_tag(project.id, "nomal")
disease_tag = trainer.create_tag(project.id, "disease")

base_image_location_normal = 'C:\\Users\\starc\\PycharmProjects\\codingtest\\gocu\\image\\normal'
file_arr_normal = os.listdir(base_image_location_normal)
base_image_location_disease = 'C:\\Users\\starc\\PycharmProjects\\codingtest\\gocu\\image\\disease'
file_arr_disease = os.listdir(base_image_location_disease)
limit = min(len(file_arr_disease),len(file_arr_normal))
from tqdm import tqdm
image_list = []
n = 32
n0 = 0

while True:
    image_list = []
    for image in tqdm(file_arr_normal[n0:n]):
        file_name = image
        with open(os.path.join (base_image_location_normal, file_name), "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[nomal_tag.id]))

    for image in tqdm(file_arr_disease[n0:n]):
        file_name = image
        with open(os.path.join (base_image_location_disease, file_name), "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[disease_tag.id]))

    upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
    n0 = n
    n += 32

    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print("Image status: ", image.status)

print('Done!')
