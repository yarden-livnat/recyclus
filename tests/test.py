
from recyclus import Client

client = Client()

r = client.test()

print(r.content)
