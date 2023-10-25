from django.shortcuts import render, HttpResponseRedirect
from .models import Member
from .forms import MemberForm
from django.views.generic.base import View, TemplateView, RedirectView
from django.contrib import messages
from django.urls import reverse
from .service import get_subscription_renewal_date_from_subscriber_type_and_subscription_date, \
    get_membership_end_date_from_membership_start_date


class MemberCreate(TemplateView):
    template_name = 'MembershipTemplate/create.html'

    def get_context_data(self):
        member_form = self.kwargs.get('member_form')
        if not member_form:
            member_form = MemberForm()
        member_data = Member.objects.all()
        context = {'data': member_data, 'form': member_form}
        return context

    def post(self, request):
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            first_name = member_form.cleaned_data['first_name']
            last_name = member_form.cleaned_data['last_name']
            age = member_form.cleaned_data['age']
            email = member_form.cleaned_data['email']
            phone = member_form.cleaned_data['phone']
            place = member_form.cleaned_data['place']
            subscriber_type = member_form.cleaned_data['subscriber_type']
            is_active = member_form.cleaned_data['is_active']
            subscription_date = member_form.cleaned_data['subscription_date']
            membership_start_date = member_form.cleaned_data['membership_start_date']
            subscription_renewal_date = get_subscription_renewal_date_from_subscriber_type_and_subscription_date(
                subscriber_type, subscription_date)
            membership_end_date = get_membership_end_date_from_membership_start_date(membership_start_date)

            member_data = Member(first_name=first_name, last_name=last_name, age=age, email=email, phone=phone,
                                 place=place, subscriber_type=subscriber_type, is_active=is_active,
                                 subscription_date=subscription_date, subscription_renewal_date=subscription_renewal_date,
                                 membership_start_date=membership_start_date, membership_end_date=membership_end_date)
            member_data.save()
            messages.success(request, 'Thank you for joining 😀')

        else:
            self.kwargs['member_form'] = member_form
            context = self.get_context_data()
            return render(request, 'MembershipTemplate/create.html', context)

        return HttpResponseRedirect(reverse('create'))


class MemberUpdate(View):
    def get(self, request, memberid):
        member_data = Member.objects.get(pk=memberid)
        member_form = MemberForm(instance=member_data)
        return render(request, template_name='MembershipTemplate/update.html',
                      context={'form': member_form, 'id': memberid})

    def post(self, request, memberid):
        member_data = Member.objects.get(pk=memberid)
        member_form = MemberForm(request.POST, instance=member_data)
        if member_form.is_valid():
            subscriber_type = member_form.cleaned_data['subscriber_type']
            subscription_date = member_form.cleaned_data['subscription_date']
            membership_start_date = member_form.cleaned_data['membership_start_date']

            member_data.subscription_renewal_date = get_subscription_renewal_date_from_subscriber_type_and_subscription_date(
                subscriber_type, subscription_date)
            member_data.membership_end_date = get_membership_end_date_from_membership_start_date(
                membership_start_date)

            member_form.save()

            messages.success(request, f'Updated details of member (id = {memberid}) successfully 🙂 !!!')
        return render(request, template_name='MembershipTemplate/update.html',
                      context={'form': member_form, 'id': memberid})


class MemberDeletePage(TemplateView):
    template_name = 'MembershipTemplate/delete.html'

    def get_context_data(self, **kwargs):
        member_id = kwargs['memberid']
        context = {'id': member_id}
        return context


class MemberDelete(RedirectView):
    url = '/member/create/'

    def get_redirect_url(self, *args, **kwargs):
        member_id = kwargs['memberid']
        Member.objects.get(pk=member_id).delete()
        return super().get_redirect_url(*args, **kwargs)
