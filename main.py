import GDS_Builder as GD
import gdspy

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('Alignment_Calibration_new')

#create your GDS file
GD.alignmentmark(-5000, -5000)
GD.alignmentmark(5000, -5000)
GD.alignmentmark(-5000, 5000)
GD.alignmentmark(5000, 5000)

GD.pillar_array(0,500,1000,1000,8,8,40,writefield = 100)
GD.pillar_array(500,500,1000,1000,8,8,10,writefield = 100)
GD.pillar_array(1000,500,1000,1000,8,8,5,writefield = 100)
GD.pillar_array(1500,500,1000,1000,8,8,3,writefield = 100)

GD.pillar_array(0,0,1000,1000,8,8,1,writefield = 100)
GD.pillar_array(500,0,1000,1000,8,8,0.5,writefield = 100)
GD.pillar_array(1000,0,1000,1000,8,8,0.3,writefield = 100)
GD.pillar_array(1500,0,1000,1000,8,8,0.2,writefield = 100)

GD.triple_injector_array(0,-500,1000,1000,8,8,3,12,writefield = 100)
GD.triple_injector_array(500,-500,1000,1000,8,8,1,8,writefield = 100)
GD.triple_injector_array(1000,-500,1000,1000,8,8,0.5,4,writefield = 100)
GD.triple_injector_array(1500,-500,1000,1000,8,8,0.3,2,writefield = 100)

GD.quad_injector_array(0,-1000,1000,1000,8,8,3,12,writefield = 100)
GD.quad_injector_array(500,-1000,1000,1000,8,8,1,8,writefield = 100)
GD.quad_injector_array(1000,-1000,1000,1000,8,8,0.5,4,writefield = 100)
GD.quad_injector_array(1500,-1000,1000,1000,8,8,0.3,2,writefield = 100)

# Save the library in a file called 'first.gds'.
gdspy.lib.write_gds('Alignment_Calibration_new.gds')
