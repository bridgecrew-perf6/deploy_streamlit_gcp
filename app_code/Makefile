# https://dev.to/mcaci/the-meaning-of-the-phony-target-inside-a-makefile-4fj8
.PHONY: run run-container gcloud-deploy

APP_NAME ?= app_code #set to app directory

run:
	@streamlit run app.py --server.port=8080 --server.address=0.0.0.0

run-container:
	@docker build . -t ${APP_NAME}
	@docker run -p 8080:8080 ${APP_NAME}

# deploy the local code and/or configuration of your app to App Engine 
# app.yaml: App Engine settings
gcloud-deploy:
	@gcloud app deploy app.yaml

