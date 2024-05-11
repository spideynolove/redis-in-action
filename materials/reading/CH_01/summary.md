# Getting to know Redis

## What is Redis?
---

### Section 1.1: What is Redis?

**1.1.1 Redis compared to other databases and software**

Redis is described as a fast, non-relational (NoSQL) database that stores keys in various data structures. Unlike relational databases that manage tables and relationships, Redis operates with a simpler, more flexible model where keys are directly mapped to types of values like strings, lists, sets, hashes, and sorted sets. This makes Redis somewhat similar to memcached but with richer data type support and built-in persistence capabilities. Redis excels in scenarios where high performance and flexible data structures are required.

**1.1.2 Other features**

Redis also offers features that go beyond simple key-value storage, which include:
- **Persistence**: Redis can write in-memory data to disk using snapshots or an append-only file, ensuring data is not lost on server restarts.
- **Replication**: To increase read performance or provide failover support, Redis supports master/slave replication. Changes made on the master server are replicated to one or more slave servers, which can serve read queries and provide redundancy.
- **Scalability**: Client-side sharding can be used to distribute data across multiple Redis instances, improving write performance by partitioning data.

**1.1.3 Why Redis?**

The section concludes by highlighting the benefits of using Redis over other technologies. Redis is particularly useful when high performance is required and when working with simple data models that do not require complex relationships between data entities. It simplifies many scenarios, such as caching, that would otherwise require more complex solutions when using traditional databases. Redis offers both speed and simplicity by providing native support for manipulating various types of data structures directly in memory.

---

### Section 1.2: What Redis Data Structures Look Like

**1.2.1 Strings in Redis**

Strings in Redis are simple text or binary data, similar to strings in most programming languages. Redis not only allows for simple operations such as setting, getting, and deleting strings but also supports more complex manipulations like appending, slicing, and atomic increments/decrements, which can treat strings as numeric values for counters.

**1.2.2 Lists in Redis**

Lists in Redis are sequences of strings sorted by insertion order, making them similar to lists or arrays in programming languages but with the added benefit of supporting operations at both ends. This makes them particularly useful for stacks or queues. Redis provides commands for pushing and popping items, accessing elements by index, and slicing, which are crucial for many queue-based tasks.

**1.2.3 Sets in Redis**

Redis sets are collections of unique strings that offer powerful operations to handle unique items efficiently. Redis supports typical set operations like addition, removal, and membership tests, along with more complex operations such as intersections, unions, and differences between sets, facilitating complex set algebra operations quickly.

**1.2.4 Hashes in Redis**

Hashes in Redis are collections of key-value pairs where both keys and values are strings. This structure is similar to objects or dictionaries in other languages, making them ideal for representing objects (like storing different fields associated with a particular object). Redis allows direct access to any field within a hash, updating fields individually, and incrementally altering numerical fields.

**1.2.5 Sorted Sets in Redis**

Sorted sets, or ZSets, are perhaps the most complex data structure in Redis. They are similar to sets but with the addition of a score that is used to order elements. Each element in a sorted set is unique, but unlike regular sets, every element has a floating-point score that determines its order. This allows for retrieval of elements based on their score range, making sorted sets excellent for priority queues, leaderboards, and more.

---

### Section 1.3: Hello Redis

**1.3.1 Voting on articles**

This subsection describes the implementation of a voting system for articles, where articles are scored based on the time of posting and the number of votes they receive. Each vote adds a certain number of points to the article’s score, calculated from the time elapsed since the article was posted.

- **Data Structures Used**: 
  - **ZSET**: Used for storing articles sorted by score and time. Each article’s ID is stored as a member with its score as the value in the sorted set.
  - **HASH**: Each article is stored in a hash containing fields such as title, poster, link, time of posting, and vote count.
  - **SET**: For each article, a set is used to store user IDs who have voted, preventing duplicate votes.

- **Operations**:
  - Checking article's eligibility for voting based on its posting time.
  - Updating article score and vote count upon receiving a new vote.

**1.3.2 Posting and fetching articles**

This subsection explains how to post new articles and retrieve lists of articles based on scores or the time of posting. 

- **Posting Articles**:
  - A unique article ID is generated using Redis's `INCR` command.
  - Article details are stored in a hash.
  - Initial scores are set in sorted sets for time-based and score-based retrieval.

- **Fetching Articles**:
  - Articles are fetched by their score or posting time using `ZRANGE` or similar commands.
  - Details of each article are retrieved from their respective hashes using `HGETALL`.

**1.3.3 Application Components**:
  - The example consolidates knowledge about Redis's ability to handle real-time data manipulation, showcasing how to effectively use different data structures in unison.
  - Demonstrates how Redis can be used for tasks typically handled by more complex database systems, such as relational databases.

---