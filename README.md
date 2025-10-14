# Flask DevOps App

!CI/CD

This is a simple Flask app containerized with Docker and deployed using GitHub Actions.

## 🛠️ Tech Stack
- Python 3.11
- Flask
- Docker
- GitHub Actions
- AWS EC2
- Gunicorn

## 🎯 Learning Objectives
- Containerize an application with Docker
- Set up automated CI/CD pipelines with GitHub Actions
- Deploy to AWS EC2
- Implement basic DevOps best practices
- Troubleshoot real-world deployment issues

## 🧱 Architecture

GitHub Repo → GitHub Actions → Docker Build → Docker Hub → AWS EC2 → Running App

## ✅ Health Check
Visit `/health` endpoint to verify deployment status.

## 📁 Project Structure
# Triggering workflow
# Re-triggering workflow

<!-- Triggered Docker build via GitHub Actions -->  

<!-- Trigger EC2 deployment test -->