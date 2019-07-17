from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('name', 'status', 'contact', )
    required_languages = ('ru', 'en', 'kg', )


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('name', 'grade')
    required_languages = ('ru', 'en', 'kg', )


@register(PreUniversity)
class PreUniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)
    required_languages = ('ru', 'en', 'kg', )


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )
    required_languages = ('ru', 'en', 'kg', )


@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )
    required_languages = ('ru', 'en', 'kg', )


@register(Institute)
class InstituteTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )
    required_languages = ('ru', 'en', 'kg', )


@register(Classroom)
class ClassroomTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)
    required_languages = ('ru', 'en', 'kg', )


@register(Building)
class BuildingTranslationOptions(TranslationOptions):
    fields = ('name', )
    required_languages = ('ru', 'en', 'kg', )




