h, m = map(int, input().split());
m = m -45

if m < 0 and h != 0 :
  h = h - 1;
  m = m + 60;
  print(h, m);
elif m < 0 and h == 0 :
  h = h + 23;
  m = m + 60;
  print(h, m);
else :
  print(h, m);