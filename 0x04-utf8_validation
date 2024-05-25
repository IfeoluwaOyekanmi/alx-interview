def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the most significant bits
    masks = [0b10000000, 0b11000000, 0b11100000, 0b11110000, 0b11111000]
    
    # For each byte in the data
    for byte in data:
        # Only consider the least significant 8 bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & masks[0]) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & masks[1]) == masks[1]:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & masks[2]) == masks[2]:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & masks[3]) == masks[3]:
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if (byte & masks[0]) != masks[0]:
                return False
            num_bytes -= 1
    
    # If we finish checking all bytes, num_bytes should be 0
    return num_bytes == 0

# Test cases
print(validUTF8([197, 130, 1]))  # Expected output: True (valid UTF-8 sequence)
print(validUTF8([235, 140, 4]))  # Expected output: False (invalid UTF-8 sequence)
