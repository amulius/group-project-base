import factory
from ..models import Person


# class WarGameFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = 'cards.WarGame'


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person
    username = factory.Sequence(lambda i: 'User{}'.format(i))
    password = factory.PostGenerationMethodCall('set_password',
                                                'password')
    email = 'test@test.com'
    phone = '555-555-5555'
