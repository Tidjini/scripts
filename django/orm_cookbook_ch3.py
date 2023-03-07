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
