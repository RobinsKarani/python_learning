# Practice Question: Temperature Converter

Create a Python program that acts as a temperature converter. The program should be able to convert temperatures between Celsius, Fahrenheit, and Kelvin. The user should be able to input a temperature value and specify the input and output units. The program should then display the converted temperature.

## Requirements:
1. The program should prompt the user to enter a temperature value.
2. The program should prompt the user to enter the input unit (Celsius, Fahrenheit, Kelvin).
3. The program should prompt the user to enter the desired output unit (Celsius, Fahrenheit, Kelvin).
4. The program should convert the temperature to the desired output unit.
5. The program should handle invalid inputs gracefully and provide meaningful error messages.

## Example:
Enter temperature value: 100
Enter input unit (C/F/K): C
Enter output unit (C/F/K): F
The converted temperature is 212.0 F


## Conversion Formulas:
- Celsius to Fahrenheit: \( F = C \times \frac{9}{5} + 32 \)
- Fahrenheit to Celsius: \( C = (F - 32) \times \frac{5}{9} \)
- Celsius to Kelvin: \( K = C + 273.15 \)
- Kelvin to Celsius: \( C = K - 273.15 \)
- Fahrenheit to Kelvin: \( K = (F - 32) \times \frac{5}{9} + 273.15 \)
- Kelvin to Fahrenheit: \( F = (K - 273.15) \times \frac{9}{5} + 32 \)
