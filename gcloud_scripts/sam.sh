
#current project (insert your project name here)
PROJECT_ID="food-classifier-example4"
BUCKET="my_bucketey_bucket3"
SERVICE_ACCOUNT="nn-developer-account3"
EMAIL="${SERVICE_ACCOUNT}@${PROJECT_ID}.iam.gserviceaccount.com"
KEY_PATH="app_code"

#login to a cloud account - bring up login prompt in your 
#gcloud auth login

#set current project
gcloud config set project ${PROJECT_ID}

#create bucket for model storage in the current project
#gsutil mb gs://$BUCKET

#upload saved model to bucket
#gsutil cp -r model gs://$BUCKET

### service account setup: https://stackoverflow.com/a/70386020
#create a service account for this project
gcloud iam service-accounts create ${SERVICE_ACCOUNT} \
                    --project=${PROJECT_ID} \
                    --description="streamlit app development"
#create key
# gcloud iam service-accounts keys create ${KEY_PATH}/${PROJECT_ID}.json \
#                     --iam-account=${EMAIL}

#assign role
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
                    --member=serviceAccount:${EMAIL} \
                    --role="roles/ml.developer"