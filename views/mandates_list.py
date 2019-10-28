##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2019 Université catholique de Louvain (http://www.uclouvain.be)
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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Prefetch
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

import base.models.entity
from assistant.forms.mandate import MandatesArchivesForm
from assistant.models import assistant_mandate
from assistant.models.enums import assistant_mandate_state, review_advice_choices, review_status
from assistant.models.review import Review
from assistant.utils import manager_access
from base.models import academic_year


class MandatesListView(LoginRequiredMixin, UserPassesTestMixin, ListView, FormMixin):
    context_object_name = 'mandates_list'
    template_name = 'mandates_list.html'
    form_class = MandatesArchivesForm

    def test_func(self):
        return manager_access.user_is_manager(self.request.user)

    def get_login_url(self):
        return reverse('assistants_home')

    def get_queryset(self):
        form_class = MandatesArchivesForm
        form = form_class(self.request.GET)
        if form.is_valid():
            self.request.session['selected_academic_year'] = form.cleaned_data[
                'academic_year'].id
            queryset = assistant_mandate.AssistantMandate.objects.filter(
                academic_year=form.cleaned_data['academic_year'])
        elif self.request.session.get('selected_academic_year'):
            selected_academic_year = academic_year.AcademicYear.objects.get(
                id=self.request.session.get('selected_academic_year'))
            queryset = assistant_mandate.AssistantMandate.objects\
                .filter(academic_year=selected_academic_year)
        else:
            selected_academic_year = academic_year.starting_academic_year()
            self.request.session[
                'selected_academic_year'] = selected_academic_year.id
            queryset = assistant_mandate.AssistantMandate.objects.filter(
                academic_year=selected_academic_year)
        queryset = queryset.select_related(
            'academic_year', 'assistant__person', 'assistant__supervisor'
        ).prefetch_related(
            Prefetch(
                'review_set',
                queryset=Review.objects.all().select_related('reviewer__person')
            )
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super(MandatesListView, self).get_context_data(**kwargs)
        context['year'] = academic_year.find_academic_year_by_id(
                self.request.session.get('selected_academic_year')).year
        context['assistant_mandate_state'] = assistant_mandate_state
        context['review_advice_choices'] = review_advice_choices
        context['review_status'] = review_status
        start_date = academic_year.find_academic_year_by_id(int(self.request.session.get(
            'selected_academic_year'))).start_date
        for mandate in context['object_list']:
            entities_id = mandate.mandateentity_set.all().order_by('id').values_list('entity', flat=True)
            mandate.entities = base.models.entity.find_versions_from_entites(entities_id, start_date)
        return context

    def get_initial(self):
        if self.request.session.get('selected_academic_year'):
            selected_academic_year = academic_year.find_academic_year_by_id(
                self.request.session.get('selected_academic_year'))
        else:
            selected_academic_year = academic_year.starting_academic_year()
            self.request.session[
                'selected_academic_year'] = selected_academic_year.id
        return {'academic_year': selected_academic_year}
