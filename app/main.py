from fastapi import FastAPI
from .routes.user import user
from .docs import tags_metadata


app = FastAPI(
	title='REST API with FastAPI & MongoDB'
	, description='This is a simple API of the FaztCode tutorial.'
	, version='0.0.1'
	, openapi_tags=tags_metadata
	)
app.include_router(user)
