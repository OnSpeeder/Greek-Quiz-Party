import urllib.request
import urllib.parse
import json

def test():
    query = """
    SELECT ?item ?itemLabel WHERE {
      ?item wdt:P31 wd:Q6256.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "el". }
    }
    LIMIT 5
    """
    url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'QuizPartyTrivia/1.0', 'Accept': 'application/sparql-results+json'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print("Items fetched:", len(data['results']['bindings']))
            for b in data['results']['bindings']:
                print(b['itemLabel']['value'])
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    test()
