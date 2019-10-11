# Big Data Analysis Frequent itemsets assignment

2019-10-11 **Cedric Mingneau, William Thenaers**

## Algorithm

Apriori with first pass counting unique author frequencies and caching `key_to_index` and `index_to_key` lists. Subsequent passes make a dictionary of each supported author from the previous pass (using only their ids as keys from `key_to_index`), and use this to lazily create n-tuples when encountering them in the baskets (only baskets with at least n items are considered). After running through the entire file, counted tuples are filtered on support threshold and passed to the next pass.

The supported tuples are chained into a new dict (for O(1) lookup) consisting of every unique author that was supported in the previous pass and these will be used to check if a newly evaluated author was supported and can be used to create new n-tuples.

Progress is indicated when reading the input file, and relevant data is printed during execution, e.g.:

```
> Run with "dblp.xml" and support 12
Start pass 1...
  Finding 1-tuples...: 7075607it [02:04, 57051.80it/s]
  Caching singles LUT...
  Created 2356436 1-tuples.
  249454 1-tuples >= support 12.
Start pass 2...
  249454 supported uniques from previous pass to find tuples.
  Finding 2-tuples...: 100%|#######| 7075607/7075607 [02:13<00:00, 53123.45it/s]
  Created 3371001 2-tuples.
  136019 2-tuples >= support 12.
Start pass 3...
...
```

## Encountered problems

We first created a list of every possible combination within the current pass, but this took a tremendous amount of memory to save.

Now a hash map (as a Python dict) is kept between passes, which contains only those authors that were frequent in the previous pass (`frequency >= support_threshold`). Furthermore, authors are stored as IDs from the `key_to_index` cache. When a basket is read from the file, only authors who appeared in frequent author map are kept. From these, combinations are made and added to another dict to count their frequency. Since these newly generated n-tuple combinations consist of only those authors who were already frequent in the previous pass, they are guaranteed to have at most the same frequency, hence no other checks are needed to discard them.

Each pass, the code reads the file again using the `NTupleFrequency` strategy to calculate n-tuple frequencies. The first pass uses a simplified strategy to only count single author frequencies. It would also be possible to use a third strategy to create the baskets in memory, needing to read the file only once. This is however not used, as the point of the assignment was to not read the file into memory, although reading only the author baskets would be feasible.

## Benchmarks

Captured on a system with: `Intel i7 7700k @ 4.8GHz`

The program output for the settings below can be found in the [benchmarks](./benchmarks) folder.

| Dataset   | Support threshold | Time (mm:ss) | Memory     |
| --------- | ----------------- | ------------ | ---------- |
| DBPL 50k  | 12                | 00:02        | ~150Mb     |
| DBPL 50k  | 15                | 00:03        | ~150Mb     |
| DBPL full | 12                | 61:06        | 300-600 Mb |
| DBPL full | 15                | 32:01        | 400-600 Mb |

## Example output

##### DBPL full dataset with support threshold 12

###### Pass 1

- (,): 6
- (,): 12

###### Pass 2

- (,,): 1
- (,,): 1

###### Pass 3

- (,,,): 1
- (,,,): 1

...

###### Pass 12

- (,,,,,,,,,,,,): 1
- (,,,,,,,,,,,,): 1

...

###### Pass 26

- (,,,,,,,,,,,,,,,,,,,,,,,,,): 1
- (,,,,,,,,,,,,,,,,,,,,,,,,,): 1