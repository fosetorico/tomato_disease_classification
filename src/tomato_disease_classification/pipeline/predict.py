import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
from tf_keras.models import load_model
from tf_keras.preprocessing import image
import os


CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Preprocess image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make predictions
        predictions = model.predict(test_image)
        print(f"Predictions shape: {predictions.shape}, Predictions: {predictions}")

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])        
        confidence_percentage = round(float(confidence) * 100, 2)

        return [{
            'class': predicted_class,
            'confidence': f"{confidence_percentage}%"
        }]
