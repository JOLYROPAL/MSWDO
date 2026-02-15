FAQ = {
    "aics": "AICS provides medical, food, transport, and burial assistance for individuals in crisis.",
    "4ps": "4Ps is a conditional cash transfer program focused on education and health compliance.",
    "social pension": "Social Pension supports indigent senior citizens with monthly assistance.",
}


def respond(message: str) -> str:
    normalized = message.lower()
    for keyword, reply in FAQ.items():
        if keyword in normalized:
            return reply
    return "Please select a service in the catalog so we can guide you through requirements and forms."
