# Realestate Data

A tool to request real estate data from an unofficial realestate.com.au
"API".

## Installation

```bash
pip install realestate-data
```

## Usage

Build out schematics to represent the search query you are after.

See [here](https://webtools.realestate.com.au/configuring-widgets-included-via-javascript/)
for available options, or take a look at ./realestate_data/schematics.py

The below creates a search object that represents
- Units and apartments for sale
- in Melbourne Victoria, 3000
- and surrounding suburbs
- price between $500,000 and $1,000,000
- minimum of 1 parking space
- minimum of 1 bathroom
- minimum of 2 bedrooms

```python
>>> from realestate_data import Search, Locality, PriceRange, Filters
>>>
>>> p = PriceRange()
>>> p.minimum = 500000
>>> p.maximum = 1000000
>>>
>>> l = Locality()
>>> l.locality = 'Melbourne'
>>> l.subdivision = Locality.SUBDIVISION_VIC
>>> l.postcode = '3000'
>>>
>>> f = Filters()
>>> f.property_types = [Filters.PROPERTY_TYPE_APARTMENT, Filters.PROPERTY_TYPE_UNIT]
>>> f.surrounding_suburbs = True
>>> f.minimum_bedrooms = 2
>>> f.minimum_bathrooms = 1
>>> f.minimum_parking_spaces = 1
>>> f.price_range = p
>>>
>>> s.channel = Search.CHANNEL_BUY
>>> s.localities = [l]
>>> s.filters = f
```

Call validate() on the search object to ensure its valid. It will return
nothing if valid and an error if not

```python
>>> s.validate()
```

Call to_primitive() to view the search object

```python
>>> s.to_primitive()
{'channel': 'buy', 'localities': [{'locality': 'Melbourne', 'subdivision': 'VIC', 'postcode': '3000'}], 'filters': {'property-types': ['apartment', 'unit'], 'minimum-bedrooms': 1, 'minimum-bathrooms': 1, 'minimum-parking-spaces': 1, 'surrounding-suburbs': True, 'price-range': {'minimum': 500000, 'maximum': 1000000}}}
```

Pass the created Search object to the paged_results generator. The generator
yields the json returned from each paged request.

```python
>>> from realestate_data import paged_results
>>> paged_data = [page for page in paged_results(s)]
```

Or use the Generator how ever you want

```python
>>> paged_data = paged_results(s)
>>> page_one = next(paged_data)
>>> page_two = next(paged_data)
```

```python
>>> for page in paged_results(s):
>>>     print(page)
```

## Todo

- Testing

## Author

Jeremy Storer <storerjeremy@gmail.com>