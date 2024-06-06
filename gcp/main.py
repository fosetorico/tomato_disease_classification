from google.cloud import storage
import tensorflow as tf
import tf_keras as keras
from PIL import Image
import numpy as np


BUCKET_NAME = "fosetorico"
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

model = None


# blob = Binary Large Object
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)


def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/tomato.h5",
            "/tmp/tomato.h5",
        )
        model = keras.models.load_model("/tmp/tomato.h5")

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256))  # image resizing
    )

    # image = image/255  # normalize the image in 0 to 1 range
    img_array = tf.expand_dims(image, axis=0)
    predictions = model.predict(img_array)
    print("Predictions:", predictions)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}

