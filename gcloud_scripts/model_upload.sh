# upload SavedModel to Google Storage Bucket

#replace with your project and bucket name
PROJECT_ID="food-classifer-example3"
BUCKET="my_bucketey_bucket"

#login to a cloud account - brings up login prompt in browser
#gcloud auth login

# set current project
gcloud config set project ${PROJECT_ID}

# create bucket for model storage in the current project
gsutil mb gs://$BUCKET

# upload saved model to bucket
gsutil cp -r model gs://$BUCKET
