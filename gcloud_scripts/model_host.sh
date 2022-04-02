# Host model saved in Google Storage bucket on AI Platform

# replace with your project and bucket name
PROJECT_ID="food-classifier-example4"
BUCKET="my_bucketey_bucket3"
MODEL_NAME="classifier_model1"
MODEL_VERSION='v01'

#login to a cloud account - brings up login prompt in browser
#gcloud auth login

# set current project
gcloud config set project ${PROJECT_ID}

# enable AI platform API
# gcloud services enable ai-platform

# create AI platform model
gcloud ai-platform models create ${MODEL_NAME} \
                            --region=us-central1
# create model version
gcloud ai-platform versions create ${MODEL_VERSION} \
                                --model=${MODEL_NAME} \
                                --region=us-central1 \
                                --machine-type=n1-standard-2 \
                                --origin=gs://$BUCKET/"model" \
                                --framework="tensorflow" \
                                --python-version=3.7 \
                                --runtime-version=2.8 \



