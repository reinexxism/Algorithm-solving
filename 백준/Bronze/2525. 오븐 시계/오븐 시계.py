currentH, currentM = map(int, input().split());
needM = int(input());  

currentH += needM // 60;
currentM += needM % 60;

if currentM >= 60 :
  currentH = currentH + 1;
  currentM = currentM - 60;

if currentH >= 24 :
  currentH = currentH - 24;

print(currentH, currentM);