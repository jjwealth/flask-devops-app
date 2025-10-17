# Flask DevOps App

DevOps Project Lab: Containerized Application Deployment

![CI/CD](https://github.com/jjwealth/flask-devops-app/actions/workflows/deploy.yml/badge.svg)


Engineer: Joshua Wealth
Supervisor: Snr. DevOps, Engr. John
Project Title: Flask DevOps App – Automated CI/CD Deployment using Docker, GitHub Actions, and AWS EC2

Project Overview

This project demonstrates a complete DevOps automation pipeline for deploying a Python Flask web application using Docker containers, GitHub Actions, and AWS EC2.
The objective is to implement continuous integration and continuous deployment (CI/CD) that automatically builds, tests, and deploys an application every time changes are pushed to GitHub.



## 🛠️ Tech Stack
- Tool: Purpose
- Python 3.11 + Flask	Web Application Framework
- Docker Containerization
- DockerHub	Image Registry
- GitHub Actions	CI/CD Automation
- AWS EC2 (Amazon Linux 2023)	Deployment Server
- Gunicorn (optional)	Production WSGI Server


## 🎯 Learning Objectives
- Containerize an application with Docker
- Set up automated CI/CD pipelines with GitHub Actions
- Deploy to AWS EC2
- Implement basic DevOps best practices
- Troubleshoot real-world deployment issues

## 🧱 Architecture:

Developer → GitHub → GitHub Actions → Docker Build → DockerHub → AWS EC2 → Running Flask App:

1. Developer pushes code to GitHub (main branch)

2. GitHub Actions triggers automatically

3. The workflow:

    - Builds a Docker image from the app

    - Pushes it to DockerHub

    - Connects to EC2 via SSH

    - Pulls and runs the latest image

4. EC2 hosts the running containerized app, accessible via its public IP on port 5000.



## ✅ Health Check
Visit `/health` endpoint to verify deployment status.

## 📁 Project Structure
# Triggering workflow
# Re-triggering workflow

<!-- Triggered Docker build via GitHub Actions -->  

<!-- Trigger EC2 deployment test -->