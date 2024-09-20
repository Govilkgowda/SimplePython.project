weight=int(input('Enter your Weight: '))
unit=input('It is in (L)bs or (k)g: ')

if unit.upper()=='L':
   calculate= weight*0.45
   print(f'Your weight is {calculate} Kilos')

elif unit.upper()=='K':
   calculate= weight//0.45
   print(f'Your weight is {calculate} Pounds')


