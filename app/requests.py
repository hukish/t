import urllib.request,json
from .models import Quote
 

api_key = None 
base_url = None


def configure_request(app):
    global base_url
    #api = app.config['QUOTE_API']
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes(category):

    get_quotes_url = base_url.format(category,api_key)
   
    with urllib.request.urlopen(base_url) as url:

        quotes_data = url.read()
        random_quote = json.loads(quotes_data)
        
        quotes_result = []

        if random_quote:
            quote = random_quote
            quote_item = process_results(quote)

        return quote_item

def process_results(quote_object):

    quote_item=[]
    id = quote_object['id']
    author = quote_object['author']
    quote = quote_object['quote']
    
    quote_item.append(Quote(id,author,quote))  
    return quote_item