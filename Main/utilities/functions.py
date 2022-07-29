import sys
sys.path.append(".")

import json, os, crayons

def getConfig() -> dict:
    """
    Gets the setup configuration.

    :returns: dict
    """

    with open("./Main/config/config.json", "r") as f:
        return json.load(f)

def checkConfig() -> list:
    """
    Checks the configuration to see if everything is properly setup, returns the keys with errors (if any)
    
    :returns: list
    """

    config = getConfig()
    errors = []

    for key, value in config.items():
        if value is None or value == "":
            errors.append(key)
    
    return errors

def configErrors(errors: list = []) -> None:
    """
    Kills the program and raises the errors.
    
    :param errors: The list of errors that need to be changed
    :type errors: list
    :returns: None
    """

    if errors == []:
        return

    path = os.path.abspath("./Main/config/config.json")
    text = crayons.red(f"[ERROR] You need to update the follwing values in the {path} file: " + crayons.white(", ".join(error for error in errors)) + crayons.cyan("\n\nUpdate the file and run the script again."))

    print(text)
    exit()

def adminPerms(guilds: list = []) -> int:
    """
    Returns the amount of guilds you have admin perms in.
    
    :param guilds: The guilds json response
    :type guilds: list
    :returns int:
    """

    t = 0

    for g in guilds:
        if int(g["permissions_new"]) & 8 == 8:
            t += 1

    return t

def owner(guilds: list = []) -> int:
    """
    Returns the amount of guilds you are owner in.
    
    :param guilds: The guilds json response
    :type guilds: list
    :returns int:
    """

    t = 0

    for g in guilds:
        if g["owner"] == True:
            t += 1

    return t

def moderator(guilds: list = []) -> int:
    """
    Returns the amount of guilds you are moderator in, checking for Manage Messages permission.
    
    :param guilds: The guilds json response
    :type guilds: list
    :returns int:
    """

    t = 0

    for g in guilds:
        if int(g["permissions_new"]) & 13 == 13:
            t += 1
    
    return t