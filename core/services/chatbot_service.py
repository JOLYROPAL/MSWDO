class ChatbotService:
    def __init__(self):
        self.faq = {
            "aics": "AICS provides temporary support for medical, food, transport, and burial needs. Please prepare complete requirements for verification.",
            "4ps": "4Ps supports qualified households through conditional cash transfers linked to health and education compliance.",
            "social pension": "Social Pension provides monthly assistance for indigent senior citizens subject to eligibility review.",
        }

    def respond(self, message: str) -> str:
        normalized = message.lower()
        for keyword, reply in self.faq.items():
            if keyword in normalized:
                return f"Thank you for contacting DSWD-MS WDO. {reply}"
        return "Thank you for your inquiry. Please select a listed service so we can guide you through official requirements, Citizen's Charter timelines, and the next processing step."
