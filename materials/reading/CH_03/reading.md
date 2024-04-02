# Commands in Redis

## Overview

Redis is a data storage and caching system known for its simplicity, speed, and versatility. It provides a rich set of commands that allow you to manipulate data, perform various operations, and interact with the Redis server. Here's an overview of some key categories of Redis commands:

**1. Key-Value Commands:**

- **SET**: Set a key to hold a string value.
- **GET**: Get the value of a key.
- **DEL**: Delete a key.
- **EXISTS**: Check if a key exists.
- **EXPIRE**: Set a key's time to live (TTL) in seconds.
- **PERSIST**: Remove the TTL on a key, making it persistent.
- **TTL**: Get the TTL of a key.
- **MSET** and **MGET**: Set or retrieve multiple keys and values at once.
- **INCR** and **DECR**: Increment or decrement the integer value of a key.
- **APPEND**: Append a value to the end of a string.
- **GETSET**: Set the value of a key and return its old value.

**2. Lists Commands:**

- **LPUSH** and **RPUSH**: Push an element to the left or right end of a list.
- **LPOP** and **RPOP**: Pop an element from the left or right end of a list.
- **LRANGE**: Get a range of elements from a list.
- **LINDEX**: Get an element from a list by index.
- **LINSERT**: Insert an element before or after another element in a list.
- **LLEN**: Get the length of a list.
- **LTRIM**: Trim a list to a specified range of elements.

**3. Sets Commands:**

- **SADD**: Add one or more members to a set.
- **SREM**: Remove one or more members from a set.
- **SMEMBERS**: Get all members of a set.
- **SISMEMBER**: Check if a member exists in a set.
- **SCARD**: Get the number of members in a set.
- **SINTER**, **SUNION**, and **SDIFF**: Perform set intersection, union, and difference operations.
- **SRANDMEMBER**: Get one or more random members from a set.

**4. Sorted Sets Commands:**

- **ZADD**: Add one or more members with scores to a sorted set.
- **ZSCORE**: Get the score of a member in a sorted set.
- **ZRANGE**: Get a range of members in ascending order by score.
- **ZREVRANGE**: Get a range of members in descending order by score.
- **ZINCRBY**: Increment the score of a member in a sorted set.
- **ZRANK** and **ZREVRANK**: Get the rank of a member in ascending or descending order.
- **ZREM**: Remove one or more members from a sorted set.

**5. Hashes Commands:**

- **HSET**: Set the field in a hash to a value.
- **HGET**: Get the value of a field in a hash.
- **HMSET** and **HMGET**: Set or retrieve multiple fields and values in a hash.
- **HDEL**: Delete one or more fields from a hash.
- **HEXISTS**: Check if a field exists in a hash.
- **HGETALL**: Get all fields and their values in a hash.
- **HINCRBY** and **HINCRBYFLOAT**: Increment the value of a field in a hash.

**6. Pub/Sub Commands:**

- **PUBLISH**: Publish a message to a channel.
- **SUBSCRIBE**: Subscribe to one or more channels.
- **UNSUBSCRIBE**: Unsubscribe from one or more channels.
- **PSUBSCRIBE**: Subscribe to channels matching a pattern.
- **PUNSUBSCRIBE**: Unsubscribe from channels matching a pattern.

**7. Other Commands:**

- **SELECT**: Change the selected database.
- **FLUSHDB** and **FLUSHALL**: Delete all keys in the current database or all databases.
- **PING**: Check if the server is running.
- **INFO**: Get information and statistics about the Redis server.
- **CONFIG SET** and **CONFIG GET**: Configure server options.
- **BGSAVE** and **BGREWRITEAOF**: Perform background saving and rewriting of append-only files.
- **SCAN** and **SSCAN**: Iterate over keys and sets using cursor-based scanning.

These are just a subset of Redis commands. Redis provides many more commands and features for tasks like scripting, transactions, remote server control, and more. Understanding how to use these commands effectively is essential for developing applications that leverage Redis's capabilities.

### Strings command

**1. SET: Set a key to hold a string value.**

```python
import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')
```

**2. GET: Get the value of a key.**

```python
# Retrieve the value of a key
value = r.get('my_key')
print(value.decode('utf-8'))  # Decode the bytes to a string
```

**3. DEL: Delete a key.**

```python
# Delete a key
r.delete('my_key')
```

