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

def EBL_alignmentmark(px, py):
    box1 = gdspy.Rectangle((-0.5 + px,2 + py), (0.5 + px,5 + py))
    box2 = gdspy.Rectangle((-0.5 + px,-2 + py),(0.5 + px,-5 + py))
    box3 = gdspy.Rectangle((-5 + px,0.5 + py),(-2 + px,-0.5 + py))
    box4 = gdspy.Rectangle((5 + px, 0.5 + py), (2 + px, -0.5 + py))
    b1 = gdspy.Rectangle((-2 + px,0.05 + py),(2 + px,-0.05 + py))
    b2 = gdspy.Rectangle((0.05 + px,-2 + py),(-0.05 + px,2 + py))
    cross1 = gdspy.boolean(box1, box2, "or")
    cross2 = gdspy.boolean(box3, box4, "or")
    cross3 = gdspy.boolean(b1, b2, "or")
    cross = gdspy.boolean(cross1, cross2, "or")
    cross = gdspy.boolean(cross, cross3, "or")
    cell.add(cross)

#creates a single pillar at px, py with a diameter of dia
def one_pillar(px, py, dia, label = None, writefield = 100):
    pillar = gdspy.Round((px, py), dia/2, tolerance=0.001)
    label = gdspy.Text(label, 4, (px - 15, py - dia -20))
    if not writefield == None:
        wp = 10 #writefield padding
        EBL_alignmentmark(px + -writefield/2 + wp,py + -writefield/2 + wp)
        EBL_alignmentmark(px + -writefield / 2 + wp,py +  writefield / 2 - wp)
        EBL_alignmentmark(px + writefield / 2 - wp,py +  writefield / 2 - wp)
        EBL_alignmentmark(px + writefield / 2 - wp,py +  -writefield / 2 + wp)
    cell.add(label)
    cell.add(pillar)


#creates an m by n array of pillars centered at px, py with step sizes of sx, sy
def pillar_array(px, py, sx, sy, m, n, dia, label_var = None, writefield = None):
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
            one_pillar(px/2 + j * sx, py/2 + i * sy, dia, label, writefield = writefield)
            j = j + 1

def double_injector_array(px, py, sx, sy, m, n, dia, pilsep, writefield):
    pillar_array(px - pilsep/2, py, sx, sy, m, n, dia, writefield=writefield)
    pillar_array(px + pilsep/2, py, sx, sy, m, n, dia, "NoLabel", writefield=None)

def triple_injector_array(px, py, sx, sy, m, n, dia, pilsep, writefield):
    pillar_array(px - pilsep/2, py, sx, sy, m, n, dia, writefield=writefield)
    pillar_array(px + pilsep/2, py, sx, sy, m, n, dia, "NoLabel", writefield=None)
    pillar_array(px, py + pilsep*np.sqrt(3)/2, sx, sy, m, n, dia, "NoLabel", writefield=None)

def quad_injector_array(px, py, sx, sy, m, n, dia, pilsep, writefield):
    pillar_array(px - pilsep/2, py + pilsep/2, sx, sy, m, n, dia, writefield=writefield)
    pillar_array(px + pilsep/2, py - pilsep/2, sx, sy, m, n, dia, "NoLabel", writefield=None)
    pillar_array(px - pilsep/2, py - pilsep/2, sx, sy, m, n, dia, "NoLabel", writefield=None)
    pillar_array(px + pilsep/2, py + pilsep/2, sx, sy, m, n, dia, "NoLabel", writefield=None)





