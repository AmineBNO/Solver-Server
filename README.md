# Solver-Server

Step 1 :
This a Python Flask application that return if the string parsed is valid or not.
If the content body of the POST request is empty, the Solver will consume the input from the Generator server created by Arkhn.

Step 2 : 
To dockerize the application, we have to buid image within the Dockerfile.
Docker-Compose is alredy configured to lunch Dockerfile and run a container from the image builded.

Step 3 : 
I used Jenkins as CI Tools to automate the creation of a Docker Image, then push it to DockerHub Repository