**4. EXPIRE: Set a key's time to live (TTL) in seconds.**

```python
# Set a key to expire in 60 seconds
r.expire('my_key', 60)
```

**5. PERSIST: Remove the TTL on a key, making it persistent.**

```python
# Remove the TTL on a key, making it persistent
r.persist('my_key')
```

**6. INCR and DECR: Increment or decrement the integer value of a key.**

```python
# Increment a key's value by 1
r.incr('counter')

# Decrement a key's value by 1
r.decr('counter')
```

**7. MSET and MGET: Set or retrieve multiple keys and values at once.**

```python
# Set multiple key-value pairs
r.mset({'key1': 'value1', 'key2': 'value2'})

# Retrieve values for multiple keys
values = r.mget(['key1', 'key2'])
```

**8. APPEND: Append a value to the end of a string.**

```python
# Append to a string
r.append('my_key', ', how are you?')
```

**9. GETSET: Set the value of a key and return its old value.**

```python
# Set the new value and get the old value
old_value = r.getset('my_key', 'New Value')
```

These are some of the basic string-related Redis commands, and you can use the `redis-py` library in Python to interact with Redis. Make sure to install the library using `pip install redis` if you haven't already.

Remember that Redis strings are binary-safe, so you can store and retrieve any binary data using these commands. When retrieving values, you may need to decode them from bytes to strings, as shown in the `GET` example above.

Feel free to adapt these examples to your specific use case and integrate Redis string commands into your Python applications as needed.

### Lists command

**1. LPUSH and RPUSH: Push an element to the left or right end of a list.**

```python
import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Left push (prepend) an element to a list
r.lpush('my_list', 'item1')

# Right push (append) an element to a list
r.rpush('my_list', 'item2')
```

**2. LPOP and RPOP: Pop an element from the left or right end of a list.**

```python
# Left pop (remove and retrieve) an element from a list
item = r.lpop('my_list')

# Right pop (remove and retrieve) an element from a list
item = r.rpop('my_list')
```

**3. LRANGE: Get a range of elements from a list.**

```python
# Retrieve elements from a list by index range
elements = r.lrange('my_list', 0, -1)  # Get all elements
```

**4. LINDEX: Get an element from a list by index.**

```python
# Retrieve an element from a list by index
element = r.lindex('my_list', 2)
```

**5. LINSERT: Insert an element before or after another element in a list.**

```python
# Insert an element before or after another element in a list
r.linsert('my_list', 'BEFORE', 'item2', 'new_item')
r.linsert('my_list', 'AFTER', 'item2', 'new_item')
```

**6. LLEN: Get the length of a list.**

```python
# Get the length (number of elements) of a list
length = r.llen('my_list')
```

**7. LTRIM: Trim a list to a specified range of elements.**

```python
# Trim a list to keep only the elements within the specified range
r.ltrim('my_list', 0, 2)  # Keep elements at indices 0, 1, and 2
```

**8. BLPOP and BRPOP: Blocking left or right pop. These commands block until an element is available to pop.**

```python
# Blocking left pop (waits for an element)
item = r.blpop('my_list', timeout=30)  # Wait up to 30 seconds for an element
```

**9. BRPOPLPUSH: Pop an element from the right end of one list and push it to the left end of another list.**

```python
# Pop from one list and push to another (atomic operation)
r.brpoplpush('source_list', 'destination_list', timeout=10)  # Wait up to 10 seconds for an element
```

These are some of the basic list-related Redis commands, and you can use the `redis-py` library in Python to interact with Redis lists. Make sure to install the library using `pip install redis` if you haven't already.

Redis lists are often used for implementing queues, stacks, and maintaining ordered collections of data. You can adapt these examples to your specific use cases and integrate Redis list commands into your Python applications as needed.

### Sets command

Certainly! Here are details on common Redis set commands along with their usage in Python using the `redis-py` library:

**1. SADD: Add one or more members to a set.**

   ```python
   r.sadd('my_set', 'member1', 'member2', 'member3')
   ```

**2. SREM: Remove one or more members from a set.**

   ```python
   r.srem('my_set', 'member2', 'member3')
   ```

**3. SMEMBERS: Get all members of a set.**

   ```python
   members = r.smembers('my_set')
   ```

**4. SISMEMBER: Check if a member exists in a set.**

   ```python
   is_member = r.sismember('my_set', 'member1')
   ```

