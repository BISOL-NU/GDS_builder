# GDS_builder
Some functions for building GDS files and GDS arrays.

Hello, welcome to the GDS builder module. The code is fairly simple and easily customizable. It is useful for developing parameter sweeps for nanopillar arrays. The only dependencies are Numpy and GDSPY. On my home machine, I use a virtual environment with both of these modules installed. 

The 'getting started' page for GDSPY can be found here, and is invaluable for customizing the code to fit your purposes:
https://gdspy.readthedocs.io/en/stable/gettingstarted.html

GDS_builder Functions:

There are two options for adding alignment marks - we have:

<img width="335" alt="Screen Shot 2022-10-31 at 6 13 06 PM" src="https://user-images.githubusercontent.com/44413655/199126928-b8c17bab-9a4e-4fa0-b9e7-1743b3b39185.png">

and

<img width="572" alt="Screen Shot 2022-10-31 at 6 13 23 PM" src="https://user-images.githubusercontent.com/44413655/199126947-f539753c-9803-44c1-80d3-d5f764ec7093.png">

Generally, all GDS files should contain global alignment marks, which can be placed depending on intended chip size. The following code chunk will create alignment marks at the four corners of a 0.5x0.5cm chip:

<img width="494" alt="Screen Shot 2022-10-31 at 6 19 29 PM" src="https://user-images.githubusercontent.com/44413655/199127565-bc9dfb01-6545-4416-9c70-6514130fa015.png">

The output of this code is:

<img width="1194" alt="Screen Shot 2022-10-31 at 6 22 03 PM" src="https://user-images.githubusercontent.com/44413655/199127832-289b04e5-930d-4814-80f7-2f13a04344ea.png">

The EBL compatible alignment marks can be placed in the same way. 

The next step is to populate the GDS file with pillars/pillar arrays. The following code creates a single pillar at location ('px', 'py') with a diameter of 'dia'. When one inputs the 'label' keyword argument it will label the device in question. 

<img width="367" alt="Screen Shot 2022-10-31 at 6 08 12 PM" src="https://user-images.githubusercontent.com/44413655/199126416-c4d54c50-4bbc-48a6-bd55-f5c8ef331291.png">

If one chooses, one can specify a writefield size for the EBL tool at Northwestern to automatically generate alignment marks near the corners of the writefield. If a writefield specification is not desired, if, for example, one is using the MLA, leave the field blank or set 'writefield' = 0. The following outputs create 50um pillars which are generated with and without writefield specification:

<img width="519" alt="Screen Shot 2022-10-31 at 6 28 27 PM" src="https://user-images.githubusercontent.com/44413655/199128425-edb348b5-7514-4990-9bd8-abbe646cdeaf.png"><img width="521" alt="Screen Shot 2022-10-31 at 6 29 46 PM" src="https://user-images.githubusercontent.com/44413655/199128525-2c37f259-2b58-46ac-b01d-3e92626f59b6.png">

One can also make an array of pillars:

<img width="508" alt="Screen Shot 2022-10-31 at 6 43 13 PM" src="https://user-images.githubusercontent.com/44413655/199129705-f2505b87-b5da-4fff-afca-61464e874370.png">

This code generates 40um pillars spaced out with 1um in the x and y direction between pillars. The array is 8x8, and there are are alignment marks specified at 100um writefield:

<img width="667" alt="Screen Shot 2022-10-31 at 6 52 31 PM" src="https://user-images.githubusercontent.com/44413655/199130542-8f42ed3b-6d0e-4460-bd7b-4814911e2a24.png">

Output:

<img width="726" alt="Screen Shot 2022-10-31 at 6 53 01 PM" src="https://user-images.githubusercontent.com/44413655/199130579-0f8b7a1d-e986-450c-b2ba-4e5b9bebc30c.png">

Zoomed output on a 4x4 array:

<img width="1301" alt="Screen Shot 2022-10-31 at 6 53 25 PM" src="https://user-images.githubusercontent.com/44413655/199130619-bc3209bd-d1b2-482a-908d-85c80432c534.png">

Functions creating double, triple, and quadruple pillar patterns in array are shown below - it should be easy to extrapolate from this to build your own higher-order arrays:

<img width="614" alt="Screen Shot 2022-10-31 at 6 53 42 PM" src="https://user-images.githubusercontent.com/44413655/199130639-d11dfc62-5406-4ae0-8d7a-dd9e62d13890.png">



