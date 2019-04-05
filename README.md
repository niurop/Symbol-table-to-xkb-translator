# Symbol table to xkb translator.

Simple way to create custom xkb layout.

### Basic usage:

#### Symbol table layout:

First line serves as a guide mask where:
+  k - column of keys on keyboard.
+  K - codes of keys in xkb layout(should be the same for most people).
+  n - symbols printed without modifiers.
+  N - symbols with level modifier (usually Shift/Caps lock).
+  a - symbols printed with group modifier(usually right Alt).
+  A - symbols printed with group and level modifiers.
+  c - symbols printed with layout switch (right Ctrl for me).
+  C - symbols printed with layout switch and level modifier.
+  b - symbols printed with layout switch and group modifier.
+  B - symbols printed with layout switch and group+level modifiers.

Until the line repeating the first one, every line represents key and its corresponding symbols under each mark in the mask.

Finally, under that lies the list mappings between symbols and their meanings.
If no mapping specified Unicode code will be used.

#### Script usage:

Script needs file path and list of 5 symbols which correspond to K in mask, and some combination of 4 others in correct order(usually KnNaA or KcCbB).
The resulting layout will have symbols corresponding to columns specified in second argument.

#### Makefile:

Makefile contains bash scripts for automatically setting up keyboard layout specified in file named special.
