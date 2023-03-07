# Create, update, deleting things
from app.models import Category
# create multiple objects

Category.objects.bulk_create(
    [
        Category(name="A"),
        Category(name="B"),
        Category(name="C"),
    ]
)

# clone object

category = Category.objects.first()
# should set pk to None
category.pk = None
category.save()
