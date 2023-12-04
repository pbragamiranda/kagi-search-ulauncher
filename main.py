import webbrowser
from ulauncher.api.client import (
    JsonRPC2Request,
    JsonRPC2Notification,
    JsonRPC2Response,
)
from ulauncher.api.Extension import Extension
from ulauncher.api.shared.action.BaseAction import BaseAction

class OpenKagiSearchAction(BaseAction):
    def run(self, keyword):
        search_url = f"https://kagi.com/search?q={keyword}"

        try:
            webbrowser.open(search_url)
        except Exception as e:
            print(f"Error: {e}")

class KagiSearchExtension(Extension):
    def __init__(self):
        super(KagiSearchExtension, self).__init__()
        self.subscribe(JsonRPC2Request, JsonRPC2Response, JsonRPC2Notification)

    def initialize(self):
        # Register the action
        self.register_action("open_kagi_search", OpenKagiSearchAction())

    def handle_query(self, query, items_requested):
        if query:
            # Trigger the action with the query as a parameter
            return [OpenKagiSearchAction(keyword=query).get_result()]

if __name__ == "__main__":
    KagiSearchExtension().run()
