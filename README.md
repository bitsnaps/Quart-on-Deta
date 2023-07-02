# Quart on Deta Space

Create a new replit with Python template, then open the `Shell` tab and follow these steps:

0- Configure tools:
You'll need the `unzip` command in order to install `space` CLI tool:
```bash
#Make sure to install unzip:
apt install unzip
```
P.S. It will be installed into your `replit.nix` in replit.

1- Install Deta CLI:
```bash
curl -fsSL https://get.deta.dev/space-cli.sh | sh
source  ~/.bashrc
```

1- Login to Deta:
Login to your Deta space and create a new project from `Builder` card, then you'll need to get your access token from your project settings then copy/paste it in the console after running this command:
```bash
space login
```
P.S. You wont be able to see your token again once you close the setting, so you'd better store it somewhere (a nice place to do that is your `secrets` tool on Replit, for example to store the Deta project key (e.g. `DETA_PROJECT_KEY`) go to `Replit -> Tools -> Secrets` and create a pair key/value of your token, you can then use it in your code like so:
```python
import os
print(os.getenv("DETA_PROJECT_KEY"))
```

3- Create a new project:
```bash
space new
```
Then follow the instructions...

4- Configure the `Spacefile`:
You then need to configure the `Spacefile` in order to tell Deta how to run your project, the most important pieces are:
- `run`: which tells Deta how to run your project
- `public_routes`: it specify where public files (static, assets, public html...) are located.
You can more options (e.g. environment variables, security settings...) in this file [docs](https://deta.space/docs/en/build/reference/spacefile).
Here is a sample settings to run this app:
```yaml
# Spacefile Docs: https://go.deta.dev/docs/spacefile/v0
v: 0
micros:
  - name: Quart-on-Deta
    src: ./
    engine: python3.9
    run: uvicorn main:app
    primary: true
    public_routes:
      - "/static/*"
#    presets:
#      env:
#        - name: YOUR_ENV_VAR
#          description: Key access to a resource
#          default: "VALUE_OF_YOUR_ENV_VAR"
```
P.S. Notice we used `uvicorn` to run on production instead of running the script with: `python main.py`.
Default port to run your project on Deta is `8080`, so make sure to specify the port in your running function:
```
def run():
  app.run(host='0.0.0.0', port=8080)
```

5- Publish your project:
Once you've finished creating your project you can run it using the following command:
```bash
space push
```
Then open the preview link you see in the console (it looks like `https://{PROJECT-NAME}-{RANDOM-HASH}.deta.app`).
P.S. Don't forget to create `requirements.txt` with your dependencies before pushing to the cloud.


6- Publish a release (Optional):
If you want to share your project with Deta community run this command:
```bash
space release
```
P.S. You can create a `.spaceignore` to untrack files you don't want to deploy.

Read more at:
https://deta.space/docs/en/build/fundamentals/the-space-runtime/configuration#custom-variables

Base Docs
https://deta.space/docs/en/build/reference/sdk/base