# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Ladan Salari Sharif
# Date: March 2015
# Goal: Create an input file for Abaqus for a perfect circular cross-section cylinder
# Input: Beam length data from CT scan data
# Output: The input file for Abaqus simulation for all combinations of beam length and diameter
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
import os
os.chdir("C:\Users\ladan\Documents\Research")
Mdb()
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from interaction import *
from part import *
from mesh import *

import decimal

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

#--------------------------------------------------------------
# MODEL PARAMETERS
#--------------------------------------------------------------

num_nodes=160
scale=1.0
input_length_dia=open("Summary_length_and_diam.csv","r")
lines = input_length_dia.readlines()
bar_indexes=[55,43,45,30]
num = 0
for sec_index in range (4):
    for bar_index in range(1,bar_indexes[sec_index]):
        split_line=lines[num].split(',')
        length=decimal.Decimal(split_line[1])
        diameter=decimal.Decimal(split_line[-1])
        
        R= float(diameter)/2000 #mm radius
        L= float(length) #mm length
        print(L)
        print(R)

#--------------------------------------------------------------
# SKETCH PART
#--------------------------------------------------------------
        session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
        session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
            meshTechnique=OFF)
        session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
            referenceRepresentation=ON)
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.sketchOptions.setValues(decimalPlaces=3)
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, R))
        p = mdb.models['Model-1'].Part(name='Cylinder', dimensionality=THREE_D, 
            type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Cylinder']
        p.BaseShellExtrude(sketch=s, depth=L)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Cylinder']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']


        #--------------------------------------------------------------
        # MESH
        #--------------------------------------------------------------
        #Seed by edges
        p = mdb.models['Model-1'].parts['Cylinder']
        e = p.edges
        pickedEdges = e.findAt(((R, 0, 0), ))
        p.seedEdgeByNumber(edges=pickedEdges, number=num_nodes, constraint=FINER)

        p = mdb.models['Model-1'].parts['Cylinder']
        e = p.edges
        pickedEdges = e.findAt(((R, 0, L), ))
        p.seedEdgeByNumber(edges=pickedEdges, number=num_nodes, constraint=FINER)

        #Define element type
        elemType1 = mesh.ElemType(elemCode=S4R, elemLibrary=STANDARD)
        elemType2 = mesh.ElemType(elemCode=STRI65, elemLibrary=STANDARD)
        p = mdb.models['Model-1'].parts['Cylinder']
        f = p.faces
        faces = f.findAt(((R, 0, L/2), ))
        pickedRegions =(faces, )
        p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
        p = mdb.models['Model-1'].parts['Cylinder']
        p.generateMesh()

        #--------------------------------------------------------------
        # ASSEMBLY
        #--------------------------------------------------------------
        a = mdb.models['Model-1'].rootAssembly
        session.viewports['Viewport: 1'].setValues(displayedObject=a)
        session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
        session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
            meshTechnique=OFF)
        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['Cylinder']
        a.Instance(name='Cylinder-1', part=p, dependent=ON)
        a = mdb.models['Model-1'].rootAssembly





        job_name="Sec"+str(sec_index+1)+"-bar"+str(bar_index)+"-mid-PD"
        
        print(job_name)
        mdb.Job(name= job_name, model='Model-1', description='', type=ANALYSIS, 
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
            scratch='', multiprocessingMode=DEFAULT, numCpus=4, numDomains=4)
        mdb.jobs[job_name].writeInput(consistencyChecking=OFF)
        mdb.jobs[job_name].waitForCompletion()
        num =num+1
            
