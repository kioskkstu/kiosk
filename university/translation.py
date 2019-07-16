from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('name', 'photo', 'status', 'contact', )
    required_languages = ('en', )


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('en', )


@register(PreUniversity)
class PreUniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)
    required_languages = ('en', )


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'teachers', 'groups',)
    required_languages = ('en', )


@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'department',)
    required_languages = ('en', )


@register(Institute)
class InstituteTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'department',)
    required_languages = ('en', )


@register(Classroom)
class ClassroomTranslationOptions(TranslationOptions):
    fields = ('name', 'floor', 'about',)
    required_languages = ('en', )


@register(Building)
class BuildingTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'floor', 'classrooms')
    required_languages = ('en', )




