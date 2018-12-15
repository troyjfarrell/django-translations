from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TranslationsConfig(AppConfig):
    name = 'translations'
    verbose_name = _('translations')

    def ready(self):
        print('ready')
        try:
            # cache all content types at the start
            from django.contrib.contenttypes.models import ContentType
            models = [ct.model_class() for ct in ContentType.objects.all()]
            ContentType.objects.get_for_models(*models)

            from django.db import models as m
            for model in models:
                field = m.CharField('trans', max_length=255)
                field.contribute_to_class(model, 'trans')
        except Exception:
            raise
