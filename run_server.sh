#! /bin/bash

uvicorn app.infrastructure.fastapi_server:app --reload --port 3000