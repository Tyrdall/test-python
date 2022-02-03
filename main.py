from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    with open('./templates/home.html', 'r') as template:
        return template.read()


@app.get("/api/boxes/")
def get_boxes():
    return {
        'data': [
            {'title': 'left', 'color': '#837cdf'},
            {'title': 'mid', 'color': '#7c83df'},
            {'title': 'right', 'color': '#df7c83'},
        ],
    }
