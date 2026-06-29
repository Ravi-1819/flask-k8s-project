# 🚀 Flask Kubernetes Deployment Project

> A simple Python Flask application deployed on Kubernetes (Kind) using Docker on AWS EC2.

---

## 📌 Project Overview

This project demonstrates how to:

* 🐍 Build a Python Flask application
* 🐳 Containerize it using Docker
* ☸️ Deploy it on a Kubernetes (Kind) cluster
* 🌐 Expose it using a NodePort Service
* ☁️ Run it on an AWS EC2 instance
* 📦 Manage source code with GitHub

---

## 🛠️ Tech Stack

| Technology        | Description             |
| ----------------- | ----------------------- |
| Python            | Backend Application     |
| Flask             | Web Framework           |
| Docker            | Containerization        |
| Kubernetes (Kind) | Container Orchestration |
| AWS EC2           | Cloud Infrastructure    |
| Git               | Version Control         |
| GitHub            | Source Code Hosting     |

---

## 📂 Project Structure

```text
flask-k8s-project/
├── app.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── requirements.txt
└── README.md
```

---

## 🚀 Docker Build

```bash
docker build -t flask-k8s:v2 .
```

---

## 📦 Load Image into Kind

```bash
kind load docker-image flask-k8s:v2 --name devops
```

---

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## 📊 Verify Resources

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
```

---

## 🌍 Access Application

```bash
kubectl port-forward service/flask-service 5000:5000
```

Open in your browser:

```text
http://localhost:5000
```

---

## 🎯 Features

* ✅ Dockerized Flask Application
* ✅ Kubernetes Deployment
* ✅ Rolling Updates
* ✅ NodePort Service
* ✅ AWS EC2 Deployment
* ✅ GitHub Version Control

---

## 📸 Screenshots

Add screenshots here:

* Home Page
* Running Pods
* Services
* GitHub Repository

---

## 👨‍💻 Author

**Ravi Singh**

GitHub: https://github.com/Ravi-1819

⭐ If you like this project, don't forget to star the repository!
