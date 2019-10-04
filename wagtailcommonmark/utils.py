from django import forms
from django.utils.encoding import smart_text
from django.utils.safestring import mark_safe

import bleach
import commonmark


MARKDOWN_TAGS = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'b', 'i', 'strong', 'em', 'tt',
    'p', 'br',
    'span', 'div', 'blockquote', 'pre', 'code', 'hr',
    'ul', 'ol', 'li', 'dd', 'dt',
    'img',
    'a',
    'sub', 'sup',
]
MARKDOWN_ATTRS = {
    '*': ['id'],
    'img': ['src', 'alt', 'title'],
    'a': ['href', 'alt', 'title'],
}


def render_commonmark(text, context=None):
    """
    Turn commonmark into HTML.
    """
    if context is None or not isinstance(context, dict):
        context = {}
    commonmark_html = _transform_commonmark_into_html(text)
    sanitised_commonmark_html = _sanitise_commonmark_html(commonmark_html)
    return mark_safe(sanitised_commonmark_html)


def _transform_commonmark_into_html(text):
    return commonmark.commonmark(smart_text(text))


def _sanitise_commonmark_html(commonmark_html):
    return bleach.clean(
        commonmark_html,
        tags=MARKDOWN_TAGS,
        attributes=MARKDOWN_ATTRS)


class CommonMarkMedia:
    """
    Mixin providing the common JS and CSS for the CommonMark admin panels
    """
    @property
    def media(self):
        return forms.Media(
            css={
                'all': (
                    'wagtailcommonmark/css/codemirror.custom.css',
                    'wagtailcommonmark/css/codemirror.css',
                )
            },
            js=(
                'wagtailcommonmark/js/codemirror.js',
                'wagtailcommonmark/js/codemirror.addon.edit.continuelist.js',
                'wagtailcommonmark/js/codemirror.mode.markdown.js',
                'wagtailcommonmark/js/codemirror.attach.js',
            )
        )
