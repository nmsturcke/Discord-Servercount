import sys
sys.path.append(".")

from flask import Flask, redirect, request, render_template
from Main.utilities import *

app = Flask(__name__)

BASE =f"https://discord.com/api/oauth2/authorize?client_id={getConfig()['application_id']}&redirect_uri=http%3A%2F%2F127.0.0.1%3A13337&response_type=code&scope=identify%20guilds"

@app.route("/", methods=["GET"])
def index():
    errors = checkConfig()
    if errors != []:
        return configErrors(errors)
    code = request.args.get("code")

    if code:
        token = Oauth.get_access_token(code)
        if token:
            user_json = Oauth.get_user_json(token)
            guilds_json = Oauth.get_guilds(token)

            identification = user_json["username"] + "#" + user_json["discriminator"]
            user_id = user_json["id"]
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_json['id']}/{user_json['avatar']}"

            admincount = adminPerms(guilds_json)
            ownercount = owner(guilds_json)

            return render_template(
                "index.html",
                identification = identification,
                user_id = user_id,
                avatar_url = avatar_url,
                servercount = str(len(guilds_json)),
                admincount = admincount,
                ownercount = ownercount
            )

            return render_template("index.html", identification=user_json["username"], avatar_url=avatar_url, servercount=len(guilds_json))
            return f"{user_json['username']} is in a total of {str(len(guilds_json))} servers"

    return redirect(BASE)


if __name__ == "__main__":
    configErrors(checkConfig())
    app.run(port=13337, debug=True)