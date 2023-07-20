def get_scalar_product(given_matrix, n_rows, n_columns, number):
    for row in range(n_rows):
        for column in range(n_columns):
            given_matrix[row][column] = number * given_matrix[row][column]
    return given_matrix


try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = [[int(input(f"Enter element ({y}, {x}) to insert into the matrix: ")) for x in range(columns)]
              for y in range(rows)]
    num = int(input("Enter an integer to multiply with : "))
    print("The scalar product of the given matrix is:", get_scalar_product(matrix, rows, columns, num))
except ValueError:
    print("Invalid input. Please enter only integers.")