**5. SCARD: Get the number of members in a set.**

   ```python
   num_members = r.scard('my_set')
   ```

**6. SINTER: Get the intersection of multiple sets.**

   ```python
   intersection = r.sinter('set1', 'set2', 'set3')
   ```

**7. SUNION: Get the union of multiple sets.**

   ```python
   union = r.sunion('set1', 'set2', 'set3')
   ```

**8. SDIFF: Get the difference between two sets.**

   ```python
   difference = r.sdiff('set1', 'set2')
   ```

**9. SRANDMEMBER: Get one or more random members from a set.**

   ```python
   random_member = r.srandmember('my_set')
   ```

**10. SPOP: Remove and return one or more random members from a set.**

   ```python
   popped_member = r.spop('my_set')
   ```

**11. SMEMBERS: Get all members of a set.**

   ```python
   members = r.smembers('my_set')
   ```

**12. SINTERSTORE, SUNIONSTORE, SDIFFSTORE: Store the results of set operations in a new set.**

   ```python
   r.sinterstore('result_set', 'set1', 'set2')
   r.sunionstore('result_set', 'set1', 'set2')
   r.sdiffstore('result_set', 'set1', 'set2')
   ```

**13. SRANDMEMBER: Get one or more random members from a set.**

   ```python
   random_member = r.srandmember('my_set', count=2)
   ```

**14. SMOVE: Move a member from one set to another.**

   ```python
   r.smove('source_set', 'destination_set', 'member_to_move')
   ```

These are the fundamental Redis set commands you can use with the `redis-py` library in Python. Sets are useful for maintaining collections of unique values and performing set operations like intersection, union, and difference.

### Hashes command

**1. HSET: Set the field in a hash to a value.**

   ```python
   r.hset('my_hash', 'field1', 'value1')
   ```

**2. HGET: Get the value of a field in a hash.**

   ```python
   value = r.hget('my_hash', 'field1')
   ```

**3. HMSET and HMGET: Set or retrieve multiple fields and values in a hash.**

   ```python
   r.hmset('my_hash', {'field1': 'value1', 'field2': 'value2'})
   values = r.hmget('my_hash', ['field1', 'field2'])
   ```

**4. HDEL: Delete one or more fields from a hash.**

   ```python
   r.hdel('my_hash', 'field1', 'field2')
   ```

**5. HEXISTS: Check if a field exists in a hash.**

   ```python
   exists = r.hexists('my_hash', 'field1')
   ```

**6. HGETALL: Get all fields and their values in a hash.**

   ```python
   all_data = r.hgetall('my_hash')
   ```

**7. HINCRBY and HINCRBYFLOAT: Increment the value of a field in a hash.**

   ```python
   r.hincrby('my_hash', 'field1', 5)
   r.hincrbyfloat('my_hash', 'field2', 3.14)
   ```

**8. HKEYS: Get all field names in a hash.**

   ```python
   field_names = r.hkeys('my_hash')
   ```

**9. HVALS: Get all field values in a hash.**

   ```python
   field_values = r.hvals('my_hash')
   ```

**10. HLEN: Get the number of fields in a hash.**

   ```python
   num_fields = r.hlen('my_hash')
   ```

**11. HSETNX: Set the field in a hash to a value if the field does not exist.**

   ```python
   r.hsetnx('my_hash', 'field1', 'new_value')
   ```

**12. HSTRLEN: Get the length of the value of a field in a hash.**

   ```python
   length = r.hstrlen('my_hash', 'field1')
   ```

**13. HSCAN: Iterate over fields and values in a hash using cursor-based scanning.**

   ```python
   cursor, items = r.hscan('my_hash', cursor=0, count=10)
   ```

**14. HMSET and HMGET for Nested Hashes:**

   Nested hashes are supported. You can use the same commands to set and retrieve values in nested hashes.

   ```python
   r.hmset('my_nested_hash', {'field1.subfield1': 'value1', 'field1.subfield2': 'value2'})
   value = r.hget('my_nested_hash', 'field1.subfield1')
   ```

These are the fundamental Redis hash commands you can use with the `redis-py` library in Python. Hashes are useful for representing structured data and objects in Redis. You can adapt these examples to your specific use cases and integrate Redis hash commands into your Python applications as needed.

### Sorted sets commands

**1. ZADD: Add one or more members with scores to a sorted set.**

