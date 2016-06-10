# Regex matching notes

- Import Regex module with "import re"
- Create Regex with "re.compile()" function with a raw string
- Pass into the "search()" method to return a "Match" object
- Call the match object's "group()" method to return string of matched text.

### Grouping with parentheses

- Example: (\d\d\d)-(\d\d\d-\d\d\d\d)
  - group(1) yields first block
  - group(2) yields second block
  - group() or group(0) yields entire text
  - In this instance, you can then separate them into variables:
    ```python
    areaCode, mainNumber = mo.groups()
    print(areaCode)
    print(mainNumber)
    ```
##Example with phone numbers

```python
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4})
mo = phoneNumRegex.search('My number is 415-515-2423')
print('Phone number found: ' + mo.group())
```
