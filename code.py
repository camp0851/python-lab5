import camp0851Library;

print('SELECT FUNCTION!');
print('[1] createVerticalLine');
print('[2] createHorizontalLine');
print('[3] createStaircase');
print('[4] randomPixel');
print('[5] clearBacklight');
print('Note: I was unable to get Function 3 to work and as such it is broken.');
print(' ');

selectOption = int(input('Enter option number: '));

if selectOption == 1:
    camp0851Library.createVerticalLine();

elif selectOption == 2:
    camp0851Library.createHorizontalLine();

elif selectOption == 3:
    camp0851Library.createStaircase();

elif selectOption == 4:
    camp0851Library.randonPixel();

elif selectOption == 5:
    camp0851Library.clearBacklight();

else:
    print('Not a valid option!');