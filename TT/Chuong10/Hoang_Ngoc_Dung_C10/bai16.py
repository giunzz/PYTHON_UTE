def decimal_to_feet_inches(decimal_height):
  feet = int(decimal_height)
  inches = int((decimal_height - feet) * 12)

  return feet, inches
decimal_height = float(input("Enter a decimal height in feet: "))
feet, inches = decimal_to_feet_inches(decimal_height)
print(f"{decimal_height} feet is equal to {feet} feet, {inches} inches.")