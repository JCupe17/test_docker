# test_docker

This repository presents a solution for the problem [Sparse Array](https://www.hackerrank.com/challenges/sparse-arrays/problem) from HackerRank. 

The *tree* of this repository is:

```bash
├── README.md
├── docker_with_flask
│   ├── Dockerfile
│   ├── input_string.txt
│   ├── main.py
│   ├── requirements.txt
│   ├── sparseArray.py
│   └── swagger_config.yml
└── docker_without_flask
    ├── Dockerfile
    ├── input_string.txt
    ├── main.py
    └── sparseArray.py
```

Description of the files:

* The main differences between both folders are in the files `main.py` and `Dockerfile`.

* The use of Flask and Swagger implies the use of a `requirements.txt` file and the `swagger_config.yml`.

* The file `sparseArray.py` is the same for both folders.

* The file `input_string.txt` is the `INPUT_FILE` for both Dockers. An environment variable was set in the Dockerfile to read this file.

## Using Docker without Flask

The folder `docker_without_flask` includes a solution using Docker and running a query by command line.

To build the Docker image, use the command:

````
docker build . -t test_mdm
````

To run the query, run the folllowing command from the folder:

````
docker run -t test_mdm ab,na,de
````

The last argument of the former command represents the query.

## Using Docker with Flask

The foler `docker_with_flask` includes a solution using Docker, Flask and Swagger for a proper render of the API.

To build the Docker image, use the command:

````
docker build . -t test_mdm
````

The application runs in the port 8791. This port is exposed in the Dockerfile to get access to the app.

To run the application, run the following command from the folder:

````
docker run -p 8791:8791 -t test_mdm
````

The Swagger render of the application will be available on: http://0.0.0.0:8791/swagger/

You will be able to perform a query in the application.


