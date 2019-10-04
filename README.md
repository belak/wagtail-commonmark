## wagtail-commonmark: CommonMark fields and blocks for Wagtail

Tired of annoying rich text editors getting in the way of your content
input?  Wish Wagtail worked more like a wiki?  Well, now it can.

`wagtail-commonmark` provides CommonMark field support for [Wagtail](https://github.com/torchbox/wagtail/).
Specifically, it provides:

* A `wagtailcommonmark.blocks.CommonMarkBlock` for use in streamfields.
* A `wagtailcommonmark.fields.CommonMarkField` for use in page models.
* A `wagtailcommonmark.edit_handlers.CommonMarkPanel` for use in the editor interface.
* A `commonmark` template tag.

### Installation

Alpha release is available on Pypi - https://pypi.org/project/wagtail-commonmark/ - installable via `pip install wagtail-commonmark`.


### Using it

Add it to `INSTALLED_APPS`:

```python
INSTALLED_APPS += [
    'wagtailcommonmark',
]
```

Use it as a `StreamField` block:

```python
from wagtailcommonmark.blocks import CommonMarkBlock

class MyStreamBlock(StreamBlock):
    markdown = CommonMarkBlock(icon="code")
```

Or use as a page field:

```python
from wagtailcommonmark.edit_handlers import CommonMarkPanel
from wagtailcommonmark.fields import CommonMarkField

class MyPage(Page):
    body = CommonMarkField()

    content_panels = [
        FieldPanel("title", classname="full title"),
        CommonMarkPanel("body"),
    ]
```

And render the content in a template:

```html+django
{% load wagtailcommonmark %}
<article>
{{ self.body|commonmark }}
</article>
```
