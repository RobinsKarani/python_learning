def temperature_converter(value, input_unit, output_unit):
    try:
        input_unit = input_unit.upper()
        output_unit = output_unit.upper()

        # Check for valid units
        valid_units = ['C', 'K', 'F']
        if input_unit not in valid_units or output_unit not in valid_units:
            raise ValueError('Invalid unit provided. Please use C, K, or F.')

        # Check if input and output units are the same
        if input_unit == output_unit:
            print(f'The converted temperature value is: {value} {output_unit}')
            return

        # Conversion logic
        if input_unit == 'C' and output_unit == 'K':
            output_value = value + 273.15
        elif input_unit == 'K' and output_unit == 'C':
            output_value = value - 273.15
        elif input_unit == 'K' and output_unit == 'F':
            celsius = value - 273.15
            output_value = celsius * 9 / 5 + 32
        elif input_unit == 'F' and output_unit == 'K':
            celsius = (value - 32) * 5 / 9
            output_value = celsius + 273.15
        elif input_unit == 'F' and output_unit == 'C':
            output_value = (value - 32) * 5 / 9
        elif input_unit == 'C' and output_unit == 'F':
            output_value = (value * 9 / 5) + 32

        print(f'The converted temperature value is: {output_value} {output_unit}')

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


try:
    temperature_converter(
        value=float(input('Enter the temperature value: ')),
        input_unit=input('Enter the input unit (F/K/C): '),
        output_unit=input('Enter the output unit (F/K/C): '),
    )
except ValueError:
    print('Please enter a valid number for the temperature value.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
