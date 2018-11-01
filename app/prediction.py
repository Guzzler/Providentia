from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region
# Now there is a trained endpoint that can be used to make a prediction
import cv2
import sys
prediction_key="b02478af3d614962a15b9a58fa8adc8f"
projectID="8cf143fa-27ac-449b-8648-0dcf3f6290b9"
training_key="4b74734b9f7f4b169ea386857fb6c54b"
trainer = training_api.TrainingApi(training_key)
project = trainer.get_project(projectID)
predictor = prediction_endpoint.PredictionEndpoint(prediction_key)

# Open the sample image and get back the prediction results.
img= cv2.imread(sys.argv[1])
height,width,channels = img.shape
with open(sys.argv[1], mode="rb") as test_data:
    results = predictor.predict_image(project.id, test_data)
for prediction in results.predictions:
    print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100), prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height)
    if prediction.probability>0.85:
        x1= prediction.bounding_box.left*width
        y1= prediction.bounding_box.top*height
        x2= (prediction.bounding_box.left+prediction.bounding_box.width)*width
        y2=(prediction.bounding_box.top+prediction.bounding_box.height)*height
        print(x1,y1,x2,y2)
        cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(255,0,0),2)
        cv2.putText(img,str(prediction.tag_name),(int(x1),int(y1)), cv2.FONT_HERSHEY_DUPLEX,5.0,(255,255,255),2)

       # cv2.putText(img, str(prediction.tag_name), (int(x1), int(y1+15)), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 255),cv2.LINE_AA)  
img2=cv2.resize(img,(65,65))
cv2.imwrite(sys.argv[2],img)
cv2.imwrite(sys.argv[3],img2)

  

