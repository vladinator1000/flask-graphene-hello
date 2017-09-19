from flask import Flask
from flask_graphql import GraphQLView

from schema import schema

# Init app
app = Flask(__name__)

# Add GraphQL route using schema.py
app.add_url_rule(
	'/graphql',
	view_func = GraphQLView.as_view('graphql', schema = schema, graphiql = True)
)

if (__name__ == '__main__'):
	app.run()
