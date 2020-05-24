# SolarIndex

QA Training Project 


## Project Brief

To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

this meant that i had to create a application which was able to do the following:

* Create

* Read

* Update

* Delete

## Architecture
In this project I have used various technologies

* Source Code: for my source code the main language used was python along with python I also used HTML and Flask

* Version Control: I used Github as my version control system as this was one of the modules i have learnt on the course i would be able                    to pull code to the local area and push code that i had completed to different branches.

* kanban style board: as seen in my pipeline bellow i used trello this was where i was able to set tasks for myself each week to design                       and build my project

* CI Server: Jenkins was the CI server i used for continous integration and would run with Gunicorn

* Cloud server: GCP Compute Engine

[link to my CI Pipeline](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/pipeline2.png)

![Pipeline](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/pipeline2.png) 

The image above is a rough representation of how the application was deployed. The source code was developed in visual studio code and in the ssh terminal here I used python and html along with the framework of flask.After i completed the code i had to push code to github after this the trello was updated.
With Github I created a WebHook between Github and Jenkins would automatically pull the code from GitHub to the CI Server, Jenkins. Using a shell script, the build was made automatically. 

## ERD Diagram 

this is my initial erd 
![ERD](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/solar%20id%20.png)

this is my final erd
![ERD2](

