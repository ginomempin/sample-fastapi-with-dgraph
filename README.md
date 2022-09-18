# FastAPI + GraphQL + dgraph

## REFERENCES

* [Dgraph](https://dgraph.io/)
    * [Dgraph Releases](https://dgraph.io/docs/releases/)
    * [Why graph databases?](https://dgraph.io/graphdb/)
    * [Dgraph Overview](https://dgraph.io/docs/dgraph-overview/)
    * [Dgraph + DQL](https://dgraph.io/docs/dql/)
    * [Dgraph + GraphQL](https://dgraph.io/docs/graphql/)
    * [GraphQL vs DQL](https://dgraph.io/blog/post/graphql-vs-dql/)
    * [pydgraph](https://dgraph.io/docs/clients/python/)
    * [Deployment and Management](https://dgraph.io/docs/deploy/overview/)
* [FastAPI + GraphQL](https://fastapi.tiangolo.com/advanced/graphql/)

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

## NOTES

### [GraphQL vs DQL](https://dgraph.io/blog/post/graphql-vs-dql/)

> With Dgraph, if you provide a GraphQL schema, a DQL schema will be generated, but if you only provide a DQL schema, then a GraphQL schema will not be generated.

> A DQL schema is predicate-first focused and supports some aspects not yet supported by the GraphQL syntax such as multi-lingual predicates and facets (data information stored on edges between nodes). A GraphQL schema is type-first focused and only supports spec-compliant elements such as `type`s, `unions`, and `interfaces`. DQL does not support unions or interfaces but can still correctly represent GraphQL schemas containing such elements.

> The schemas will need indexes applied to enable searching, and the GraphQL schema must have [directives](https://dgraph.io/docs/graphql/directives/) applied to it for Dgraph to generate the correct DQL indexes, map inverse relationships, and inform endpoint functions of identifiers to use in the DQL schema.

> Dgraph provides a GraphQL endpoint to provide access from frontend clients directly to the database in a secure and manageable manner. Dgraph provides developers with a toolset of directives to apply in the GraphQL schema that apply business logic rules such as authorizing access to data and applying constraints that otherwise do not exist in the database itself.

> Dgraph at its core uses a single query language, DQL. Any incoming GraphQL queries or mutations are rewritten on the fly within the core functions into DQL, which are then understood by the database. ... With this knowledge, it is easy to understand that anything that can be done in GraphQL can be done in DQL, but the opposite is not necessarily true. Some queries and mutations are possible in DQL that are simply not possible in GraphQL, mainly due to the restriction of the GraphQL specification itself being a strictly typed query language, and DQL being a loosely typed graph query language that can even work without a predefined schema.

> GraphQL provides clients with a strictly controlled query and mutation endpoint that developers can tightly control while DQL provides developers with a more flexible graph query language to control their data in ways outside of the normal use cases of front-end applications.

> DQL can be considered a direct raw graph database query language that's similar to other database direct languages such as SQL, Cypher, or Gremlin while GraphQL should be thought of as an API endpoint to access the database in a controlled manner.
