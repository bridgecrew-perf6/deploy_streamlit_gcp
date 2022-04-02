### Script for CS329s ML Deployment Lec 
import os
import json
import requests
import SessionState
import streamlit as st
import tensorflow as tf
from utils import load_and_prep_image, classes_and_models, predict_json

# Setup environment credentials (you'll need to change these)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "food-classifier-example4-1ae44c7c7423.json" # change for your GCP key
PROJECT = "food-classifier-example4" # change for your GCP project
REGION = "us-central1" # change for your GCP region (where your model is hosted)

def page_setup():
    """
    Basic setup for streamlit app page
    """
    st.set_page_config(page_title="Food Image Classifier")
    #app name
    st.title("Food Classification App")

@st.cache # cache the function so predictions aren't always redone (Streamlit refreshes every click)
def make_prediction(image, model, class_names):
    """
    Takes an image and uses a trained TensorFlow model to make a
    prediction.
    Args:
        image: image file
        model: trained Tensorflow model
        class_names (list): class_names
    Returns:
        image tensor (preproccessed)
        pred_class (prediction class from class_names)
        pred_conf (model confidence)
    """
    image = load_and_prep_image(image)
    # Cast tensors as int16 (saves a lot of space, ML Engine has a limit of 1.5MB per request)
    image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
    # image = tf.expand_dims(image, axis=0)
    preds = predict_json(project=PROJECT,
                         region=REGION,
                         model=model,
                         instances=image)
    pred_class = class_names[tf.argmax(preds[0])]
    pred_conf = tf.reduce_max(preds[0])
    return image, pred_class, pred_conf

def model_selection():
    """
    Returns CLASSES & MODEL from sidebar drop down menu selection
    """
    # Pick the model version, currently only 1 enabled
    choose_model = st.sidebar.selectbox(
        "Pick the model you'd like to use for inference",
        (
            "Model 1 (10 food classes)", # original 10 classes, selected by default
        )
    )

    # Model choice logic
    CLASSES = classes_and_models["model_1"]["classes"]
    MODEL = classes_and_models["model_1"]["model_name"]

    # Display info about model and classes
    st.write(f"See what classes the model can identify: ")
    if st.checkbox("Show classes"): #if box is selected
        st.write(f"You chose {MODEL}, these are the classes of food it can identify:\n", CLASSES)
    
    return CLASSES, MODEL

if __name__ == "__main__":
    # set up title, etc
    page_setup()

    #select model 
    CLASSES, MODEL = model_selection()

    # display file uploader widget, return UploadedFile object
    uploaded_file = st.file_uploader(label="Upload your food image here: ",
                                    type=["png", "jpeg", "jpg"])

    # Setup session state to remember state of app so refresh isn't always needed
    # See: https://discuss.streamlit.io/t/the-button-inside-a-button-seems-to-reset-the-whole-app-why/1051/11 
    session_state = SessionState.get(pred_button=False)

    # Create logic for app flow
    if not uploaded_file:
        st.warning("Please upload an image.")
        st.stop()
    else:
        # read file
        session_state.uploaded_image = uploaded_file.read()
        # display file
        st.image(session_state.uploaded_image, use_column_width=True)
        # display Predict button
        pred_button = st.button("Predict")

    # If user pressed the Predict button
    if pred_button:
        session_state.pred_button = True 

        #predict on image
        session_state.image, session_state.pred_class, session_state.pred_conf = make_prediction(session_state.uploaded_image, model=MODEL, class_names=CLASSES)
        st.write(f"Prediction: {session_state.pred_class}, \
                Confidence: {session_state.pred_conf:.3f}")

