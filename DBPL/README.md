# Big Data Analysis Frequent itemsets assignment

## Algorithm

Apriori with first pass counting unique author frequencies and caching `key_to_index` and `index_to_key` lists. Subsequent passes make a dictionary of each supported author from the previous pass, and use this to lazily create n-tuples when encountering them in the baskets (only baskets with at least n items are considered). Tuples are then filtered on support threshold and passed to the next pass.

Progress is indicated when reading the input file, and relevant data is printed during execution.

## Encountered problems

We first created a list of every possible combination within the current pass, but this took a tremendous amount of memory to save.

Now only a hash map (as a Python dict) is kept between passes, which contains only those authors that were frequent in the previous pass. Furthermore, authors are stored as IDs from the `key_to_index` cache. When a basket is read from the file, only authors who appeared in frequent author map are kept. From these combinations are made and added to another dict to count their frequency. Since these newly generated n-tuple combinations consist of only those authors who were already frequent in the previous pass, they are guaranteed to have at most the same frequency, hence no other checks are needed to discard them.

Each pass, the code reads the file again using the `NTupleFrequency` strategy to calculate n-tuple frequencies. The first pass uses a simplified strategy to only count single author frequencies. It would also be possible to use a third strategy to create the baskets in memory, needing to read the file only once. This is however not used, as the point of the assignment was to not read the file into memory, although reading only the author baskets would be feasible.

## Benchmarks

Captured on a system with: `Intel i7 7700k @ 4.8GHz`

| Dataset   | Support threshold | Time (mm:ss) | Memory     |
| --------- | ----------------- | ------------ | ---------- |
| DBPL 50k  | 12                | 00:02        | ~150Mb     |
| DBPL 50k  | 15                | 00:03        | ~150Mb     |
| DBPL full | 12                | 61:06        | 300-600 Mb |
| DBPL full | 15                | 32:01        | 400-600 Mb |

