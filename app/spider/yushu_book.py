from flask import current_app


class YuShuBook:
    def search_by_keywords(self, q):
        config = current_app.config
