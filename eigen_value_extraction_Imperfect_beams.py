# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Ladan Salari Sharif
# Date: February 2016
# Goal: Post-process the ABAQUS odb buckling simulation results
# Input: ABAQUS simulation results (.odb file) from the buckling simulation
# Output: Post-process the odb files and retrieve the eigenvalues to calculate the buckling load
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
print("ODB extraction")
from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *

load_number = 20

# This while loop will run through each odb writing the appropriate eigen value to a text file
Bar_numbers = 2000
for bar_number in range(1, Bar_numbers + 1):
    counter_2 = 1
    while counter_2 <= load_number:
        odb = openOdb(
            "L1100-D728_imper" + str(bar_number) + "_Load" + str(counter_2) + ".odb"
        )

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
                "L1100-D728_imper"
                + str(bar_number)
                + "_Load"
                + str(counter_2)
                + ","
                + str(File_eigenvalue)
                + "\n"
            )
            file_evalue = open("Eigen_Values.txt", "a")
            file_evalue.write(text_information)

            counter_2 += 1

        except:
            counter_2 += 1
