from django import forms

from wagtail.utils.widgets import WidgetWithScript

from .utils import CommonMarkMedia


class CommonMarkTextarea(CommonMarkMedia,
                         WidgetWithScript,
                         forms.widgets.Textarea):
    def render_js_init(self, id_, name, value):
        return 'codeMirrorAttach("{0}");'.format(id_)
