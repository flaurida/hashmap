# HashMap

## Overview

In this repo I implement a hashmap with amortized constant time lookups in Python without using a hashmap primitive.

The way I implemented the hashmap was by creating a list of linked lists, where each linked list node stores a key/value pair in the hashmap. Conceptually, these linked lists can be thought of as "buckets" that store a subset of the key/value pairs in the entire hashmap. In order to determine which bucket a given key/value pair  belongs on, I use a hash function (from Python's `hashlib` module) and take the output % the total number of buckets to give the index in the list of the appropriate bucket. The reason I chose to use a linked list for each bucket is it allows for constant time insertion and deletion one a specific node is found.

This implementation allows for amoritzed constant time lookup becuase I make sure that the number of key/value pairs does not exceed the number of buckets. Therefore, on average each bucket will contain one key/value pair, which allows for amortized constant time lookup. This also allows for amortized constant time insertion, updating, and deletion. Of course, ensuring that the number of buckets is at least as many as the total number of key/value pairs involves growing and shrinking the number of buckets when the number of key/value pairs reaches a specific threshold. Though the resizing operation is linear time with respect to the number of key/value pairs, because it only happens occasionally the total cost of the operation is amortized over time. Specifically, the number of buckets doubles when the number of key/value pairs exceeds the number of buckets, and is halved when the number of key/value pairs falls short of a quarter of the number of buckets.

## Setup

This repo includes unittest files for the [hashmap](./hash_map_tests.py) as well as the [linked list](./linked_list_tests.py) that represents each bucket in the hashmap. I also include a [basic script](./main.py) that can be run to show the basic functionality of the hashmap.

## TL;DR

1. Clone this repo
2. cd `hashmap`
3. run `python main.py` for brief tutorial
4. run `python hash_map_tests.py` to run tests on the hashmap
5. run `python linked_list_tests.py` to run tests on the linked list "buckets"

Thanks for visiting! :)
