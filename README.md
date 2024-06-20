# Object Detection App

This repository contains an object detection application built with TensorFlow, OpenCV, and deployed on Kubernetes.

## Project Overview

The Object Detection App uses a pre-trained SSD MobileNet V2 model from TensorFlow Hub to detect objects in images. The application is containerized using Docker and deployed on a Kubernetes cluster.

## Contents

- `app.py`: The main application script that performs object detection on an input image.
- `Dockerfile`: The Dockerfile used to build the container image for the application.
- `deployment.yaml`: The Kubernetes deployment and service configuration file.
- `.devcontainer/`: Configuration files for setting up the development environment in GitHub Codespaces.

## Prerequisites

- Docker
- Kubernetes cluster (local or cloud-based)
- kubectl
- GitHub account
