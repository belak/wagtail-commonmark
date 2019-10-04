from django import forms

from .utils import render_commonmark, CommonMarkMedia
from .widgets import CommonMarkTextarea

from wagtail.core.blocks import TextBlock


class CommonMarkBlock(CommonMarkMedia, TextBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.CharField(required=required, help_text=help_text,
                                     widget=CommonMarkTextarea())
        super().__init__(**kwargs)

    def render_basic(self, value, context=None):
        return render_commonmark(value, context)
