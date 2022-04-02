# GCP uses Cloud Build to build Docker containers

# create this py environment in a container, should match AI platform version (see gcloud_scripts/model_host.sh)
FROM python:3.7

## App engine stuff
# Expose port 8080 on the App Engine computer, app will be served here
EXPOSE 8080

# Upgrade pip in container environment
RUN pip install -U pip

# convention: if running Docker on App Engine, put all application code in app (dir inside container)
COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

# copy everything in cwd (app_code) into Docker's app
COPY . /app
# change DOcker working dir
WORKDIR app

# Run once container is built
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

# built container is pushed to GCR
# if docker container is too large, it may take too long to build & hit CB's timeout limit -> use .dockerignore to remove unnecessary items from app_code
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv