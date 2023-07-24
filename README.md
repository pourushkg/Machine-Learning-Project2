# Machine-Learning-Project2
This is my second machine learning project 

## Software and account Requirement. 

1. [Github Account](https://github.com)
2. [Heroku Account](https://signup.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

## Creating cond environment 

'''
conda create -p venv python==3.7 -y
'''

## To Activate virtual environment 

'''
conda activate venv/
'''
## To install the required libraries 
'''
pip install -r requirements.txt
'''
## To create a .gitignore file
'''
touch .gitignore
'''

## To add file to git 
'''
git add. 
'''
or 
'''
git add <file_name>
'''
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file. 

To check the git status 
'''
git status
'''
To check all version maintained by git
'''
git log
'''

To create version/commit all changes by git 
'''
git commit -m "message"

To change/version to git hub 

'''
git push origin main
'''

To get remote url 

''' 
git remote -v
'''


BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .

> Note: Image name for docker must be lowercase 

To list docker images 
'''
docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 d7f2f1e326e2

To check running container in docker
'''
docker ps
'''
To stop any docker container
'''
docker stop <container_id>