```python
r.zadd('my_sorted_set', {'member1': 10, 'member2': 20})
```

**2. ZSCORE: Get the score of a member in a sorted set.**

```python
score = r.zscore('my_sorted_set', 'member1')
```

**3. ZRANGE and ZREVRANGE: Get a range of members by their rank (index) in ascending or descending order.**

```python
members_asc = r.zrange('my_sorted_set', start=0, end=-1)
members_desc = r.zrevrange('my_sorted_set', start=0, end=-1)
```

**4. ZINCRBY: Increment the score of a member in a sorted set.**

```python
r.zincrby('my_sorted_set', 5, 'member1')
```

**5. ZRANK and ZREVRANK: Get the rank (index) of a member in ascending or descending order.**

```python
rank_asc = r.zrank('my_sorted_set', 'member1')
rank_desc = r.zrevrank('my_sorted_set', 'member1')
```

**6. ZREM: Remove one or more members from a sorted set.**

```python
r.zrem('my_sorted_set', 'member1', 'member2')
```

**7. ZRANGEBYSCORE and ZREVRANGEBYSCORE: Get a range of members by their score in ascending or descending order.**

```python
members_by_score_asc = r.zrangebyscore('my_sorted_set', min=0, max=50)
members_by_score_desc = r.zrevrangebyscore('my_sorted_set', min=50, max=0)
```

**8. ZCOUNT: Count the number of members within a score range.**

```python
count = r.zcount('my_sorted_set', min=0, max=50)
```

**9. ZCARD: Get the number of members in a sorted set.**

```python
num_members = r.zcard('my_sorted_set')
```

**10. ZREMRANGEBYRANK and ZREMRANGEBYSCORE: Remove members by their rank or score range.**

```python
r.zremrangebyrank('my_sorted_set', start=0, end=2)
r.zremrangebyscore('my_sorted_set', min=0, max=50)
```

**11. ZRANGEBYLEX and ZREMRANGEBYLEX: Get a range of members lexicographically and remove members by their lexicographical range.**

```python
members_lex = r.zrangebylex('my_sorted_set', min='[a', max='[e')
r.zremrangebylex('my_sorted_set', min='[a', max='[e')
```

**12. ZLEXCOUNT: Count the number of members within a lexicographical range.**

```python
count = r.zlexcount('my_sorted_set', min='[a', max='[e')
```

**13. ZINTERSTORE and ZUNIONSTORE: Perform intersection or union of multiple sorted sets and store the result in a new set.**

```python
r.zinterstore('destination_set', {'set1': 1, 'set2': 2})  # Intersection
r.zunionstore('destination_set', {'set1': 1, 'set2': 2})  # Union
```

**14. ZSCAN: Iterate over members in a sorted set using cursor-based scanning.**

```python
cursor, items = r.zscan('my_sorted_set', cursor=0, count=10)
```

These are the fundamental Redis sorted set commands you can use with the `redis-py` library in Python. Sorted sets are useful for maintaining ordered collections of data with unique members and scores. You can adapt these examples to your specific use cases and integrate Redis sorted set commands into your Python applications as needed.

### Pub/sub commands

Certainly! Here are details on common Redis publish/subscribe (pub/sub) commands along with their usage in Python using the `redis-py` library:

**1. PUBLISH: Publish a message to a channel.**

```python
# Publisher
r.publish('my_channel', 'Hello, subscribers!')
```

**2. SUBSCRIBE: Subscribe to one or more channels.**

```python
import redis

# Create a subscriber instance
subscriber = redis.Redis(host='localhost', port=6379, db=0)

# Subscribe to a channel
subscriber.subscribe('my_channel')
```

**3. UNSUBSCRIBE: Unsubscribe from one or more channels.**

```python
# Unsubscribe from a channel
subscriber.unsubscribe('my_channel')
```

**4. PSUBSCRIBE: Subscribe to channels matching a pattern.**

```python
# Subscribe to channels matching a pattern
subscriber.psubscribe('user_*')
```

**5. PUNSUBSCRIBE: Unsubscribe from channels matching a pattern.**

```python
# Unsubscribe from channels matching a pattern
subscriber.punsubscribe('user_*')
```

**6. Message Handling:**

- When messages are published to a channel or channels matching a pattern, the subscriber can receive and handle these messages in real-time. 
- You typically use a callback function to process messages.

