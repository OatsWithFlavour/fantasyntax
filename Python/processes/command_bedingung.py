def bedingte_env(muster: dict) -> dict:
    """
    Extrahiert name- und environment-Paare aus dem muster-Dictionary.
    """
    result = {}

    for item in muster.get("command", []):
        item: dict
        if "environment" in item:
            name = item.get("name")
            environment = item.get("environment")
            if name is not None and environment is not None:
                result[name] = environment

    return result
