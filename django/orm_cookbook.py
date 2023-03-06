from django.db.models import Q
from application import models
# find the query associated with a queryset
queryset = models.Event.objects.all()
print("SQL Query")
print(str(queryset.query))
# OR query
authorized_event = models.Event.objects.filter(authorize=True)
confirmed_event = models.Event.objects.filter(confirm=True)
result = authorized_event | confirmed_event
# OR with filter Q
result = models.Event.objects.filter(Q(authorize=True) | Q(confirm=True))
