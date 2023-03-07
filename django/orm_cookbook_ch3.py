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


# create just one object in table
# this is usefull in configurations tables
class Config(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # check existance
        if self.__class__.objects.count():
            # get PK if item exist
            self.pk = self.__class__.objects.first().pk

        super().save(*args, **kwargs)


# update field by it self exp!count=F('count') + 1
Category.objects.filter(name="filter").update(count=F('count') + 1)

# turncate
# this is use DELETE FROM ... wich is slow
Category.objects.all().delete()
# instead define a turncate function in Category Model


class Category(models.Model):
    ...

    @classmethod
    def turncat(cls):
        with connection.cursor() as cursor:
            cursor.execute('TURNCATE TABLE "{0}" CASCADE'.format(
                cls.__meta__.db_table))

# signals for third party apps and models you can't control
# otherwise use .save overiding
