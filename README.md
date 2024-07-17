# Beautiful Soup and Base64 Examples

Welcome to the **Beautiful Soup and Base64 Examples** repository! This repository provides examples of how to use Beautiful Soup for HTML parsing and how to encode and decode data using base64 in Python.

## Table of Contents

- [Installation](#installation)
- [Examples](#examples)
- [Beautiful Soup Example](#beautiful-soup-example)
- [Base64 Encoding and Decoding Example](#base64-encoding-and-decoding-example)
- [Combined Example](#combined-example)
- [Data](#data)

## Installation

To install the necessary dependencies, you can use pip and the provided `requirements.txt` file. Run the following command:

```
pip install -r requirements.txt
```

## Examples

### Beautiful Soup Example

This example demonstrates how to parse HTML using Beautiful Soup. The script `beautiful_soup_example.py` shows how to read an HTML document, parse it, and extract information from it.

```python
# src/beautiful_soup_example.py

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
print(soup.title.string)
print(soup.find_all('a'))
print(soup.get_text())
```

### Base64 Encoding and Decoding Example

This example demonstrates how to encode and decode data using base64. The script `base64_example.py` shows how to perform base64 encoding and decoding operations.

```python
# src/base64_example.py

import base64

data = "Hello, World!"
encoded_data = base64.b64encode(data.encode('utf-8'))

print(encoded_data)  # Output: b'SGVsbG8sIFdvcmxkIQ=='

decoded_data = base64.b64decode(encoded_data).decode('utf-8')

print(decoded_data)  # Output: Hello, World!
```

### Combined Example

This example combines the usage of Beautiful Soup and base64 encoding/decoding. The script `combined_example.py` shows how to parse HTML, extract text, and then encode and decode that text using base64.

```python
# src/combined_example.py

from bs4 import BeautifulSoup
import base64

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
text = soup.get_text()

encoded_text = base64.b64encode(text.encode('utf-8'))
print(encoded_text)  # Encoded text

decoded_text = base64.b64decode(encoded_text).decode('utf-8')
print(decoded_text)  # Decoded text
```

## Data

The `data/` directory contains a sample HTML file (`sample.html`) used in the Beautiful Soup examples.

### Sample HTML File

```html
<!-- data/sample.html -->
<html>
  <head>
    <title>The Dormouse's story</title>
  </head>
  <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
      and they lived at the bottom of a well.</p>
    <p class="story">...</p>
  </body>
</html>
```

## Contributing

Feel free to contribute by submitting a pull request. Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.