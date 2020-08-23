import json
    

class CountriesIterator:
    
    def __init__(self, countries_json):
        with open('countries.json') as file:
            self.countries_json = json.load(file)
        self.start = -1
        self.end = len(self.countries_json)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        country = self.countries_json[self.start]["name"]["common"]
        return (f'{country} - https://en.wikipedia.org/wiki/{country.replace(" ", "_")}')

for country in CountriesIterator('countries.json'):
    with open('wiki_countries.txt', 'a') as f:
        f.write(country + '\n')