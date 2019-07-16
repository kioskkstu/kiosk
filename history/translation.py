from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('name', 'text', )
    required_languages = ('ru', 'en', 'kg', )

