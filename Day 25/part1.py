def snafu_to_decimal(snafu):
  # Initialize a dictionary to convert SNAFU digits to their decimal values
  digit_values = {
      "2": 2,
      "1": 1,
      "0": 0,
      "-": -1,
      "=": -2
  }
  
  # Initialize a variable to store the decimal equivalent of the SNAFU number
  decimal = 0
  
  # Iterate through each digit in the SNAFU number, from right to left
  for i, digit in enumerate(snafu[::-1]):
    # Convert the SNAFU digit to its decimal value using the dictionary
    value = digit_values[digit]
    # Calculate the place value of the digit using the SNAFU place values (powers of 5)
    place_value = 5 ** i
    # Add the product of the value and place value to the decimal equivalent
    decimal += value * place_value
  
  # Return the decimal equivalent
  return decimal

def base5(num): 
    quotient = num/5  
    remainder = num%5
    if quotient == 0:  
        return ""
    else:
        return base5(int(quotient)) + str(int(remainder)) 


def i2s(ival):
    if ival == 0:
        return ''
    match ival % 5:
        case 0 | 1 | 2:
            return i2s(ival // 5) + str(ival % 5)
        case 3:
            return i2s( 1 + ival // 5) + '='
        case 4:
            return i2s( 1 + ival // 5) + '-'


data = open("input.txt").read().split("\n")

sum = 0
for line in data:
    sum += snafu_to_decimal(line)

snafu = base5(sum)
snafu2 = snafu.replace('3','-')
snafu3 = snafu2.replace('4', '=')
print(i2s(sum))

