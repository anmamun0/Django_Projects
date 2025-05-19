# GitHub Api Request 

###### API Request URL:

```bash
✅ For your repo: https://github.com/anmamun0/advanced-scientific-calculator

https://api.github.com/repos/anmamun0/advanced-scientific-calculator/git/trees/main?recursive=1
```
###### This will return a JSON object with all files and folders in the repository under the main branch (change main if your default branch has a different name).

---

###### You want to fetch files under the Topic/ directory only.
###### API Endpoint to use:
###### You still use the GitHub Trees API with the ?recursive=1 option:

```bash
✅  https://github.com/anmamun0/Django_Projects/tree/main/Topic

https://api.github.com/repos/anmamun0/Django_Projects/git/trees/main?recursive=1
```
###### This will give you all files and folders in the main branch of Django_Projects. You then filter paths that start with Topic/.

### Decode GtuHub Context

```python
import base64

encoded = "VG90YWwgRXh0cmEgRmVhdHVyZTogMjMKVG90YWwgQnV0dG9ucyA6IDM4Ckhp\nZ2h0IENhbGN1bGF0aW9uIERpZ2l0OjUwCgorLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tCkZ1bGwgU3RvcCBDdXN0b21pemF0aW9uLCAKSGlzdG9y\neSBUcmFjawpaZXJvIERpdml0aW9uIEVycm9yCkltYWdpbmF5IFRyYWNrCldp\nbmRvdyBJY29uCkJpbmFyeS1EZWNpbWFsIC0+PC0KSGV4LURlY2ltYWwgLT48\nLQpPY3QtRGVjaW1hbCAtPjwtClNjaWVudGlmaWMgQ2FsY3VsYXRpb24gPSBT\naW4sIFRhbiwgQ290LCBsb2cxYAo=\n"  # this is a truncated string for example

decoded_bytes = base64.b64decode(encoded)
decoded_text = decoded_bytes.decode('utf-8')

print(decoded_text)

 
txt = 'Hello how are you!'
encoded_bytes = base64.b64encode(txt.encode('utf-8'))
print(encoded_bytes)            # Outputs: b'SGVsbG8gaG93IGFyZSB5b3Uh'
print(encoded_bytes.decode())   # Optional: to get the string version

```

##### Output:
```sh
$ python gitbub_decoding.py 
Total Extra Feature: 23
Total Buttons : 38
Hight Calculation Digit:50

+------------------------------
Full Stop Customization,
History Track
Zero Divition Error
Imaginay Track
Window Icon
Binary-Decimal -><-
Hex-Decimal -><-
Oct-Decimal -><-
Scientific Calculation = Sin, Tan, Cot, log1`
```
