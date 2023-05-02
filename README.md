# WebsitePortfolio

This is my Django app that runs inside a Docker container.

## Prerequisites

Before building and running the application, you need to have the following installed on your machine:

- Docker
- Python 3.x
- pip

## Building and running with Docker

To build and run the application inside a Docker container, follow these steps:

1. Clone the repository:
git clone https://github.com/23BraSut/DjangoProject
or attempt to pull from my docker repo docker pull 23brasut/website:latest

2. Change directory to the project root:

3. Build the Docker image: using
but if you bulid your own image from the cloned repo then you will have to change the name below

4. Run the Docker container:
if you pulled you can run this docker run -p 8000:8000 23brasut/website

5. Access the application at `http://localhost:8000`




