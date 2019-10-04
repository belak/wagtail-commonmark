from jinja2.ext import Extension

from .templatetags.wagtailcommonmark import commonmark as commonmark_filter


class CommonMarkExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.filters.update({
            'commonmark': commonmark_filter,
        })


# Nicer import names
commonmark = CommonMarkExtension
