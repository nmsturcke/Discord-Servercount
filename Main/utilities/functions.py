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
    text = f"You need to update the following values in the {crayons.magenta(str(path))} file: " + ", ".join(error for error in errors) + crayons.cyan("\n\nUpdate the file and try to run the script again.")

    print(text)
    exit()
    