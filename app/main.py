from fastapi import FastAPI
from pydantic import UUID4

from jsons.service_example.response_example import (
    GET_EXAMPLE_SERVICE_JSON, GET_RANDOM_EXAMPLE_SERVICE_JSON)
from tags import tags_metadata


description = """
You know when you have no way out to solve a problem, one of the best
things you can use is magic! When you need several services
communicating to be able to test a feature, it can be quite
complex to prepare all the necessary infrastructure. Another
problem is when services that are available in staging and
devint environments do not have cohesive data. There is
nothing better than asking the God of lies Loki for help and
creating a great illusion between the services in a local and
simple way.
"""

app = FastAPI(
    docs_url="/",
    title="Loki - Fake Services",
    description=description,
    version="1.0.0",
    contact={
        "name": "Thiago Nogueira Freire",
        "email": "thiagonf10e@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


@app.get("/service-example/v1/user/{id}",
         tags=["Service Example"])
def get_user(id: UUID4):
    mock_response = GET_EXAMPLE_SERVICE_JSON
    mock_response["id"] = id
    return mock_response


@app.get("/service-example/v1/user/order/{id}",
         tags=["Service Example"])
def get_user_order(id: UUID4):
    mock_response = GET_RANDOM_EXAMPLE_SERVICE_JSON
    mock_response["id"] = id
    return mock_response
