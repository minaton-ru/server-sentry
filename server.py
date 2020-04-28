import os
from bottle import route
from bottle import run
from bottle import Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://612426b6b954437f8eda7e482aa9ae01@o384400.ingest.sentry.io/5215603",
    integrations=[BottleIntegration()]
)
app = Bottle()

@route('/fail')  
def fail():  
    raise RuntimeError("There is an error!")  
    return  

@route('/success')  
def success():  
    return "success"

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
