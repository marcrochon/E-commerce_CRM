from django.contrib import admin

from ecommerce_crm.programmeletter.models import TeamName
from ecommerce_crm.programmeletter.models import StaffInTeam
from ecommerce_crm.programmeletter.models import LetterData

from ecommerce_crm.programmeletter.forms import StaffInTeamForm
from ecommerce_crm.programmeletter.forms import TeamNameForm

from ajax_select.admin import AjaxSelectAdmin

from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse


class StaffInline(admin.StackedInline):
    """
    This class is used to add, edit or delete staff.
    """
    form = StaffInTeamForm
    model = StaffInTeam
    fields = ['staff', ]
    extra = 3


class TeamNameAdmin(AjaxSelectAdmin):
    """
    This class is used to add, edit or delete team for the field work.
    """
    form = TeamNameForm
    inlines = [StaffInline]
    model = TeamName


class LetterDataAdmin(admin.ModelAdmin):
    """
    This class is used to add, edit or delete letter data for generation of
    programme letter.
    """
    def response_add(self, request, obj, post_url_continue=None):
        request.session['old_post'] = request.POST
        request.session['letterdata_id'] = obj.id
        return HttpResponseRedirect(reverse\
            ("ecommerce_crm.programmeletter.views.programmeletter"))

    def response_change(self, request, obj, post_url_continue=None):
        request.session['old_post'] = request.POST
        request.session['letterdata_id'] = obj.id
        return HttpResponseRedirect(reverse\
            ("ecommerce_crm.programmeletter.views.programmeletter"))

admin.site.register(TeamName, TeamNameAdmin)
admin.site.register(LetterData, LetterDataAdmin)