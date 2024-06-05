weight=int(input('Enter your Weight: '))
unit=input('(L)bs or (k)g: ')

if unit.upper()=='L':
   calculate= weight*0.45
   print(f'Your weight is {calculate} Kilos')

elif unit.upper()=='K':
   calculate= weighr/0.45
   print(f'Your weight is {calculate} Pounds')


