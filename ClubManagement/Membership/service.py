from .config import MEMBERSHIP_DURATION
from datetime import timedelta
from .models import SubscriberChoices


def get_subscription_renewal_date_from_subscriber_type_and_subscription_date(subscriber_type, subscription_date):
    subscription_renewal_date = None
    if subscriber_type == SubscriberChoices.monthly.value:
        subscription_renewal_date = subscription_date + timedelta(days=30)
    elif subscriber_type == SubscriberChoices.semi_annual.value:
        subscription_renewal_date = subscription_date + timedelta(days=365/2)
    elif subscriber_type == SubscriberChoices.annual.value:
        subscription_renewal_date = subscription_date + timedelta(days=365)

    return subscription_renewal_date


def get_membership_end_date_from_membership_start_date(membership_start_date):
    membership_end_date = membership_start_date + timedelta(days=MEMBERSHIP_DURATION)
    return membership_end_date
