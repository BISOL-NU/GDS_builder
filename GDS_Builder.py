import numpy as np
import gdspy

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('Alignment_Calibration_new')
cell = lib.new_cell('Pattern')

#creates an alignment mark at the specified location
def alignmentmark(px, py):
    points1 = [(-50 + px, -5 + py), (-50 + px, 5 + py), (50 + px, 5 + py), (50 + px, -5 + py)]
    points2 = [(-5 + px, -50 + py), (-5 + px, 50 + py), (5 + px, 50 + py), (5 + px, -50 + py)]
    box1 = gdspy.Polygon(points1)
    box2 = gdspy.Polygon(points2)
    cross = gdspy.boolean(box1, box2, "or")
    cell.add(cross)

#creates a single pillar at px, py with a diameter of dia
def one_pillar(px, py, dia, label = None):
    pillar = gdspy.Round((px, py), dia/2, tolerance=0.001)
    label = gdspy.Text(label, 4, (px - 15, py - dia -20))
    cell.add(label)
    cell.add(pillar)

#creates an m by n array of pillars centered at px, py with step sizes of sx, sy
def pillar_array(px, py, sx, sy, m, n, dia, label_var = None):
    px = px - (sx * m)
    py = py - (sy * n)
    i = -1
    while i < m:
        j = 0
        i = i + 1
        while j <= n:
            label = str(i) + "," + str(j) + "," + str(dia) + "um"
            if label_var == "NoLabel":
                label = ""
            one_pillar(px/2 + j * sx, py/2 + i * sy, dia, label)
            j = j + 1

def double_injector_array(px, py, sx, sy, m, n, dia, pilsep):
    pillar_array(px - pilsep/2, py, sx, sy, m, n, dia)
    pillar_array(px + pilsep/2, py, sx, sy, m, n, dia, "NoLabel")

def triple_injector_array(px, py, sx, sy, m, n, dia, pilsep):
    pillar_array(px - pilsep/2, py, sx, sy, m, n, dia)
    pillar_array(px + pilsep/2, py, sx, sy, m, n, dia, "NoLabel")
    pillar_array(px, py + pilsep*np.sqrt(3)/2, sx, sy, m, n, dia, "NoLabel")

def quad_injector_array(px, py, sx, sy, m, n, dia, pilsep):
    pillar_array(px - pilsep/2, py + pilsep/2, sx, sy, m, n, dia)
    pillar_array(px + pilsep/2, py - pilsep/2, sx, sy, m, n, dia, "NoLabel")
    pillar_array(px - pilsep/2, py - pilsep/2, sx, sy, m, n, dia, "NoLabel")
    pillar_array(px + pilsep/2, py + pilsep/2, sx, sy, m, n, dia, "NoLabel")

#create your GDS file
alignmentmark(-5000, -5000)
alignmentmark(5000, -5000)
alignmentmark(-5000, 5000)
alignmentmark(5000, 5000)

pillar_array(0,500,1000,1000,8,8,40)
pillar_array(500,500,1000,1000,8,8,10)
pillar_array(1000,500,1000,1000,8,8,5)
pillar_array(1500,500,1000,1000,8,8,3)

pillar_array(0,0,1000,1000,8,8,1)
pillar_array(500,0,1000,1000,8,8,0.5)
pillar_array(1000,0,1000,1000,8,8,0.3)
pillar_array(1500,0,1000,1000,8,8,0.2)

triple_injector_array(0,-500,1000,1000,8,8,3,12)
triple_injector_array(500,-500,1000,1000,8,8,1,8)
triple_injector_array(1000,-500,1000,1000,8,8,0.5,4)
triple_injector_array(1500,-500,1000,1000,8,8,0.3,2)

quad_injector_array(0,-1000,1000,1000,8,8,3,12)
quad_injector_array(500,-1000,1000,1000,8,8,1,8)
quad_injector_array(1000,-1000,1000,1000,8,8,0.5,4)
quad_injector_array(1500,-1000,1000,1000,8,8,0.3,2)

# Save the library in a file called 'first.gds'.
lib.write_gds('Alignment_Calibration_new.gds')
print('meow')



