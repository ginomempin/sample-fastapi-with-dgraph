# FastAPI + GraphQL + dgraph

## REFERENCES

* [Dgraph](https://dgraph.io/)
    * [Why graph databases?](https://dgraph.io/graphdb/)
    * [Dgraph Docs](https://dgraph.io/docs)
        * [Dgraph Overview](https://dgraph.io/docs/dgraph-overview/)
        * [Dgraph + DQL](https://dgraph.io/docs/dql/)
        * [Dgraph + GraphQL](https://dgraph.io/docs/graphql/)
        * [pydgraph](https://dgraph.io/docs/clients/python/)
        * [Deployment and Management](https://dgraph.io/docs/deploy/overview/)
    * [Dgraph Releases](https://dgraph.io/docs/releases/)
* [FastAPI official tutorial on GraphQL](https://fastapi.tiangolo.com/advanced/graphql/)

## SETUP

* Install Python 3.9 (preferrably from Homebrew)
* Install Python packages and activate venv
    ```none
    $ pipenv install --dev --python=/path/to/python3.9
    $ pipenv shell
    ```
* Start the local Dgraph Zero and Alpha instances (in a separate terminal)
    ```none
    $ docker-compose -f deployment/docker-compose.yml up
    ```
    * Test that `pydraph` + local Dgraph is working
        ```none
        $ python tests/simple.py
        Created person named "Alice" with uid = 0x3
        Number of people named "Alice": 1
        Number of people named "Bob": 1
        Bob's UID: 0x4
        Bob deleted
        Number of people named "Alice": 1
        Number of people named "Bob": 0
        DONE!
        ```
* Run the app
    ```none
    $ uvicorn app.service:app --port=8000
    INFO:     Started server process [46253]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```
    * Test that the app is working
        ```none
        $ curl -s http://127.0.0.1:8000/data | jq
        {
          "total_items": 0,
          "items": []
        }
        ```
