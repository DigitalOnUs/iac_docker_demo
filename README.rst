Load balanced webserver example
===============================

This is a sample project that shows how to setup a nginx instance as a load balancer for a web application.

Docker images used:
-------------------

- nginx
- python:3.6-alpine

Project tree:
-------------

::

    $ tree
    .
    ├── README.rst
    ├── backend
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── webserver.py
    ├── docker-compose.json
    └── loadbalancer
        ├── Dockerfile
        └── nginx.conf

    2 directories, 7 files

Try it yourself:
----------------

::

    $ docker-compose --file docker-compose.json up -d

    $ docker-compose --file docker-compose.json ps
              Name                    Command          State                Ports
    --------------------------------------------------------------------------------
    proj_angrier-api_1          python webserver.py    Up      8000/tcp
    proj_fortune-api_1          python webserver.py    Up      8000/tcp
    proj_nginx-loadbalancer_1   nginx -g daemon off;   Up      0.0.0.0:49010->80/tcp
    proj_sweetier-api_1         python webserver.py    Up      8000/tcp

See it in action:
-----------------

::

    $ docker-compose --file docker-compose.json logs -f


Open a new terminal and type:
-----------------------------

::

    $ curl --silent --request POST --data '{"who": "slackmart"}' http://localhost:49010/hello-world | python -m json.tool
    {
        "hello": "slackmart",
        "method": "GET",
        "ok": true
    }

    $ for _ in $(seq 1 400); do curl http://localhost:49010/hello-world ; done

What you should see in the docker compose logs:
-----------------------------------------------


::

    sweetier-api_1        | [2018-09-20T03:37:14+00:00] - 172.18.0.2 - "GET /hello-world" - 200 - curl/7.61.0
    sweetier-api_1        | [2018-09-20T03:37:14+00:00] - 172.18.0.2 - "GET /hello-world" - 200 - curl/7.61.0
    nginx-loadbalancer_1  | [20/Sep/2018:03:37:14 +0000]: POST /hello-world HTTP/1.1 from: 172.18.0.1 => to: 172.18.0.3:8000
    nginx-loadbalancer_1  | [20/Sep/2018:03:37:14 +0000]: POST /hello-world HTTP/1.1 from: 172.18.0.1 => to: 172.18.0.5:8000
    nginx-loadbalancer_1  | [20/Sep/2018:03:37:14 +0000]: POST /hello-world HTTP/1.1 from: 172.18.0.1 => to: 172.18.0.4:8000
    nginx-loadbalancer_1  | [20/Sep/2018:03:37:14 +0000]: POST /hello-world HTTP/1.1 from: 172.18.0.1 => to: 172.18.0.5:8000
    fortune-api_1         | [2018-09-20T03:37:14+00:00] - 172.18.0.2 - "GET /hello-world" - 200 - curl/7.61.0
