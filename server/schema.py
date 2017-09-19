# GraphQL in Python
from graphene import Schema, Argument, String, Int, ObjectType

class Query(ObjectType):
	# Define a field with arguments
	hello = String(
		name = Argument(String, default_value = 'stranger'),
		age = Argument(Int)
	)

	def resolve_hello(self, info, name, age):
		return 'Hi {} you are {} years old.'.format(name, age)

schema = Schema(query=Query)
