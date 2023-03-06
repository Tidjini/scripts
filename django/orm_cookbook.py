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
