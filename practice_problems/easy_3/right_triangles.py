# Right Triangles

# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. 
# The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, 
# and the other end at the upper-right.

# Example 1
# triangle(5)
# Output for Example 1
#     *
#    **
#   ***
#  ****
# *****
# Example 2
# triangle(9)
# Output for Example 2
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

def triangle(n):
    spaces = n - 1
    stars = 1
    count = 0

    while count < n:
        print(' ' * spaces + '*' * stars)
        count+=1
        spaces-=1
        stars+=1


triangle(5)
triangle(9)