# Deep Learning Streamlit app on Google App Engine

I've trained a fine-tuned EfficientNetB0 image classifer in Tensorflow on the food101 dataset and hosted it on Google AI platform. A Streamlit app was built to perform inference on user-uploaded images. This app can be deployed to Google App Engine. I've described the steps I used to deploy the model & app on GCP in the next section.

## What's needed to get started?
- [Git](https://git-scm.com/)
- A [GCP account](https://cloud.google.com/gcp) & a GCP project.
- Install the [glcoud CLI](https://cloud.google.com/sdk/docs/install).
- Trained Tensorflow model. This app performs inference using an image classifer trained on the [Food101 dataset](https://www.tensorflow.org/datasets/catalog/food101).

## Setting up your environment

1. Clone this repo & setup python environment inside app directory:
```
git clone https://github.com/gqmz/deploy_streamlit_gcp.git
cd app_code
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

2. Train model. For convenience, I've uploaded a [copy](model) of the trained model to this repository. Alternatively, use the notebook to train a model.

3. Some setup for the GCP project
```
# upload model to created storage bucket
bash gcloud_scripts/model_upload.sh

# Create AI Platform model & add link to model in bucket 
bash gcloud_scripts/model_host.sh

# setup service account
bash glcoud_scripts/sam.sh
```
In Google Cloud console, create a JSON private key for this service account and download it to the app_code directory. The Streamlit app will use this key for authentication. Do NOT commit this key to github.


