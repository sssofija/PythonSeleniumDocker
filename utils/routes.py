ROUTES = {
    "base": "https://demoqa.com",
    "text_box": "/text-box",
    "checkbox": "/checkbox",
    "radio_button": "/radio-button",
    "buttons": "/buttons",
    "webtables": "/webtables"
}

def get_url(route_key: str) -> str:
    base = ROUTES["base"]
    path = ROUTES.get(route_key)

    if not path:
        raise ValueError(f"No route found for key: {route_key}")

    return f"{base}{path}"
