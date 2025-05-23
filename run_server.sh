#! /bin/bash

uvicorn src.infrastructure.fastapi_server:app --reload --port 8000