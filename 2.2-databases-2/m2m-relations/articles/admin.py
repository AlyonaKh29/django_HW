from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = False
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    flag = True
            if not flag:
                raise ValidationError('Ошибка! Главный тэг должен быть первым.')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ObjectTag(admin.ModelAdmin):
    fields = ['name']
