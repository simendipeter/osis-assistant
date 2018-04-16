##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2018 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from ordered_model.models import OrderedModel
from ordered_model.admin import OrderedModelAdmin


class LearningAchievementsAdmin(OrderedModelAdmin):
    list_display = ('learning_unit_year', 'code_name', 'order', 'move_up_down_links')
    fieldsets = ((None, {'fields': ('learning_unit_year', 'code_name', 'order', 'text')}),)
    readonly_fields = ['order']
    search_fields = ['learning_unit_year__acronym', 'code_name', 'order']
    raw_id_fields = ('learning_unit_year',)


class LearningAchievements(OrderedModel):
    code_name = models.CharField(max_length=100, verbose_name=_('code'))
    text = RichTextField(null=True, verbose_name=_('text'))
    learning_unit_year = models.ForeignKey('LearningUnitYear')
    order_with_respect_to = 'learning_unit_year'

    class Meta:
        unique_together = ("code_name", "learning_unit_year")

    def __str__(self):
        return u'{} - {} (order {})'.format(self.learning_unit_year, self.code_name, self.order)