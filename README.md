# shopify-challenges
Repo for shopify Challenges

## Barebones online marketplace

For my take on this challenge, I decided to take the word "barebones" to heart. 
Whereas other solutions may implement the use of helpful frameworks like Ruby on 
Rails or Flask, I decided to do a REST API implementation with absolutely no 
external dependencies other than a standards compliant interpreter of Python 3.

It is my opinion that every developer should be required to take at least some time
to really get into the nitty gritty of the whole stack they're working on - I have seen
many occasions in the past where failure to understand the underworkings of a system have
lead to inefficiencies, mistakes, and delays.

In the spirit of this mindset, I've decided to start on a fairly low (but not too low) foundation to build my REST API on.
With this ~100 line python script, I have been able to build a server to exactly these specs:

- "Build a server side web api that can be used to fetch products either one at a time or all at once."

- "Every product should have a title, price, and inventory_count."

- "Querying for all products should support passing an argument to only return products with available inventory."

- "Products should be able to be "purchased" which should reduce the inventory by 1. Products with no inventory cannot be
   purchased."

Of course, this is definitely not a true production scale API by any means - there's a reason that all those frameworks exist
to abstractify much of this. But I hope that the core take away of this exercise, from me to you, is that I am somebody who
cares enough to really understand the details of everything I'm working on.

I tested the server with Postman v6.7.1. You can find a live copy of the server (with this exact code) running on
`###.###.#.#`.

### Full documentation

- `GET /catalogue`
  - Optional parameter: `available=1`
  - Returns full catalogue of items. If `available=1` is set, then the output 
      will only return items with positive stock.
  - Example:
    ```
    {"book": {"price": 1, "inventory_count": 5}, "shoe": {"price": 2, "inventory_count": 6}, "food": {"price": 3, "inventory_count": 7}, "bark": {"price": 4, "inventory_count": 8}, "bazz": {"price": 5, "inventory_count": 9}, "booo": {"price": 100, "inventory_count": 0}}
    ```
