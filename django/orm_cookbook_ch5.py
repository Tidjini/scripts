# Database modeling

# Many to Many Relationship

class User(Model):
    tweet = CharField(max_length=255)
    follower = ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    pass


user1 = User(tweet="tweet")
user1.save()
user2 = User(tweet="tweet user 2")
user2.save()
user3 = User(tweet="tweet user 3")
user3.save()

# Add Follower
user1.follower.add(user2)
user1.follower.add(user3)
user1.save()

# Remove Follower
user1.follower.remove(user2)
user1.save()

# Self Referencing


class User(Model):
    manager = ForeignKey('self', on_delete=CASCADE)
    pass


# OR
class User(Model):
    manager = ForeignKey('app.Employee', on_delete=CASCADE)
    pass


# Try to convert Existing Database to Django Models
# python manage.py inspectdb > models.py


# Views and virtual tables (le vues)
# but with this you can not insert data => django.db.utils.OperationalError
class TempUser(models.Model):
    first_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temp_user'


# null  => for database column value
# blank => for form input in Admin and your Views
