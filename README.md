## Meme Generator

In this project, I am using Python as programming language - and the skills I've developed throughout this course.

Also before actiual implementations, I have installed several open libraries to get the things going.

#### Overview

In this project, we are detecting the data inside different file types present like .pdf,.csv,.docx etc.

Once we are aware about the data we are extracting the data by printing at console by using different Imparsor functions.

Then we are using Pillow library of python to work with the images and putting the text data of extracted imparser functions over image by creating random function generators.

The html files and basics templates are already available with us in the starter code.

#### Setting up and running the program

We will use different libraries listed below to perform different set of operations in our project.

***import sys***

We are using sys library of python with argv to get the specific arguments passed to command line interface(cli) by user.

***import subprocess***

To use other software that is available from the command line within our Python application , we can use a Python module called subprocess. Subprocess will allow us to interface with software that we'd normally execute from a terminal window.

***import random***

Used to generate the random number or choice to use in different applications like getting random choices or getting random numbers etc.

***import requests***

The HyperText Transfer Protocol (HTTP) is the protocol—or set of rules—governing how requests are sent over the Internet, and it has a clear and rigid definition for how requests can be made.

 A network command is often referred to as a request and structured command sent over a network between two computers.

**To work with pdf files and parse those data we need pdftotext converter**

To download pdftotext converter, go to "[Download Xpdf and XpdfReader](https://www.xpdfreader.com/download.html)" and download the zip file at ### Download the Xpdf command line tools and once done set the path variable of system with bin address location of tool.



To work with Python library for creating and updating Microsoft Word (.docx) files we use *python-docx*

*pip install python-docx*

To work with .csv or excel files we use pandas library:

*pip install pandas*

##### Folder structure formed during project work

_data : this folder contains all the required datasets to work with Quote Engine and MemeEngine.

MemeEngine : This folder has files to process the images using pillow and related libraries and the __init__.py file to convert the folder into the directory where we can call the classes and functions defined in other files/directories.

QuoteEngine : Converted the pdf,docx and csv datasets into the importer functions and then again used init.py file to import all the classes and functions to use them outside as a structured objects.

#### virtual environment creation

To perform all the above operations, I have created seperate virtual environment where I have installed several dependancies of project.

#installing venv
py -m pip install --user virtualenv
#creating virtual env
py -m venv env
#activating virtual env
.\env\Scripts\activate

#### How to start flask server

Step1 : Export the variable FLASK_APP and assign it to script we are working with .

            For windows, use set instead of export

export FLASK_APP = app.py **or** set FLASK_APP = app.py

step 2 :  Type below command in conda prompt to run the server 

        flask run --host 0.0.0.0 --port 3000

#### Importing files and functions across files examples

***Partial Import without aliasing***
    from urllib import request

***Releative imports***

    from .aloha import say_hi

    from .adios import say_goodbye

Note : Here say_hi is function name in aloha.py file and we are writing this relative import in __init__.py file


