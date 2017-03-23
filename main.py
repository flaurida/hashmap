from hash_map import HashMap

# A basic demo of the methods in our hashmap class
hash_map = HashMap()
print "Welcome to a brief tutorial of our hashmap!\n"
print "At the beginning the hashmap is: " + str(hash_map)

hash_map["AAPL"] = 100
hash_map["GOOG"] = 200
hash_map["SP500"] = 175.75
print "After inserting our positions: " + str(hash_map)

hash_map["GOOG"] = 400
print "After doubling our number of shares in Google: " + str(hash_map)

hash_map.delete("AAPL")
print "After selling all of our shares in Apple: " + str(hash_map)

other_hash_map = HashMap()
other_hash_map["GOOG"] = 100
other_hash_map["DIS"] = 500
print "My friend recommends a different set of positions: " + str(other_hash_map)

hash_map.update(other_hash_map)
print "Our positions after updating with friend's recommendations: " + str(hash_map)

print "A list of tickers of our positions: " + str(hash_map.keys())
print "A list of the number of shares for each position: " + str(hash_map.values())

print "Number of buckets in our hashmap: " + str(hash_map.num_buckets())

hash_map["BRK-A"] = 50
hash_map["AMZN"] = 100
hash_map["FB"] = 150
hash_map["JNJ"] = 200
hash_map["XOM"] = 25
hash_map["GE"] = 250

print "After buying spree we now hold: " + str(hash_map)
print "The total number of buckets is now: " + str(hash_map.num_buckets())
