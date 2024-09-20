import pandas as pd
import logging
from fastapi import APIRouter
from models import InputModel, OutputModel
from pycaret.classification import load_model, predict_model

logging.basicConfig(level=logging.INFO)

router = APIRouter()
model = None


@router.on_event('startup')
def load_model_pipeline():
    """
    Loads the model from the file "et_pipeline.pkl" and assigns it to the global variable model.

    Raises:
        FileNotFoundError: If the model file is not found.
    """
    global model
    try:
        model = load_model('et_pipeline')
    except FileNotFoundError:
        raise FileNotFoundError('Model not found!')


@router.get('/health')
def index():
    """
    Returns a dictionary with a health message.

    Returns:
        dict: A dictionary with a 'message' key containing the health message.
    """
    return {'message': 'Estou saudavel!'}


@router.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    """
    Endpoint for making predictions based on input data.

    Args:
        data (InputModel): The input data for prediction.

    Returns:
        dict: A dictionary containing the prediction result.
    """
    data_dict = data.dict()
    data_df = pd.DataFrame([data_dict])
    predictions = predict_model(model, data=data_df)
    return {"prediction": predictions["prediction_label"].iloc[0]}
