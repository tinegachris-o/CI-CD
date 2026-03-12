# Flask CI/CD Pipeline with Docker and GitHub Actions

## Overview

This project demonstrates a simple Flask API integrated with a CI/CD pipeline.
The pipeline automatically runs tests, builds a Docker image, and pushes the image to Docker Hub whenever code is pushed to the `main` branch.

The project showcases basic DevOps practices including:

* Automated testing
* Containerization with Docker
* Continuous Integration with GitHub Actions
* Image publishing to Docker Hub

---

## Project Structure

```
CICD/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── Pipfile
├── Pipfile.lock
│
├── test/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

## Flask Application

The Flask app exposes a simple endpoint:

```
GET /
```

Response:

```json
{
  "status": "ok",
  "message": "Hello from CI/CD"
}
```

---

## Running the App Locally

Activate the virtual environment:

```
pipenv shell
```

Run the application:

```
python app.py
```

Open in browser:

```
http://localhost:8000
```

---

## Running Tests

Tests are written using **pytest**.

Run tests with:

```
pytest
```

Example test verifies:

* API endpoint works
* HTTP status code is correct
* Response JSON is correct

---

## Docker Setup

Build the Docker image:

```
docker build -t myapp:test .
```

Run the container:

```
docker run -p 8000:8000 myapp:test
```

Test the API:

```
curl http://localhost:8000
```

---

## CI/CD Pipeline

The project uses **GitHub Actions** to automate testing and Docker builds.

Workflow file:

```
.github/workflows/ci-cd.yml
```

Pipeline steps:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Run pytest tests
5. Build Docker image
6. Push Docker image to Docker Hub

---

## Docker Hub Integration

The pipeline pushes images to Docker Hub using repository secrets.

Required secrets:

```
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Images are tagged as:

```
<username>/flask-app-utcli:latest
<username>/flask-app-utcli:<commit_sha>
```

---

## Technologies Used

* Python 3.13
* Flask
* Pytest
* Docker
* GitHub Actions
* Pipenv

---

## Learning Objectives

This project demonstrates how to:

* Build a simple Flask API
* Write automated tests
* Containerize an application
* Implement CI/CD using GitHub Actions
* Push Docker images automatically

---

## Author

Tinega
