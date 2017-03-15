# Project-5
 Project 5: Feature Selection + Classification

## Domain and Data

You're working as a data scientist with a research firm. You're firm is bidding on a big project that will involve working with thousands or possible tens of thousands of features. You know it will be impossible to use conventional feature selection techniques. You propose that a way to win the contract is to demonstrate a capacity to identify relevant features using machine learning. Your boss says, "Great idea. Write it up." You figure that working with the Madelon synthetic dataset is an excellent way to demonstrate your abilities.

A data engineer colleague sets up a remote PostgreSQL database for you to work with. You can connect to that database at " " with user dsi and password " ". You can connect via command line using

$ psql -h joshuacook.me -p 5432 -d dsi -U dsi_student
and entering the password when prompted

(Optional) You tell your colleague, thanks, but you prefer to run your database locally using docker.
Regardless of whether you use the remote database or Docker, your colleague encourages you to use sqlalchemy to connect postgres to pandas. He suggests that the following code might be useful but seems distracted and rushed and tells you to check stack when you push for more:

engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(user, password, url, port, database))
Problem Statement

Your challenge here is to implement three machine learning pipelines designed to demonstrate your ability to select salient features programatically.

## Solution Statement

Your final product will consist of:

A prepared report
Three Jupyter notebooks to be used to control your pipelines
A library of python code you will use to build your pipelines

Pipeline 1: Benchmarking



Pipeline 2: Select Features with l1 - Penalty



Pipeline 3: Build Model with Grid Search
