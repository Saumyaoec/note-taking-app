# Note Taking App

This is a simple note-taking application built with FastAPI and MongoDB.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)


## Introduction

This application allows users to create, read, update, and delete notes. It provides a RESTful API for managing notes and includes authentication features for user signup and login.

## Features

- User authentication (signup, login)
- CRUD operations for notes
- MongoDB integration for data storage

## Installation

To run this application locally, you'll need Python 3.9 and MongoDB installed on your system.

1. Clone this repository:
   ```bash
   https://github.com/Saumyaoec/note-taking-app.git


2.  cd note-taking-app
3.  pip install -r requirements.txt
4.  uvicorn app.main:app --reload
5.  docker build -t note-taking-app .
6.  docker run -d --name note-app-container -p 8000:8000 note-taking-app



