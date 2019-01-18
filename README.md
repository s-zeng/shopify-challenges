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

1. "Build a server side web api that can be used to fetch products either one at a time or all at once."
2. "Every product should have a title, price, and inventory_count."
3. "Querying for all products should support passing an argument to only return products with available inventory."
4. "Products should be able to be "purchased" which should reduce the inventory by 1. Products with no inventory cannot be
    purchased."

Of course, this is definitely not a true production scale API by any means - there's a reason that all those frameworks exist
to abstractify much of this. But I hope that the core take away of this exercise, from me to you, is that I am somebody who
cares enough to really understand the details of everything I'm working on.

I tested the server with Postman v6.7.1. You can find a live copy of the server (with this exact code) running on
http://corn-syrup.csclub.uwaterloo.ca:5678/ - feel free to test it out there.

### Full documentation

- `GET /fetch`
  - Required parameter: `name1=&name2=&...`
  - Returns the titles, prices, and inventory_counts of each given id name_1 through name_n
  - Returns null for a given name_n if name_n does not exist in database
  - Satisfies requirement 1, 2
  - Example for `GET /fetch?book=&bark=`:
    ```
    {"book": {"title": "book", "price": 1, "inventory_count": 5}, "bark": {"title": "bark", "price": 4, "inventory_count": 8}}
    ```
- `GET /catalogue`
  - Optional parameter: `available=1`
  - Returns full catalogue of items. If `available=1` is set, then the output 
      will only return items with positive stock.
  - Satisfies requirement 2, 3
  - Example:
    ```
    {"book": {"price": 1, "inventory_count": 5}, "shoe": {"price": 2, "inventory_count": 6}, "food": {"price": 3, "inventory_count": 7}, "bark": {"price": 4, "inventory_count": 8}, "bazz": {"price": 5, "inventory_count": 9}, "booo": {"price": 100, "inventory_count": 0}}
    ```
- `POST /buy`
  - Required parameter:`name1=count1&name2=count2...`
  - We define a "purchase" as a decrease in the stock of an item
  - Sets the remaining inventory_count of each name_1 item to the difference between the current inventory_count and the count_n
    parameter, unless the purchase would put the inventory count below 0 (in which case it would simply be set to 0)
  - Returns the updated state of each name_n, in the same manner as fetch
  - Satisfies requirement 4
  - Example for `POST /buy?book=2&bark=10`:
    ```
    {"book": {"title": "book", "price": 1, "inventory_count": 3}, "bark": {"title": "bark", "price": 4, "inventory_count": 0}}
    ```
 
 (there's also the undocumented `POST /unbuy` (which is exactly what it sounds like) that you can use for tinkering around on the server)
 
 That's it from me folks. Hope to see you all soon.
