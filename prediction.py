from tensorflow.keras.models import load_model

def load_model():
    model = load_model('model/pet_health_model.h5')
    return model

def predict_health(model, img_array):
    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        return 'Healthy'
    else:
        return 'Consult a Vet'