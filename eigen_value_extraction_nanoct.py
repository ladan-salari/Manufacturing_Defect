# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Ladan Salari Sharif
# Date: March 2015
# Goal: Post-process the ABAQUS odb buckling simulation results
# Input: ABAQUS simulation results (.odb file) under buckling simulation
# Output: Post-process the odb files and return the eigenvalues to calculate the buckling load
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

print("ODB extraction")

from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *

bar_num = 1
load_num = 1
sec_num = 1
bar_indexes = [55, 43, 45, 30]

# max_load_number=20
# This while loop will run through each odb writing the appropriate eigen value to a text file
while sec_num <= 4:
    while bar_num <= bar_indexes[sec_num - 1]:
        while load_num <= 20:
            odb_directory = (
                "C:/Users/ladan/Documents/Research/Nano_CT_Bars_FEA/Sec%d-bar%d-mid-load%d.odb"
                % (sec_num, bar_num, load_num)
            )
            odb = openOdb(odb_directory)

            # This pulls out the first eigen value from the buckling step and assigns it the File_eigenvalue variable
            try:
                firstFrame = odb.steps["Buckling"].frames[1]
                Framedescription = firstFrame.description
                descriptionparts = Framedescription.partition("=")
                File_eigenvalue = float(descriptionparts[2])

                # Printing the Eigen Value to command window
                print(File_eigenvalue)
                odb.close()

                text_information = (
                    "\n Sec%d-bar%d-load%d      First Eigen Value=  %f"
                    % (i, bar_num, load_num, File_eigenvalue)
                )
                file = open("Eigen_Values.txt", "a")
                file.write(text_information)
                file.close()
                load_num += 1

            except:
                load_num += 1

        bar_num += 1
        load_num = 1
    sec_num += 1
