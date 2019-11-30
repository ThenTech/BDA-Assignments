# v3 ------------------------------------------------------------------------------

# For each col/file in SignMatrix
for col in range(len(SignMatrix[0])):
    # For each hashed shingle in the file's multiset
    # This is the domain we are interested in
    for x in hashed_shingle_multisets[col]:
        # Iterate over permutation hashes (rows from SM)
        for row, h in enumerate(pHashes):
            hashval = h(x)
            # Check if the new value is lower, and replace
            if hashval < SignMatrix[col][row]:
                SignMatrix[col][row] = hashval

# v2 ------------------------------------------------------------------------------

# For each value from the shingles hash domain
for x in image(shingle_hash):
    # For each col/file in SignMatrix
    for col in range(len(SignMatrix[0])):
        # Iterate over permutation hashes (rows from SM)
        for row, h in enumerate(pHashes):
            hashval = h(x)
            # Check if the new value is lower, and replace
            if hashval < SignMatrix[row][col]:
                SignMatrix[row][col] = hashval

# v1 ------------------------------------------------------------------------------

# p_hashes is the collection of permutation hash functions
for h in p_hashes:
    # shingle_hash is the hash function that hashed the
    # shingles image(shingle_hash) == all row indices of bit vector!
    for x in image(shingle_hash):
        # hashed_shingle_multiset contains all hashed shingle of a document
        if (h(x) in hashed_shingle_multiset):
            file_signature_matrix.add(x)
            break
# the image of every p_hash function must equal
# the image of shingle_hash function
