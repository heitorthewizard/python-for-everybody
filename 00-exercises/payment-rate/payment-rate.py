fh = float(input('Enter Hours: '))
fr = float(input('Enter Rate: ')) 

if fh > 40:
    print('overtime')
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    print('regular')
    xp = fh * fr

print('Pay:',xp)
