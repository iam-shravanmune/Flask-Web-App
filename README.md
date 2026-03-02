# Flask Application with Docker & CI Pipeline

---

## Project Overview

This project demonstrates the implementation of a modern DevOps workflow by:

- Developing a web application using Flask
- Containerizing the application using Docker
- Deploying to AWS EC2 instance
- Automating build validation using GitHub Actions

The primary focus of this project is to implement Continuous Integration (CI) best practices for a containerized Python application.

---

## Architecture Overview

```
<img width="1000" height="597" alt="diagram-export-3-2-2026-3_38_52-PM" src="https://github.com/user-attachments/assets/67a4443b-c11a-41a1-a1ef-7ad89e0c7557" />

```

---

## Application Layer

The application is built using Flask, a lightweight Python web framework commonly used for building APIs and backend services.

**Features:**
- Simple web server
- Dependency management via requirements.txt
- Docker-compatible structure

---

## AWS EC2 Deployment

This project deploys the Docker container to an AWS EC2 instance.

### Launch EC2 Instance

1. Go to AWS Console → EC2 → Launch Instance
2. Select **Ubuntu Server**
3. Choose instance type (t2.micro for free tier)
4. Configure security group:
   - Open port 80 (HTTP)
   - Open port 22 (SSH)
5. Launch and download key pair (.pem file)

### Connect to EC2 Instance
```
bash
ssh -i "your-key.pem" ec2-user@<ec2-public-ip>
```

### Install Docker on EC2

**For Ubuntu:**
```
bash
sudo apt update
sudo apt install docker.io -y
docker ps
```
### if permission denied by daemon
```
bash
sudo usermod -aG docker $USER
newgrp
```

### Build & Run Container

```
bash
# Build the Docker image
docker build -t flask-app .

bash
#list of Docker image
docker images

# Run the container
docker run -d -p 80:5000 flask-app
docker ps -a
```

### Access the Application

```
http://<ec2-public-ip>
```

---

## Continuous Integration (CI)

This project implements Continuous Integration using GitHub Actions.

**Workflow location:** `.github/workflows/cicd.yml`

### CI Pipeline Execution Flow

On every push to the main branch:

1. GitHub creates a temporary Ubuntu runner
2. The repository is checked out
3. Python 3.10 is installed
4. Project dependencies are installed
5. Python syntax validation is performed
6. Docker image is built
7. Pipeline returns success or failure

---

## CI Workflow Configuration

```
yaml
name: Flask CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Validate Python syntax
      run: python -m py_compile app.py

    - name: Build Docker image
      run: docker build -t flask-app .
```

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## DevOps Concepts Demonstrated

- Continuous Integration (CI)
- Automated build validation
- Docker containerization
- AWS EC2 deployment
- Infrastructure-free CI runners
- Fail-fast pipeline design
- Push-based workflow trigger

---

## Future Enhancements

- Add automated unit testing
- Add code linting (Flake8)
- Implement Continuous Deployment (CD)
- Push Docker image to Amazon ECR
- Use AWS ECS/Fargate for deployment
- Set up Load Balancer with Auto Scaling

---

## Author

**Shravan Mune**  
DevOps Engineer Enthusiast | AWS | Docker | CI/CD | Cloud Technologies
