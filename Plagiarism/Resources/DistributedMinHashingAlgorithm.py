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