```python
import redis

def message_handler(message):
    print(f"Received message: {message['data']}")

# Create a subscriber instance
subscriber = redis.Redis(host='localhost', port=6379, db=0)

# Subscribe to a channel and specify the callback function
subscriber.subscribe(**{'my_channel': message_handler})
```

In this example, the `message_handler` function will be called whenever a message is received on the 'my_channel' channel.

**7. PUBLISH/SUBSCRIBE Interaction:**

You can have separate Redis connections for publishing and subscribing. Publishers publish messages to channels, and subscribers receive messages from channels. There's no direct interaction between publishers and subscribers.

```python
# Publisher
r.publish('my_channel', 'Hello, subscribers!')

# Subscriber
import redis

def message_handler(message):
    print(f"Received message: {message['data']}")

subscriber = redis.Redis(host='localhost', port=6379, db=0)
subscriber.subscribe(**{'my_channel': message_handler})
```

**8. Unsubscribing:**

Subscribers can unsubscribe from channels or patterns at any time using `unsubscribe` or `punsubscribe`.

```python
# Unsubscribe from 'my_channel'
subscriber.unsubscribe('my_channel')

# Unsubscribe from channels matching 'user_*'
subscriber.punsubscribe('user_*')
```

**9. Limitations:**

- Redis pub/sub is best suited for real-time messaging within a single Redis server or a small cluster.
- It's not a full-fledged message queue and doesn't guarantee message persistence or delivery to offline subscribers.

These are the fundamental Redis pub/sub commands and concepts you can use with the `redis-py` library in Python. Pub/sub is useful for building real-time communication and notification systems. You can adapt these examples to your specific use cases and integrate Redis pub/sub commands into your Python applications as needed.

### Sorting command

Redis provides a powerful sorting capability using the `SORT` command. Sorting can be applied to lists, sets, and sorted sets. Below are details on sorting commands in Redis, along with their usage in Python using the `redis-py` library.

**SORT Command:**

The `SORT` command allows you to sort the elements of a list, set, or sorted set based on various criteria and return the sorted elements. You can specify options such as sorting by scores, lexicographically, and more.

Here's the basic syntax of the `SORT` command:

```plaintext
SORT source [BY pattern] [LIMIT offset count] [GET pattern [GET pattern ...]] [ASC|DESC] [ALPHA] [STORE destination]
```

- `source`: The key of the data structure you want to sort.
- `BY pattern`: Optional. Specify a pattern to use for sorting.
- `LIMIT offset count`: Optional. Limit the number of results returned.
- `GET pattern`: Optional. Get values associated with elements in the result.
- `ASC` or `DESC`: Optional. Sort in ascending or descending order.
- `ALPHA`: Optional. Sort lexicographically (for strings).
- `STORE destination`: Optional. Store the result in a new key.

**Sorting Examples with Python (`redis-py`):**

Here are some examples of using the `SORT` command with `redis-py`:

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Example 1: Basic sorting of a list in ascending order
result = r.sort('my_list')

# Example 2: Sorting a list in descending order
result = r.sort('my_list', desc=True)

# Example 3: Sorting a set using an external key pattern
result = r.sort('my_set', by='external_*')

# Example 4: Sorting and limiting results
result = r.sort('my_list', start=0, num=5)

# Example 5: Sorting and getting values associated with elements
result = r.sort('my_set', get='external_*->field1')

