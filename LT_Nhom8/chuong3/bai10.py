x = float(input("Richter Magnitude"))
if x > 9.0: 
    print('Causes unbeliveable damage')
elif x > 8.0:
    print('Causes major damage')
elif x > 7.0:
    print('Causes damage to most buildings')
elif x > 6.0:
    print('Causes damage to well-built structures')
elif x > 5.0:
    print('Causes damage to poorly constructed buildings')
elif x > 4.0:
    print("Damge done to weak buildings")
elif x > 2.0:
    print("Very rarely cause of damage")
elif x > 1.0:
    print("Microearthquakes not felt or rarely felt")