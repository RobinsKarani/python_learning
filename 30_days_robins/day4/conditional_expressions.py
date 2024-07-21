def process_score(score):
    try:
        # Validate that the score is a number
        score = float(score)

        # Check if the score is within the valid range
        if score < 0 or score > 100:
            raise ValueError('Score must be between 0 and 100.')

        # Determine the grade based on the score
        if score >= 60:
            grade = (
                "A" if score >= 90 else
                "B" if score >= 80 else
                "C" if score >= 70 else
                "D"
            )
            print(f"Score: {score} %, Grade: {grade}")
        else:
            print(f"Score: {score} %, Umeuma nje vibaya sana")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


try:
    # Get user input
    user_score = input('Enter the score (0-100): ')
    process_score(user_score)
except ValueError:
    print('Please enter a valid number for the score.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
