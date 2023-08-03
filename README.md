# Machine-Learning-Project2
This is my second machine learning project 

## Software and account Requirement. 

1. [Github Account](https://github.com)
2. [Heroku Account](https://signup.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = anishyadav7045075175@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```
To check running container in docker
```
docker ps
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```



Tos stop docker conatiner
```
docker stop <container_id>
```

To install all the libraries mention after creating setup.py file 

'''
python setup.py install
'''

Install ipynbkernel
'''
pip install ipykernel
'''
