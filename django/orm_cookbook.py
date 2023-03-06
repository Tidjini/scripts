from django.db.models import Q
from app import models
# find the query associated with a queryset
queryset = models.Event.objects.all()
print("SQL Query")
print(str(queryset.query))
# OR query
authorized_event = models.Event.objects.filter(authorize=True)
confirmed_event = models.Event.objects.filter(confirm=True)
or_result = authorized_event | confirmed_event
# OR with filter Q
or_result = models.Event.objects.filter(Q(authorize=True) | Q(confirm=True))
# AND Query
and_result = authorized_event & confirmed_event
and_result = models.Event.objects.filter(Q(authorize=True) & Q(confirm=True))
and_result = models.Event.objects.filter(authorize=True, confirm=True)

# Not operator
not_authorized = models.Event.objects.filter(~Q(authorize=True))

# UNION
# Union can be performed on differents models, but they must have same fields with same datatypes
authorized_event.union(confirmed_event)

# SELECT Some fields
select_result = models.Event.objects.filter(
    authorize=True, confirm=True).values('name', 'details')
select_result = models.Event.objects.filter(
    authorize=True, confirm=True).values_list('name', 'details')
# this selection give selected fields, plus id
select_result_with_id = models.Event.objects.filter(
    authorize=True, confirm=True).only('name', 'details')
# todo Subquery review with example

# field equals to other field
users = models.Users.objects.filter(first_name=F('last_name'))
users = models.Users.objects.anontate(first=Substr(
    "first_name", 1, 1), last=Substr("last_name", 1, 1)).filter(first=F('last'))

# Nth results with slice operator
second_user = users.order_by('-last_login')[1]
# Duplicate names,
# 1/select value first_name
# 2/count names Count(first_name)
# 3/get duplicates by filtering results
users = models.User.objects.values('first_name').annotate(
    name_count=Count('first_name')).filter(name_count__gt=1)
