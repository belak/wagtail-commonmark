from jinja2.ext import Extension

from .templatetags.wagtailcommonmark import commonmark


class CommonMarkExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.filters.update({
            'commonmark': commonmark,
        })


# Nicer import names
commonmark = CommonMarkExtension
