# flask-graphene-hello
A simple example using GraphQL (Graphene) and Flask


### Prerequisites

First, [install pipenv](http://docs.pipenv.org/en/latest/basics.html):

```
$ pip install pipenv
```

### Installing

1. Check out this repository:

    $ git clone https://github.com/savovs/flask-graphene-hello.git
    $ cd flask-graphene-hello

2. Install dependencies:

  $ pipenv install


3. Open project shell (in virtual environment):

    $ pipenv shell

4. Run Flask

    $ FLASK_APP=./server/index.py flask run


5. Go to `localhost:5000/graphql` and run a `hello(age: 23, name: "yourname")` query

That's it! 

✨🍰✨
