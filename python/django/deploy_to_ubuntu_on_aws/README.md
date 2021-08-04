# Basic Deployment onto Ubuntu based EC2 Instance
Do or Run the following steps

## Contents of Directory
- nginx_project.conf
- supervisor_project.conf
- setup.sh (runs once, to setup server)
- update.sh (run every time an update is made)

## 1: Add the 'deploy_pack' onto your django project (Locally)
Deploy directory should be in the root of your project.
Root is where 'manage.py' is.
Must be added on dev/local server

## 2: Create/Update .env file
File must be in root
Add is to .gitignore
Following values must come from .env:
- SECRET_KEY
- DEBUG (True for dev, False for prod)
- API Keys
- DB Creds

## 3: Update git url var inside setup.sh
Change value of PROJECT_GIT_URL into own url
Must be the https link, for now
- PROJECT_GIT_URL

## 4: Update project name inside 'supervisor_project.conf'
Change project_name into current project name inside the following files:
- nginx_project.conf
- supervisor_project.conf
- setup.sh
    - PROJECT_BASE_PATH
    - Supervisor config
    - Nginx config
- update.sh

## 5: Update settings.py
DEBUG = bool(int(os.environ.get('DEBUG', 1)))
SECRET_KEY = os.environ.get('SECRET_KEY', 'DummyKey')
STATIC_ROOT = 'static/'
ALLOWED_HOSTS = ['127.0.0.1',
                'elastic_ip/public_dns',
                ]

## 6: Ensure sh files are executable
chmod +x deploy_pack/*.sh

## 7: PUSH CHANGES TO GITHUB

## 8: SSH into Ubuntu LTS EC2 instance

## 9: Run setup.sh inside the instance
curl -sL https://raw_setup_file_url | sudo bash -

## 10: If any changes have been made in GitHub
cd into PROJECT_BASE_PATH '/usr/local/apps/project_name'
Run 'sudo sh ./deploy_pack/update.sh'
