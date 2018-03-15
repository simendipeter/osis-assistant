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
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from base.business.learning_unit_deletion import check_other_than_proposal
from base.business.learning_unit_proposal import compute_proposal_type
from base.business.learning_unit_proposal import delete_learning_unit_proposal, reinitialize_data_before_proposal
from base.business.learning_units.perms import can_delete_learning_unit_year
from base.forms.learning_unit_proposal import LearningUnitProposalModificationForm
from base.models import proposal_learning_unit
from base.models.entity_version import find_latest_version_by_entity
from base.models.enums import proposal_state
from base.models.enums import proposal_type
from base.models.learning_unit_year import LearningUnitYear
from base.models.person import Person
from base.models.proposal_learning_unit import ProposalLearningUnit
from base.views import layout
from base.views.common import display_success_messages, display_error_messages
from base.views.learning_unit import compute_form_initial_data
from base.views.learning_unit import get_learning_unit_identification_context
from base.views.learning_units import perms
from base.views.learning_units.delete import get_messages_deletion_context, delete_learning_unit_years


@login_required
@perms.can_create_modification_proposal
@permission_required('base.can_propose_learningunit', raise_exception=True)
def propose_modification_of_learning_unit(request, learning_unit_year_id):
    learning_unit_year = get_object_or_404(LearningUnitYear, id=learning_unit_year_id)
    user_person = get_object_or_404(Person, user=request.user)
    initial_data = compute_form_initial_data(learning_unit_year)
    proposal = proposal_learning_unit.find_by_learning_unit_year(learning_unit_year)

    form = LearningUnitProposalModificationForm(
        request.POST or None,
        initial=initial_data,
        instance=proposal,
        learning_unit=learning_unit_year.learning_unit
    )

    if request.method == 'POST':
        if form.is_valid():
            type_proposal = compute_proposal_type(initial_data, request.POST)
            form.save(learning_unit_year, user_person, type_proposal, proposal_state.ProposalState.FACULTY.name)
            messages.add_message(request, messages.SUCCESS,
                                 _("success_modification_proposal")
                                 .format(_(type_proposal), learning_unit_year.acronym))
            return redirect('learning_unit', learning_unit_year_id=learning_unit_year.id)

    return render(request, 'learning_unit/proposal/update.html', {
        'learning_unit_year': learning_unit_year,
        'person': user_person,
        'form': form,
        'experimental_phase': True})


@login_required
@perms.can_perform_cancel_proposal
@permission_required('base.can_propose_learningunit', raise_exception=True)
def cancel_proposal_of_learning_unit(request, learning_unit_year_id):
    learning_unit_year = get_object_or_404(LearningUnitYear, id=learning_unit_year_id)
    return cancel_creation_proposal(learning_unit_year, request)


@login_required
@perms.can_edit_learning_unit_proposal
def edit_learning_unit_proposal(request, learning_unit_year_id):
    user_person = get_object_or_404(Person, user=request.user)
    proposal = proposal_learning_unit.find_by_learning_unit_year(learning_unit_year_id)
    initial_data = compute_form_initial_data(proposal.learning_unit_year)
    initial_data.update(_build_proposal_data(proposal))

    proposal_form = LearningUnitProposalModificationForm(
        request.POST or None,
        initial=initial_data,
        instance=proposal,
        learning_unit=proposal.learning_unit_year.learning_unit
    )

    if proposal_form.is_valid():
        try:
            type_proposal = compute_proposal_type(initial_data, request.POST)
            proposal_form.save(proposal.learning_unit_year, user_person, type_proposal,
                               proposal_form.cleaned_data.get("state"))
            display_success_messages(request, _("proposal_edited_successfully"))
            return HttpResponseRedirect(reverse('learning_unit', args=[learning_unit_year_id]))
        except (IntegrityError, ValueError) as e:
            display_error_messages(request, e.args[0])
    return layout.render(request, 'learning_unit/proposal/edition.html',  {
        'learning_unit_year': proposal.learning_unit_year,
        'person': user_person,
        'form': proposal_form,
        'experimental_phase': True})


def _build_proposal_data(proposal):
    return {"folder_id": proposal.folder.folder_id,
            "folder_entity": find_latest_version_by_entity(proposal.folder.entity.id,
                                                           datetime.date.today()),
            "type": proposal.type,
            "state": proposal.state}


def cancel_proposal_of_type_creation(request, learning_unit_proposal):
    person = get_object_or_404(Person, user=request.user)
    learning_unit_year = get_object_or_404(LearningUnitYear, id=learning_unit_proposal.learning_unit_year.id)
    if not can_delete_learning_unit_year(learning_unit_year, person):
        return HttpResponseForbidden()

    messages_deletion = check_other_than_proposal(learning_unit_year)
    if not messages_deletion:
        _delete_learning_unit_proposal_of_type_creation(learning_unit_proposal, request)
        return redirect('learning_unit_proposal_search')
    else:
        context = get_learning_unit_identification_context(learning_unit_year.id, person)
        if messages_deletion:
            context.update(get_messages_deletion_context(learning_unit_year, messages_deletion))

        return layout.render(request, "learning_unit/identification.html", context)


def _delete_learning_unit_proposal_of_type_creation(learning_unit_proposal, request):
    learning_unit_year = learning_unit_proposal.learning_unit_year
    delete_learning_unit_years(learning_unit_year, request)
    delete_learning_unit_proposal(learning_unit_proposal)
    messages.add_message(request, messages.SUCCESS, _("success_cancel_proposal").format(learning_unit_year.acronym))


def cancel_creation_proposal(learning_unit_year, request):
    learning_unit_proposal = get_object_or_404(ProposalLearningUnit, learning_unit_year=learning_unit_year)
    if learning_unit_proposal.type == proposal_type.ProposalType.CREATION.name:
        return cancel_proposal_of_type_creation(request, learning_unit_proposal)
    else:
        reinitialize_data_before_proposal(learning_unit_proposal, learning_unit_year)
        delete_learning_unit_proposal(learning_unit_proposal)
        messages.add_message(request, messages.SUCCESS, _("success_cancel_proposal").format(learning_unit_year.acronym))
        return redirect('learning_unit', learning_unit_year_id=learning_unit_year.id)