## Creates Dictionary using parameter function
## Outside function calls for letterGrade, checks map for translation from string
def letterGradeTranslation(letterGrade):
    gradeMap = {
        'A+': 4.30,
        'A': 4.00,
        'A-': 3.70,
        'B+': 3.30,
        'B': 3.00,
        'B-': 2.67,
        'C+': 2.33,
        'C': 2.00,
        'C-': 1.67,
        'D+': 1.33,
        'D': 1.00,
        'D-': 0.67,
        "F": 0.00
    }
    ## Takes the user input and switches to upper case, if not in gradeMap, 0.0 is returned
    return gradeMap.get(letterGrade.upper(), None)


## Organizes the entire GPA Calc function
def main():

    ## Creates an empty list for actual letter grades to be appended to
    listOfGrades = []

    ## Creates an empty list for GPA's to be appended to
    grades = []


    ## While loop used to repeat function until terminated
    while True:
        letterGrade = input('Enter a letter grade, once finished enter "Done": ') ## Allows user input grade to be a variable

        ## Termination using 'if' function
        if letterGrade.lower() == 'done': 
            print('Ending calculations of GPA.')
            break

        
        ## Converts parameter function into a variable to provide for GPA numbers 
        gpa = letterGradeTranslation(letterGrade)

        # Checks if gpa variable isn't a valid input, prints invalid if so, or continues function if not invalid
        if gpa is not None:

            # Adds letter grade's provided to the 'listOfGrades[]' <-- empty list
            listOfGrades.append(letterGrade)

            ## Adds gpa calculation variable to 'grades[]' <-- empty list
            grades.append(gpa)

            ## Creates variable for the total average gpa
            ## This is done by taking the sum of GPA's and dividing by total count of grades provided
            totalGpa = sum(grades) / len(grades)

            ## Using f-strings to combine regular text with variables '{}' used to list grades and calculate GPA's
            print(f'GPA of letter grade {letterGrade} entered: {gpa}')
            print(f'Your list of grades are:  {listOfGrades}')
            print(f'Total GPA calculated: {totalGpa:.2f}\n')
        else:
            invalidGrade = input(f"Invalid grade: {letterGrade}. Do you want to continue? (y/n) ").lower()
            if invalidGrade == 'y':
                print("Continuing GPA calculation...\n")
            elif invalidGrade == 'n':
                print('Ending calculations of GPA.')
                break

## Block to check if script is being run as main program, if yes, 'main()' function runs
## Good practice to control execution of code if script is imported into another script
if __name__ == '__main__':
    main()