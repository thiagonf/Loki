from fastapi import FastAPI
from pydantic import UUID4


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
