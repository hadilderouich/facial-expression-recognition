from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from keras.models import model_from_json
import io
from PIL import Image

app = FastAPI()

# Charger le modèle
with open("fer.json", "r") as json_file:
    model = model_from_json(json_file.read())
model.load_weights("fer.weights.h5")

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

@app.post("/predict-emotion/")
async def predict_emotion(file: UploadFile = File(...)):
    # Lire l'image
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes)).convert('L')  # grayscale
    img = img.resize((48, 48))
    img_array = np.array(img).astype('float32')
    img_array = np.expand_dims(img_array, axis=0)
    img_array = np.expand_dims(img_array, axis=-1)

    # Prédiction
    prediction = model.predict(img_array)
    emotion = emotions[np.argmax(prediction[0])]

    return JSONResponse(content={"emotion": emotion})
