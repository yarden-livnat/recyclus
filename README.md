# Recyclus
A python client for interacting with Recyclus services 

## Quick start

``` python
>>> import pp  # optional for a better prettyprint
>>> from recyclus import Client
>>> client = Client()

>>> client.server(host=...) # If you need to change from the default local service

# A one time registration 
# user: default to local username
# password: the user will prompt for password if none was given

>>> client.register(user=None, password=None) 

# if you already registered from a different machine you can login
>>> client.login(password='...') 

# run a job
>>> job = client.run(scenario='schenario.xml', project='demo')

# check job status
>>> pp(job.status())
{
    'info': {
        'simulation': {
            'duration': '0:00:05',
            'ended at': '2019-03-12 21:39:47',
            'files': '["scenario", "output", "stdio"]',
            'start time': '2019-03-12 21:39:42.285867',
            'started at': '2019-03-12 21:39:42',
            'status': 'done',
        },
        'status': 'done',
    },
    'status': 'ok',
}

# list remote files, both input and output
>>> job.files()
['scenario.xml', 'cyclus.sqlite']

# fetch and save a file
>>> job.save('cyclus.sqlite')

# delete a job and all the associated files
>>> job.delete()
```

## Commands

* `client.server(host)`: Change the remote services host (default is 'localhost'). 
 The current url will be return if no host is given

* `client.register(user=None, password=None)`: Register with the remote service User defaults to local username. If 
no password is provided you'll be prompt for one


