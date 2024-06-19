for i in range (11, 101):
  print("h",i, "= net.get('h",i, "')")
  print('cmd1 = "bash normal.sh &"')
  print("h",i, ".cmd(cmd1)")
  print()