# Example 6: Sorting and storing the result in a new key
r.sort('my_list', store='sorted_list')
```

These examples demonstrate some common use cases for sorting in Redis using the `SORT` command and how to execute them using the `redis-py` library in Python.

Sorting in Redis is flexible and powerful, allowing you to sort data based on various criteria and store or use the sorted result as needed in your application.

### Basic Redis transactions commands

Redis supports basic transactions using the `MULTI`, `EXEC`, and `DISCARD` commands. These commands allow you to group multiple Redis commands into a single transaction, ensuring that all commands within the transaction are executed atomically.

Here's how basic Redis transactions work in detail, along with their usage in Python using the `redis-py` library:

**1. MULTI: Start a Transaction**

The `MULTI` command is used to initiate a new transaction. After issuing this command, Redis will queue up subsequent commands as part of the transaction until you explicitly execute them with `EXEC`. If you want to cancel the transaction, you can use `DISCARD`.

**Usage in Python (`redis-py`):**

```python
import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Start a transaction
pipe = r.pipeline()
pipe.multi()
```

**2. Queue Transactional Commands**

Between the `MULTI` and `EXEC` commands, you can queue up any Redis commands you want to execute atomically. These commands are not executed immediately; they are stored in a queue.

**Usage in Python (`redis-py`):**

```python
# Queue commands in the transaction
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
```

**3. EXEC: Execute the Transaction**

The `EXEC` command is used to execute all the queued commands as a single atomic transaction. If any of the commands fail, none of the changes are applied.

**Usage in Python (`redis-py`):**

```python
# Execute the transaction
response = pipe.execute()
```

The `response` will contain the results of each command in the same order they were queued. If the transaction was successful, the response will be a list of values corresponding to the commands.

**4. DISCARD: Cancel the Transaction**

If you decide to cancel a transaction before executing it, you can use the `DISCARD` command. This command discards all the queued commands and ends the transaction.

**Usage in Python (`redis-py`):**

```python
# Cancel the transaction
pipe.discard()
```

**Example of Using Redis Transactions in Python:**

Here's a complete example of using Redis transactions with `redis-py`:

```python
import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Start a transaction
pipe = r.pipeline()
pipe.multi()

# Queue commands in the transaction
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')

# Execute the transaction
response = pipe.execute()

# Check the response (list of results)
for result in response:
    print(result)
```

In this example, the two `SET` commands are queued in a transaction, and `EXEC` is used to execute them atomically. The results of the `SET` commands are printed after execution.

Redis transactions are useful for ensuring the atomicity of multiple Redis commands. They are especially valuable when you need to perform multiple operations as a single, indivisible unit of work.

### Expiring keys commands

In Redis, you can set keys to expire after a certain amount of time using the `EXPIRE`, `PEXPIRE`, `EXPIREAT`, and `PEXPIREAT` commands. These commands allow you to automatically delete keys after a specified duration or at a specific timestamp. Here are the details of these commands and how to use them in Python with the `redis-py` library:

**1. EXPIRE: Set a Key's Time to Live (TTL) in Seconds**

The `EXPIRE` command sets a key's time to live (TTL) in seconds. After the specified time elapses, Redis will automatically delete the key.

```python
import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set the TTL for a key to 60 seconds
r.expire('my_key', 60)
```

**2. PEXPIRE: Set a Key's Time to Live (TTL) in Milliseconds**

The `PEXPIRE` command is similar to `EXPIRE`, but it sets the TTL in milliseconds instead of seconds.

```python
# Set the TTL for a key to 1000 milliseconds (1 second)
r.pexpire('my_key', 1000)
```

**3. EXPIREAT: Set a Key's Time to Live (TTL) Using a Unix Timestamp**

The `EXPIREAT` command allows you to set a key's TTL by specifying a Unix timestamp (seconds since January 1, 1970). Redis will automatically delete the key when the specified timestamp is reached.

```python
import time

# Calculate a timestamp for 10 minutes from now
timestamp = int(time.time()) + 600

# Set the key to expire at the calculated timestamp
r.expireat('my_key', timestamp)
```

**4. PEXPIREAT: Set a Key's Time to Live (TTL) Using a Unix Timestamp in Milliseconds**

The `PEXPIREAT` command is similar to `EXPIREAT`, but it sets the TTL using a Unix timestamp in milliseconds.

```python
# Calculate a timestamp in milliseconds for 10 minutes from now
timestamp_ms = int(time.time() * 1000) + 600000

# Set the key to expire at the calculated timestamp in milliseconds
r.pexpireat('my_key', timestamp_ms)
```

**Checking TTL:**

You can check the remaining time to live (TTL) of a key using the `TTL` and `PTTL` commands (in seconds and milliseconds, respectively).

```python
# Get the remaining TTL of a key in seconds
ttl_seconds = r.ttl('my_key')

# Get the remaining TTL of a key in milliseconds
ttl_milliseconds = r.pttl('my_key')
```

**Removing TTL:**

To remove the TTL of a key and make it persistent, you can use the `PERSIST` command.

```python
# Remove the TTL of a key, making it persistent
r.persist('my_key')
```

These commands provide fine-grained control over the expiration of keys in Redis, allowing you to implement features like caching and automatic data cleanup in your applications. Use them according to your specific use case and requirements.