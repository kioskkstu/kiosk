from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name', )
    required_languages = ('en', )


@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ('time', 'day_of_week', 'subject', 'week', 'type', 'teacher', 'classroom', 'group', )
    required_languages = ('en', )