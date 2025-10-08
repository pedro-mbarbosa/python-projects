def calculate_storage(filesize):
    block_size = 4096
    full_blocks = block_size // filesize
    partial_block_remainder = block_size % filesize
    
    if partial_block_remainder > 0:
        return 4096 * 2
    return 4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192