from fastapi import FastAPI
from fastapi.responses import JSONResponse

from model.predict import predict_output,MODEL_VERSION,model

from schema.userInput import user_input

app = FastAPI()


@app.get("/")
def home():
    return {'message' : 'Insurance prediction Model '}

@app.get("/health")
def health_check():
    return {
        'status' : 'Ok',
        'version' : MODEL_VERSION,
        'model_loaded' : model is not None
    }

@app.post("/predict")
def predict_premium(data: user_input):

    input_data = {
        'bmi': data.bmi,
        'Age_group': data.age_group,
        'life_style_risk': data.life_style_risk,
        'city_tyre': data.city_tyre,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(input_data)

        return JSONResponse(
            status_code=200,
            content={'predicted category': prediction}
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=str(e)
        )