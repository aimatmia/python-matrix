from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4,100)

for t in range(100):
    r = random.randrange(1, 50)
    ra = random.randrange(1, 50)
    ran = random.randrange(1, 50)
    rand = random.randrange(1, 50)
    add_edge(matrix, (t*r+1)%500, (t*ra+5)%500, 0, \
             (t*ran+2)%500, (t*rand+6)%500, 0)

test = new_matrix(4, 4)
print "Testing identity, 4x4"
id = ident( test )
print_matrix(id)

print "Testing scalar mult. 9*identity"
scale = scalar_mult( id, 9 )
print_matrix(scale)

print "Testing add_edge. Adding edge (0,1,2,3), (2,3,4,5), \n \t\t (4,5,6,7), (6,7,0,1)"
mat = new_matrix(4, 4)
init_pt()
add_edge(mat, 0, 1, 0, 2, 3, 0)
add_edge(mat, 2, 3, 0, 4, 5, 0)
add_edge(mat, 4, 5, 0, 6, 7, 0)
add_edge(mat, 6, 7, 0, 0, 1, 0)
print_matrix(mat)

print "Testing matrix_mult. 9*identity*add_edges"
prod = matrix_mult(mat, scale)
print_matrix(prod)

draw_lines( matrix, screen, color )
display(screen)
