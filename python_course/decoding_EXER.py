import base64

def encode_text(text):
    # Convert the text to bytes
    text_bytes = text.encode('utf-8')
    
    # Encode the bytes using Base64
    encoded_bytes = base64.b64encode(text_bytes)
    
    # Convert the encoded bytes back to a string
    encoded_text = encoded_bytes.decode('utf-8')
    
    return encoded_text

def decode_text(encoded_text):
    # Convert the encoded text to bytes
    encoded_bytes = encoded_text.encode('utf-8')
    
    # Decode the bytes using Base64
    decoded_bytes = base64.b64decode(encoded_bytes)
    
    # Convert the decoded bytes back to a string
    decoded_text = decoded_bytes.decode('utf-8')
    
    return decoded_text

# Example usage
original_text = "Hello, this is a sample text."

# Encoding the text
encoded_text = encode_text(original_text)
print("Encoded Text:", encoded_text)

# Decoding the text
decoded_text = decode_text(encoded_text)
print("Decoded Text:", decoded_text)
