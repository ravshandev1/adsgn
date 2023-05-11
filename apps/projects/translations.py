from modeltranslation.translator import TranslationOptions, register
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Category, Project, Profession


class CustomTranslationsAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class InlineTranslationsAdmin(TranslationTabularInline):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(Category)
class Translation(TranslationOptions):
    fields = ('name',)


@register(Profession)
class Translation(TranslationOptions):
    fields = ('name',)


@register(Project)
class Translation(TranslationOptions):
    fields = ('about',)
