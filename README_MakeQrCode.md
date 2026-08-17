# 📷 Create QR code (`MakeQrcode.py`)

This script takes a site address from the user and creates a QR code image for it.

---

## How to run

```bash
python MakeQrcode.py
```

### Example

```
Enter the site address : https://example.com
```

Output: A file named `qrcode.png` is created in the same folder, which opens the entered address when scanned.

---

## Required libraries

```bash
pip install qrcode[pil]
```

---

## Script code

```python
import qrcode

url = input("Enter the site address : ")

img = qrcode.make(url)

img.save("qrcode.png")
```

---

## License

This project is released under the MIT license.

## Author

[Mehdi] - Computer student and interested in security and programming
