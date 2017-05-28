#### To run:

##### Option 1

To run from the command line:

```
// Configure virtual environ
virtualenv env
source env/bin/activate

// Configure testing environ
pip install nose

// Run tests
nosetests

// End session
deactivate
```

##### Option 2

To run tests within the included Docker image:

```
docker build --tag python-string-exercies .
docker run --rm python-string-exercies
```
