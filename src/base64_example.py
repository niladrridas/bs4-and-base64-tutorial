# src/base64_example.py

import base64

data = "Hello, World!"
encoded_data = base64.b64encode(data.encode('utf-8'))

print(encoded_data)  # Output: b'SGVsbG8sIFdvcmxkIQ=='

decoded_data = base64.b64decode(encoded_data).decode('utf-8')

print(decoded_data)  # Output: Hello, World!
