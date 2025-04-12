# End-to-End Project for Detection and Classification of Tomato Diseases.
An AI-powered system that uses computer vision to detect and classify tomato plant diseases, specifically designed to address agricultural challenges. This project aims to provide early disease detection capabilities to help prevent crop losses and improve food security.

## Workflow
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/fosetorico/tomato_disease_classification
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.10 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine
	2. ECR: Elastic Container registry to save your docker image in aws

	#Description: About the deployment

	1. Build docker image of the source code
	2. Push your docker image to ECR
	3. Launch Your EC2 
	4. Pull Your image from ECR in EC2
	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess
	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image

## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	#optinal

	sudo apt-get update -y
	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	sudo usermod -aG docker ubuntu
	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_REGION = 
    AWS_ECR_LOGIN_URI = 
    ECR_REPOSITORY_NAME = 
