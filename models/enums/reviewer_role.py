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
from django.utils.translation import gettext_lazy as _

PHD_SUPERVISOR = 'PHD_SUPERVISOR'
SUPERVISION = 'SUPERVISION'
SUPERVISION_ASSISTANT = 'SUPERVISION_ASSISTANT'
SUPERVISION_DAF = 'SUPERVISION_DAF'
SUPERVISION_DAF_ASSISTANT = 'SUPERVISION_DAF_ASSISTANT'
RESEARCH = 'RESEARCH'
RESEARCH_ASSISTANT = 'RESEARCH_ASSISTANT'
VICE_RECTOR = 'VICE_RECTOR'
VICE_RECTOR_ASSISTANT = 'VICE_RECTOR_ASSISTANT'

ROLE_CHOICES = (
    (PHD_SUPERVISOR, _('Thesis promoter')),
    (SUPERVISION, _('Dean of Faculty')),
    (SUPERVISION_ASSISTANT, _('Dean of Faculty representative')),
    (SUPERVISION_DAF, _('DAF')),
    (SUPERVISION_DAF_ASSISTANT, _('DAF representative')),
    (RESEARCH, _('President of Institute')),
    (RESEARCH_ASSISTANT, _('Representative of the Institute President')),
    (VICE_RECTOR, _('Vice-rector of sector')),
    (VICE_RECTOR_ASSISTANT, _('DAS/CAS'))
)

ENABLE_TO_DELEGATE = [SUPERVISION, RESEARCH, SUPERVISION_DAF]
ABLE_TO_VALIDATE = [SUPERVISION, RESEARCH, RESEARCH_ASSISTANT, PHD_SUPERVISOR, VICE_RECTOR, VICE_RECTOR_ASSISTANT]
