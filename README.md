# test_docker

This repository presents a solution for the problem [Sparse Array](https://www.hackerrank.com/challenges/sparse-arrays/problem) from HackerRank. 

The *tree* of this repository is:

```bash
├── README.md
├── docker_with_flask
└── docker_without_flask
    ├── Dockerfile
    ├── input_string.txt
    ├── main.py
    └── sparseArray.py
```

## Using Docker without Flask

The folder *docker_without_flask* presents a solution using Docker and running a query by command line.

To build the Docker image, use the command:

````
docker build . -t test_mdm
````

To run the query, run the folllowing commands from the folder:

````
docker run -t test_mdm ab,na,de
````

The last argument of the former command represents the query.

## Using Docker with Flask



