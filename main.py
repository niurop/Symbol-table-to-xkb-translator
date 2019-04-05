from sys import argv
with open(argv[1]) as file:
  lines = file.read().splitlines()
  mask = lines[0]
  divider = 1 + lines[1:].index(mask)
  indexesToRead = [mask.index(s) for s in argv[2]]
  symbols = {}
  for definition in lines[1 + divider:]:
    symbols[definition[0]] = definition[2:]
  translate = lambda s: symbols.get(s, 'U' + hex(ord(s))[2:])
  output = 'default  partial\nxkb_symbols "basic" {\n'
  for line in lines[1:divider]:
    output += '\tkey <{}> {{ [{} ] }};\n'.format(line[indexesToRead[0]:indexesToRead[0]+4],
      ','.join([' '+(translate(line[i]) if i<len(line) else 'NoSymbol') for i in indexesToRead[1:]]))
  output += '\tinclude "level3(ralt_switch)"\n\n};'
  print(output)
