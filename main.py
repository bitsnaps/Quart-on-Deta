from quart import Quart, render_template, websocket
#import os

# Use this in case you want to get an env var
#origin = f"https://{os.getenv('DETA_SPACE_APP_HOSTNAME')}"
#api_key = os.getenv("DETA_API_KEY")

#app = Quart(__name__)
app = Quart(__name__, static_folder="./static", static_url_path="/assets")


@app.route("/")
async def hello():
  return await render_template("index.html")


@app.route("/api")
async def json():
  return {"hello": "world"}


@app.websocket("/ws")
async def ws():
  while True:
    #await websocket.send("hello")
    await websocket.send_json({"hello": "World"})


# Use this function if you're running from uvicorn
def run() -> None:
  # specifying the "port=8080" is optional when using the full hostname
  #app.run(host=os.getenv('DETA_SPACE_APP_HOSTNAME'))
  app.run(host='0.0.0.0', port=8080)


# You can run directly from the shell python using (python main.py):
#if __name__ == "__main__":
#app.run(host='0.0.0.0', debug=True) # if you're running this app on local
#  app.run(host='0.0.0.0', port=8080)
