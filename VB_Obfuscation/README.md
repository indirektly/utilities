# Visual Basic Obfuscation

### VB-obfus-by-oper-simplify.py

This takes variables set and simplifies if operators such as xor are used.

Example:
```
Original Line:
CreateObject(Juliet(Array((57 Xor 105), (92 + (42 Xor 22)), 249, (0 Xor 174))))

Modified:
CreateObject(Juliet(Array(80, 96, 249, 174)))

```

Usage
```
python VB-obfus-by-oper-simplify.py
Usage: VB-obfus-by-oper-simplify FILE_NAME ['LIST_OF_OPERATORS_DELIMITED_BY_A_DASH'] OUT_FILE_NAME
(the OUT_FILE is optional)

python VB-obfus-by-oper-simplify.py VB_macro.vb Xor`+ out.txt
```