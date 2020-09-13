#!/usr/bin/env python3

import json
import requests
from collections import defaultdict

POINT_THRESHOLD = 40
year = 2000
page = 10

stories = defaultdict(list)

for year in range(2005, 2010):
    for page in range(5):
        ct = 0
        url = f"https://hn.algolia.com/api/v1/search?tags=story&numericFilters=points>{POINT_THRESHOLD}&query={year}&page={page}"
        print(url)
        r = requests.get(url)
        data = r.json()
        for hits in data['hits']:
            if f"({year})" in hits['title']:
                print(f"   {hits['title']} -- {hits['points']}")
                print()
                stories[year].append(hits)
                ct += 1
        if ct == 0:
            break 



with open("stories.json", "w") as out:
     json.dump(stories, out)
