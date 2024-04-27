from fastapi import FastAPI
from src.v1.gateways.http import AppRoute
from config.database import init_db
from config.loader import ConfigLoad as cfg

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)
# register http route
app.include_router(AppRoute)

# init db model
init_db()

# grpc
# tbd

# run fast api
# uvicorn main:app --reload
if __name__ == '__main__':
    import uvicorn
    if cfg['env'] == 'PRODUCTION':
        uvicorn.run(app='main:app', host=cfg['http']['host'], port=cfg['http']['port'], workers=cfg['http']['worker'])
    else:
        uvicorn.run(app='main:app', host=cfg['http']['host'], port=cfg['http']['port'], reload=True)