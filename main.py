import io
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras import layers


with open("data/labels.txt", "r") as file:
    food_items_list = file.readlines()

labels = [item.strip() for item in food_items_list]

model = tf.keras.models.load_model("models/mobilenet/model_full_tune")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def reviews_form(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.post("/classify")
async def analyze_reviews(request: Request, file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return {"error": "Only image files are allowed."}

    file_contents = await file.read()

    img = image.load_img(io.BytesIO(file_contents), target_size=(224, 224))
    pred_img = image.img_to_array(img)
    pred_img = tf.expand_dims(pred_img, axis=0)

    predictions = model.predict(pred_img)

    pred_label = labels[predictions.argmax()]
    pred_prob = round(predictions.max()*100,2)


    return JSONResponse(content={
        "pred_label": pred_label,
        "pred_prob": str(pred_prob)+"%"
    })
