import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os
current_dir=os.path.dirname(os.path.abspath(__file__))
model_path=os.path.join(current_dir,'cnn_model.h5')
model=tf.keras.models.load_model(model_path)
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

st.title("Image Classification using CNN")
st.write("Upload an image and the model will predict its class.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True)
    img = image.resize((32, 32),Image.LANCZOS)
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    score = predictions[0]
    st.write(f"### Prediction: {class_names[np.argmax(score)]}")
    st.write(f"Confidence: {100 * np.max(score):.2f}%")