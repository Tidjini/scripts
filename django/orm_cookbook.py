# find the query associated with a queryset
queryset = models.Event.objects.all()
print("SQL Query")
print(str(queryset.query))
