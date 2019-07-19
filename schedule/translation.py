from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name', )
    required_languages = ('ru', 'en', 'kg', )