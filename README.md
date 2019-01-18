# shopify-challenges
Repo for shopify Challenges

## Barebones online marketplace

For my take on this challenge, I decided to take the word "barebones" to heart. 
Whereas other solutions may implement the use of helpful frameworks like Ruby on 
Rails or Flask, I decided to do a REST API implementation with absolutely no 
external dependencies other than a standards compliant interpreter of Python 3.

Here, the entirety of the server and rest API is defined in only ~100 lines of 
code; and with no outside dependencies, this means that the audit space for 
issues is extremely tiny!

### Full documentation

- `GET /catalogue`
  - Optional parameter: `available=1`
  - Returns full catalogue of items. If `available=1` is set, then the output 
      will only return items with positive stock.
  - Example:
    ```
    {"book": {"price": 1, "inventory_count": 5}, "shoe": {"price": 2, "inventory_count": 6}, "food": {"price": 3, "inventory_count": 7}, "bark": {"price": 4, "inventory_count": 8}, "bazz": {"price": 5, "inventory_count": 9}, "booo": {"price": 100, "inventory_count": 0}}
    ```
