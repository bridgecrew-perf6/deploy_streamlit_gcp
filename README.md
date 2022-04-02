# Deep Learning Streamlit app on Google App Engine

I've trained a fine-tuned EfficientNetB0 image classifer in Tensorflow on the food101 dataset and hosted it on Google AI platform. A Streamlit app was built to perform inference on user-uploaded images. This app can be deployed to Google App Engine. I've described the steps I used to deploy the model & app on GCP in the next section.

## What's needed to get started?

- [Git](https://git-scm.com/)
- A [GCP account](https://cloud.google.com/gcp) & a GCP project.
- Install the [glcoud CLI](https://cloud.google.com/sdk/docs/install).
- Trained Tensorflow model. This app performs inference using an image classifer trained on the [Food101 dataset](https://www.tensorflow.org/datasets/catalog/food101).

## Note on repo structure
- ['/app_code/'](/app_code/) contains code that defines Streamlit app, Docker container, and App Engine configuration
- ['/gcloud_scripts/'](/gcloud_scripts/) contains shell scripts used to configure GCP project
- ['/model/'](/model/) is a trained Tensorflow model that is deployed to GCP and used for inference.

## Setting up your Gcloud environment

1. Clone this repo & setup python environment inside app directory:
```
git clone https://github.com/gqmz/deploy_streamlit_gcp.git
cd app_code
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

2. Train model. For convenience, I've uploaded a [copy](model) of the trained model to this repository.

3. GCP project setup
```
# create storage bucket and upload model to it
bash gcloud_scripts/model_upload.sh

# Create AI Platform model & link to model in bucket 
bash gcloud_scripts/model_host.sh

# setup service account with role: AI developer to access model
bash glcoud_scripts/sam.sh
```
In Google Cloud console, create a JSON private key for this service account and download it to the app_code directory. The Streamlit app will use this key for authentication. Do NOT commit this key to github.

## Setting up the application code

In app_code/app.py, update the GCP private key path, project & region
```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<PATH_TO_KEY"
PROJECT = "<PROJECT_NAME>"
REGION = "<GCP_REGION>"
```

In app_code/utils.py, update the model name
```
classes_and_models = {
    "model_1": {
        "classes": base_classes,
        "model_name": "<AI_PLATFORM_MODEL_NAME>" # match MODEL_NAME from gcloud_scripts/model_upload.sh
    },
}
```

## Deploying the Streamlit app locally

With your working directory set to app_code & within an activated py environment, there's 2 ways to run the app locally

```
# through the make file
make run 

# directly through streamlit
streamlit run app.py
```

## Deploying the Streamlit app to Google App Platform

Steps needed to deploy app to App Platform
- Package app into Docker container as defined in ['/app_code/Dockerfile'](/app_code/Dockerfile).
- Upload created Docker image to Google Container Registry
- Now deploy the hosted Docker image on an App Engine Instance (defined by ['/app_code/app.yaml'](/app_code/app.yaml))
These steps are triggered by executing the following command:
```
make gcloud-deploy
```

## Next steps
- Add support for multiple models
- CI/CD support with Github Actions
- Log app data


