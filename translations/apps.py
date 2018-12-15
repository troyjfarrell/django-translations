from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.utils import OperationalError


class TranslationsConfig(AppConfig):
    name = 'translations'
    verbose_name = _('translations')

    def ready(self):
        try:
            # cache all content types at the start
            from django.contrib.contenttypes.models import ContentType
            models = [ct.model_class() for ct in ContentType.objects.all()]
            ContentType.objects.get_for_models(*models)

            # add proper translatable fields dynamically
            from django.db import models as m
            from translations.models import Translatable
            from translations.languages import _get_translation_choices
            for model in models:
                if issubclass(model, Translatable):
                    for field in model.get_translatable_fields():
                        for (code, language) in _get_translation_choices().items():
                            translation_field = field.clone()

                            if model.are_translatable_fields_blank():
                                translation_field.blank = True

                            verbose_name = '{} ({})'.format(
                                field.verbose_name,
                                language
                            )
                            translation_field.verbose_name = verbose_name

                            code = code.replace('-', '_')
                            name = '{}_in_{}'.format(
                                field.name,
                                code
                            )
                            translation_field.contribute_to_class(model, name)
        except OperationalError as e:
            if e.args[0] != 'no such table: django_content_type':
                raise

