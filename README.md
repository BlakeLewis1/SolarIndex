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

## Scope and requiremnets

The requirements set for the project are below. Note that these are a
minimum set of requirements that you can add to during the project.

The requirements of the project are as follows:

* A Trello board (or equivalent Kanban board tech) with full expansion
  on user stories, use cases and tasks needed to complete the project.
  It could also provide a record of any issues or risks that you faced
  creating your project.

* A relational database used to store data persistently for the
  project, this database needs to have at least 2 tables in it, to
  demonstrate your understanding, you are also required to model a
  relationship.

* Clear Documentation from a design phase describing the architecture
  you will use for you project as well as a detailed Risk Assessment.
  A functional CRUD application created in Python, following best
  practices and design principles, that meets the requirements set on
  your Kanban Board

* Fully designed test suites for the application you are creating, as
  well as automated tests for validation of the application. You must
  provide high test coverage in your backend and provide consistent
  reports and evidence to support a TDD approach.

* A functioning front-end website and integrated API's, using Flask.
  Code fully integrated into a Version Control System using the
  Feature-Branch model which will subsequently be built through a CI
  server and deployed to a cloud-based virtual machine.

## Project Tracking 

[Trello](https://trello.com/b/Lfj9XdE4/solarindex)

[User Stories](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/User%20stories.pdf)

[MOSCOW](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/MOSCOW.pdf) 

[Risk Assessment](

This was one of the first things I completed in my project as it was important to get done inorder to be able to complete the project in time and to a good quality. this would help the project to be planned properly. In addition to creating a plan I would need to create user stories as well in order to structure priorties in the project and gain an idea of what the project would entail, these would be created in a word document and not included on the trello. I would also add colours to the different cards on trello to indicate piority this followed the following pattern:

* Red - crucial 

* Yellow -  important

* Green - not important 
In addition to this to order my piorties whilst developing my project i have created a document called MOSCOW this orders features of the project in Must haves, Should haves and Could haves. this helps me as it means that i spend time working on the most important tasks  


## Architecture
In this project I have used various technologies

* Source Code: for my source code the main language used was python along with python I also used HTML and Flask

* Version Control: I used Github as my version control system as this was one of the modules i have learnt on the course i would be able                    to pull code to the local area and push code that i had completed to different branches.

* kanban style board: as seen in my pipeline bellow i used trello this was where i was able to set tasks for myself each week to design                       and build my project

* CI Server: Jenkins was the CI server i used for continous integration and would run with Gunicorn

* Cloud server: GCP Compute Engine

![Pipeline](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/pipeline2.png) 

The image above is a rough representation of how the application was deployed. The source code was developed in visual studio code and in the ssh terminal here I used python and html along with the framework of flask.After i completed the code i had to push code to github after this the trello was updated.
With Github I created a WebHook between Github and Jenkins this would automatically pull the code from GitHub to the CI Server, Jenkins. Using a shell script, the build was made automatically. 

## ERD Diagram 

This is my initial erd: 
![ERD](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/solar%20id%20.png)
Some of the tables in this ERD were unnecessary and not really needed for the web app so I took some time to simplify the erd diagram as i believed making a this many tables would lead to issues with the time constraint of the project 

This is my final erd:
![ERD2](https://github.com/BlakeLewis1/SolarIndex/blob/master/Documentation/solar_id%20ERD.png) 

## Testing 

Testing was completed using pytest as shown in my pipeline i completed testing with a 89% coverage using only unit tests this was due time constraints  


