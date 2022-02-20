# flightradar24 #
### Display Top 10 Watched Flights from flightradar24.com
```
$ fr.py
```
#### Example of query on Sunday, February 20, 2022

| flight_id | flight | callsign | squawk | clicks | from_iata | from_city | to_iata | to_city |
| --------- | ------ | -------- | ------ | ------ | --------- | --------- | ------- | ------- |
2ae24bf7 | None | FORTE11 | 2051 | 18768 | None | None | None | None
2ae2b969 | TK1476 | THY9ZF | 4527 | 4464 | HRK | Kharkiv | IST | Istanbul
2ae17b1c | None | JAKE12 | 3551 | 3972 | MHZ | Mildenhall | None | None
2ae2ba01 | TK1470 | THY6ZQ | 4531 | 3876 | OZH | Zaporizhzhia | IST | Istanbul
2ae29635 | TK411 | THY1QS | 6305 | 3400 | IST | Istanbul | VKO | Moscow
2ae282d8 | QU4710 | UTN4710 | 6354 | 3168 | AYT | Antalya | KBP | Kyiv
2ae29ecc | TK416 | THY3QX | 1522 | 2576 | VKO | Moscow | IST | Istanbul
2ae2c419 | PS601 | AUI601 | 4541 | 2360 | KBP | Kyiv | GYD | Baku
2ae2bc6d | TK286 | THY286 | 6245 | 1936 | MSQ | Minsk | IST | Istanbul
2ae2bf47 | FR3826 | RYR6BU | 5576 | 1704 | KBP | Kyiv | NAP | Naples


### F.A.Q's
#### I see from_iata and to_iata - what is that?
An IATA airport code[^1], also known as an IATA location identifier, IATA station code, or simply a location identifier, is a three-letter geocode designating many airports and metropolitan areas around the world, defined by the International Air Transport Association (IATA).

#### Is the data sorted in any way?
Not by the Python script but on the back-end. The data is sorted in descending order by **clicks** which is also called a **view** thus top 10 viewed aircraft as per project title

#### How is null data represented?
It is represented by the text string **None**

#### How did you find the API endpoint?
I loaded the page https://flightradar24.com and hit f12 to observe the network tab. Once the data was loaded, I looked for all json responses with status code 200. That's usually a good place to start looking for this type of data. It's easy to find from there. The key is to not waste your time looking for it without using this to hone in on the right neighborhood. Otherwise it can be kind of tedious like finding a needle in a haystack.


[^1]: * [Airline and Location Code Search](https://www.iata.org/en/publications/directories/code-search/). _International Air Traffic Association_. Retrieved 2022-02-20.
