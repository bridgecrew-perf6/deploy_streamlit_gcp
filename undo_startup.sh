#delete dummy project
gcloud projects delete streamlit-food-classifier

"""
#auth an account - prompts webpage login
gcloud auth login 

#undo auth for an account
gcloud auth revoke 

#check current project
gcloud config get-value #MY_PROJECT_ID

#set current project
gcloud config set project $MY_PROJECT_ID

#create project 
gcloud projects create $MY_PROJECT_PATH
"""