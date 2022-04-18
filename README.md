[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/VincentLeV/stackoverflow-api-py)

[![License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)

![](https://img.shields.io/github/issues-raw/VincentLeV/stackoverflow-api-py?style=flat-square)
<br/>


# Stackoverflow API

## Table of Contents

[Introduction](#introduction)
<br/>
[Features](#features)
<br/>
[Tech Stack](#tech-stack)
<br/>
[Run The Project Locally](#run-the-project-locally)
<br/>
[Extract Data Only](#extract-data-only)
<br/>
[Demo](#demo)

## Introduction

This is an API that scrapes the newest unanswered question on Stackoverflow by tags.
The API should work with any available tags on Stackoverflow. 

With this API, user could check out the unanswered questions on Stackoverflow quickly without any hassle. 
There is a link for each question that leads straight to Stackoverflow. 

The motivation behind this project is to practice Python, scraping the web and creating data pipeline skills.

## Features

- Can check the unanswered questions by tag
- Can extract data to .csv, .py and .js formats

## Tech Stack

1. Python
2. Jupyter Notebook
3. Requests_html
4. FastAPI
5. Pandas

## Run The Project Locally

In the terminal execute:

Windows

    ./start.ps1

MacOS
    
    ./start.sh

Check the API out at <p align="center">Check the app out at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a></p>

The data will be extracted into different formats after the command and can be found in the "data" folder

## Extract Data Only

Execute the below line in the terminal:

Windows

    ./extract.ps1

MacOS

    ./extract.sh

## Demo

<a href="https://stackoverflow-api-py.herokuapp.com/" target="_blank">
    <p align="center">https://stackoverflow-api-py.herokuapp.com/</p>
</a>