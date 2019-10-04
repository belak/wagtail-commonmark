from django.db.models import TextField

from .widgets import CommonMarkTextarea


class CommonMarkField(TextField):
    def formfield(self, **kwargs):
        defaults = {
            'widget': CommonMarkTextarea
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
