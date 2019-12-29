from rest_framework.renderers import JSONRenderer
'''
JSONRenders().render(serializer.data)

it converts native python data type (dictionary)  to Json format 

'''
from rest_framework.parsers import JSONParser
import  io
'''
it converts jsont to python native data type
stream = io.BytesIO(json)
data =  JSONParser().parse(stream)
we can pass this data to serializer for further processing.
'''