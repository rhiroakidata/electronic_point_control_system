# electronic_point_control_system

Project for PontoTel recruitment process. The challenge is create a system for controlling the time of a company's employees. The construction of this system is consisted of three stages: 

1. Model and create a database with two models: Contributor and Ponto

2. Creation of REST APIs to communicate with this database

3. Unit tests for APIs

## Getting Started (Without/with Docker)

First clone git project.

```
git clone https://github.com/rhiroakidata/electronic_point_control_system.git
```

Go to the project

```
cd eletronic_point_control_system/
```

For running MongoDB, it was used Docker, so first install Docker clicking [here](https://docs.docker.com/engine/install/ubuntu/).

After that, run the command below
```
docker run --name mongo-latest -p 27017:27017 -d mongo
```

### Without Docker

After, create virtual environment

```
python3 -m venv ./venv
```

Activate your virtual environment

```
source venv/bin/activate
```

Install dependencies of project

```
pip3 install -r requirements/dev.txt
```

Finally, run project

```
make run
```

For testing project, run

```
make test
```

### With docker

Please run the following command:
```
docker build -t api_pontotel:latest .
```

As result, created Docker image, after execute command below for creating Docker container:
```
docker run -itd --name api_pontotel_latest -p 5001:5000  -e SECRET_KEY=hard-secret-key --link mongo-latest:dbserver -e MONGODB_URI=mongodb://dbserver:27017/api-pontotel api_pontotel:latest
```

## Additional

This topic is optional, here explain how to prepare your Operational System and Virtual Environment for running mask detector. Well, let`s start!

1. First update your Ubuntu System
```
sudo apt-get update
sudo apt-get upgrade
```

2. Install image and video I/O libraries and useful packages
```
sudo apt-get install build-essential cmake unzip pkg-config

sudo apt-get install libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev

sudo apt-get install libjpeg-dev libpng-dev libtiff-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk-3-dev

sudo apt-get install libopenblas-dev libatlas-base-dev liblapack-dev gfortran

sudo apt-get install libhdf5-serial-dev

sudo apt-get install python3-dev python3-tk python-imaging-tk

3. Install Python libraries
```
pip install numpy

pip install opencv-contrib-python

pip install imutils
```

4. Install Tensorflow
```
pip install tensorflow
```

5. Enable the route and service

Uncomment this file /media/hiroaki/DATA/workspace/electronic_point_control_system/apps/bonus/services.py

Also, uncomment the route '/mask-detector' in api.py

Then, save both files.

## Built With

* [Python 3](https://www.python.org/) - Programming language used
* [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/) - The web framework used
* [Pytest](https://docs.pytest.org/en/latest/) - Test framework used
* [MongoEngine](http://mongoengine.org/#home) - ORM tool for MongoDB database
* [Visual Studio Code](https://code.visualstudio.com/docs) - IDE used

## Authors

* **Rodrigo Hiroaki Ideyama** - *Initial work* - [rhiroakidata](https://github.com/rhiroakidata)

## Acknowledgments

* PontoTel
* PyImageSearch
* StackOverflow
