# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Ladan Salari Sharif
# Date: February 2016
# Goal: Create an input file for Abaqus for imperfect beams created using stochastic models with various load cases
# Input: The input file for stochastic beams
# output: The input file for Abaqus simulation for different load cases.
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
import math

number_bar = 2001  # number of bars
# ---------------------------------------------------------------------------------
# create the header for the input file
# ---------------------------------------------------------------------------------
for number_bars in range(1, number_bar):
    for load_index in range(1, 21):
        input_file_name = "L1100-D728_imper" + str(number_bars) + ".inp"
        input_file = open(input_file_name, "r")
        lines = input_file.readlines()
        output_file_name = (
            "L1100-D728_imper" + str(number_bars) + "_Load" + str(load_index) + ".inp"
        )
        output_file = open(output_file_name, "w")
        for i in range(0, 6494):
            output_file.write(lines[i])
        preload_x = (
            -5
            * math.cos(60 * math.pi / 180)
            * math.cos((load_index - 1) * 18 * math.pi / 180)
        )
        preload_y = (
            -5
            * math.cos(60 * math.pi / 180)
            * math.sin((load_index - 1) * 18 * math.pi / 180)
        )
        preload_z = -5 * math.sin(60 * math.pi / 180)
        output_file.write("MAXZ, 1, " + str(preload_x) + "\n")
        output_file.write("MAXZ, 2, " + str(preload_y) + "\n")
        output_file.write("MAXZ, 3, " + str(preload_z) + "\n")
        output_file.write(
            "**\n** OUTPUT REQUESTS\n**\n*Restart, write, frequency=0\n**\n** FIELD OUTPUT: F-Output-1\n"
        )
        output_file.write(
            "**\n*Output, field, variable=PRESELECT\n**\n** HISTORY OUTPUT: H-Output-1\n**\n*Output, history, variable=PRESELECT\n*End Step\n"
        )
        # ---------------------------------------------------------------------------------
        # write buckling Step
        # ---------------------------------------------------------------------------------
        output_file.write(
            "** ----------------------------------------------------------------\n"
        )
        output_file.write(
            "**\n** STEP: Buckling\n**\n*Step, name=Buckling, nlgeom=NO, perturbation\n"
        )
        output_file.write(
            "*Buckle\n10, , 18, 3000000\n**\n** BOUNDARY CONDITIONS\n**\n** Name: MAXZ Type: Displacement/Rotation\n"
        )
        output_file.write(
            "*Boundary, op=NEW, load case=1\nMAXZ, 4, 4\nMAXZ, 5, 5\nMAXZ, 6, 6\n"
        )
        output_file.write(
            "*Boundary, op=NEW, load case=2\nMAXZ, 4, 4\nMAXZ, 5, 5\nMAXZ, 6, 6\n"
        )
        output_file.write(
            "** Name: MINZ Type: Symmetry/Antisymmetry/Encastre\n*Boundary, op=NEW, load case=1\n"
        )
        output_file.write(
            "MINZ, ENCASTRE\n*Boundary, op=NEW, load case=2\nMINZ, ENCASTRE\n**\n"
        )
        output_file.write(
            "** LOADS\n**\n** Name: Load   Type: Concentrated force\n*Cload, op=NEW\n"
        )
        load_x = (
            -50
            * math.cos(60 * math.pi / 180)
            * math.cos((load_index - 1) * 18 * math.pi / 180)
        )
        load_y = (
            -50
            * math.cos(60 * math.pi / 180)
            * math.sin((load_index - 1) * 18 * math.pi / 180)
        )
        load_z = -50 * math.sin(60 * math.pi / 180)
        output_file.write("MAXZ, 1, " + str(load_x) + "\n")
        output_file.write("MAXZ, 2, " + str(load_y) + "\n")
        output_file.write("MAXZ, 3, " + str(load_z) + "\n")
        output_file.write("**\n** OUTPUT REQUESTS\n**\n*Restart, write, frequency=0\n")
        output_file.write(
            "**\n** FIELD OUTPUT: F-Output-2\n**\n*Output, field, variable=PRESELECT\n*End Step"
        )
