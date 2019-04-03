import maya.cmds as cmds
import math

######################################### Define Functions ##################################################

def AnimationSpeed (pPlayBackTime, pAnimationTime):
    
    cmds.playbackOptions( loop='continuous' )
    cmds.playbackOptions( minTime=1, maxTime= pPlayBackTime, ast= 1, aet= pAnimationTime )


def keyMovement( pObjectName, pStartTime, pEndTime, pTargetAttribute, pRotateAngle1, pRotateAngle2 ):
    
    cmds.cutKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute )
    
    cmds.setKeyframe( pObjectName, time= pStartTime, attribute=pTargetAttribute, value=pRotateAngle1 )
    cmds.setKeyframe( pObjectName, time= pEndTime, attribute=pTargetAttribute, value=pRotateAngle2 )

    cmds.selectKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True )
    
    cmds.keyTangent( inTangentType='fast', outTangentType='slow' )


def random (pNumberOfButterfly, pMinRangeX, pMaxRangeX, pMaxRangeY, pMaxRangeZ, pMinRangeZ):
    
    import random

    random.seed( 8428 )
    Butterfly = cmds.ls( orderedSelection=True )
    transformName = Butterfly[0]
    
    instanceGroupName = cmds.group( empty=True, name=transformName + '_instance_grp#' )
    MinRangeY = 5
    
    for i in range( 0, pNumberOfButterfly ):
        
        instanceResult = cmds.instance( transformName, name=transformName + '_instance#' )
        
        cmds.parent( instanceResult, instanceGroupName )
        
        #print 'instanceResult: ' + str( instanceResult )
        
        x = random.uniform( pMinRangeX, pMaxRangeX )
        y = random.uniform( MinRangeY, pMaxRangeY )
        z = random.uniform( pMinRangeZ, pMaxRangeZ )
        
        cmds.move( x, y, z, instanceResult )
        
        xRot = random.uniform( -50, 50 )
        yRot = random.uniform( 0, 360 )
        zRot = random.uniform( -50, 50 )
        
        cmds.rotate( xRot, yRot, zRot, instanceResult )
        
        scalingFactor = random.uniform( 0.01,0.15 )
        
        cmds.scale( scalingFactor, scalingFactor, scalingFactor, instanceResult )
        

        cmds.xform( instanceGroupName, centerPivots=True )
    
    
    
    cmds.hide( transformName )
    cmds.xform( instanceGroupName, centerPivots=True )
    
    
            
############################################# Create UI ##################################################

def createUI(pCreateCallback):
    
    
    #check to see if our window exists
    
    windowID = 'ButterflyGenerator'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    
    #create our window 
    
    Mywindow = cmds.window( windowID, title='BUTTERFLY GENERATOR', resizeToFitChildren=True, sizeable=False)
    
    #creat a main layout

    
    mainlayout = cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[ (1,160), (2,300), (3,10) ], columnOffset=[ (1,'right',3) ] )
    
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
   

######################### GROUP OPTION #######################################
    
    cmds.text( label='  CREATE SERIES OF BUTTERFLY', w = 160)
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    
    cmds.text( label='  Number of Butterflies:', w = 160)
    NumberOfButterflyField = cmds.intSliderGrp(minValue= 1, maxValue= 1000, value= 50, step= 1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=2, style='none' )
    cmds.separator( h=2, style='none' )
    cmds.separator( h=2, style='none' )
    
    cmds.text(w = 160, label='Colour:')
    ColourField = cmds.colorSliderGrp ( rgb = (20, 1, 0.14))
    cmds.separator( h=10, style='none' )
        
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    
    cmds.text( label='Area size: ', w = 160)
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    
    cmds.text( label='Height: ', w = 160)
    MaxRangeYField = cmds.intSliderGrp(minValue= 6, maxValue= 100, value= 25, step= 1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=5, style='none' )
    cmds.separator( h=5, style='none' )
    cmds.separator( h=5, style='none' )
    
    cmds.text( label='Translate X: ', w = 160)
    MinRangeXField = cmds.intSliderGrp(minValue= -100, maxValue= -1, value= -10, step= 1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=2, style='none' )
    cmds.text( label='                     to ', w = 160)
    cmds.separator( h=2, style='none' )
    
    cmds.separator( h=10, style='none')
    MaxRangeXField = cmds.intSliderGrp(minValue= 1, maxValue= 100, value= 10, step=1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=5, style='none' )
    cmds.separator( h=5, style='none' )
    cmds.separator( h=5, style='none' ) 
    
    cmds.text( label='Translate Z: ', w = 160)
    MinRangeZField = cmds.intSliderGrp(minValue= -100, maxValue= -1, value= -10, step= 1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=2, style='none' )
    cmds.text( label='                     to ', w = 160)
    cmds.separator( h=2, style='none' )
    
    cmds.separator( h=10, style='none')
    MaxRangeZField = cmds.intSliderGrp(minValue= 1, maxValue= 100, value= 10, step=1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' ) 
    
######################### ANIMATION OPTION #######################################    
    
    cmds.text( label='ANIMATION ', w = 160)
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    
    cmds.text( label='Speed(Wave/frame):', w = 160)
    PlayBackTimeField = cmds.intSliderGrp(minValue=5, maxValue=80, value=8, step=1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.text( label='Animation Length:', w = 160)
    AnimationTimeField = cmds.intSliderGrp(minValue=1, maxValue=800, value=80, step=1, field = True )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
        
######################### CREATE OPTION #######################################

    cmds.separator( h=10, style='none' )
    cmds.button(label = "Create", w = 160, command = lambda *args: 
    CreateCallback(cmds.intSliderGrp(NumberOfButterflyField, query=True, value=True), 
    cmds.intSliderGrp(MinRangeXField, query=True, value=True), 
    cmds.intSliderGrp(MaxRangeXField, query=True, value=True),
    cmds.intSliderGrp(MaxRangeYField, query=True, value=True),
    cmds.intSliderGrp(MinRangeZField, query=True, value=True),
    cmds.intSliderGrp(MaxRangeZField, query=True, value=True),
    cmds.intSliderGrp(AnimationTimeField, query=True, value=True),
    cmds.intSliderGrp(PlayBackTimeField, query=True, value=True),
    cmds.colorSliderGrp ( ColourField, query = True, rgbValue = True))  )
    
    
    cmds.separator( h=10, style='none')
    
    
    def cancelProc(*pArgs):
        
        print "action is cancelled"
        cmds.deleteUI("ButterflyGenerator")
    
    cmds.separator( h=10, style='none' )
    cmds.button(label = "Cancle", w = 160,command = cancelProc)
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
    cmds.separator( h=15, style='none' )
     
    
    #show window
    cmds.showWindow (Mywindow)


    

######################################### Define Call Back ##################################################
    

def CreateCallback(NumberOfButterfly, MinRangeX, MaxRangeX, MaxRangeY, MinRangeZ, MaxRangeZ, 
AnimationTime, PlayBackTime, rgb, *pArgs ):
    
    print "Start Create"
    cmds.deleteUI("ButterflyGenerator")
        
    ######################################### Create Body ##################################################
    
    Butterfly_Body = cmds.polyCube( sx=15, sy=2, sz=2, w=10, h=1, n = 'Butterfly_Body')
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[15])
    cmds. scale ( 1,1,1.25)
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[154] )
    cmds.polyMoveEdge( sx = 0.5, sy = 0.5, sz = 0.5, lty = 3.5)
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[120,136,152,168,184,200,216,232] )
    cmds.polyMoveEdge( sx = 0.5, sy = 0.5, sz = 0.5 )
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[160] )
    cmds.polyMoveEdge( sx = 0.5, sy = 0.5, sz = 0.5, lty = -0.5)
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[161,162,163,164,165,166,167,183,199,151,135,247,231,215] )
    cmds.polyMoveEdge( sx = 0.5, sy = 0.5, sz = 0.5 )
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[157] )
    cmds.polyMoveEdge( sx = 1.5, sy = 1.5, sz = 1.5 )
    
    cmds.polySelect( 'Butterfly_Body', edgeLoop=[156,158] )
    cmds.polyMoveEdge( sx = 1.5, sy = 1.2, sz = 1.2 )
    cmds.select (clear = True)
    
    cmds. move(1.5, 0, 0,Butterfly_Body, os= True)
    cmds.makeIdentity(Butterfly_Body, apply=True, t=1)
    
    ######################################### Create Antennae ##################################################
    
    Butterfly_L_Antennae = cmds.polyCube( sx=1, sy=10, sz=1, w=0.05, h=3, d=0.05, n = 'Butterfly_L_Antennae')
    cmds.move(-4.5, 0.8, -0.6, Butterfly_L_Antennae, os = True)
    cmds.rotate(-16, 0, 70, Butterfly_L_Antennae, os = True)
    cmds.polySelect( 'Butterfly_L_Antennae', edgeLoop=[9] )
    cmds.polyMoveEdge( sx = 2, sy = 2, sz = 2 )
    
    Butterfly_R_Antennae = cmds.polyCube( sx=1, sy=10, sz=1, w=0.05, h=3, d=0.05, n = 'Butterfly_R_Antennae')
    cmds.move(-4.5, 0.8, 0.6, Butterfly_R_Antennae, os = True)
    cmds.rotate(16, 0, 70, Butterfly_R_Antennae, os = True)
    cmds.polySelect( 'Butterfly_R_Antennae', edgeLoop=[9] )
    cmds.polyMoveEdge( sx = 2, sy = 2, sz = 2 )
    
    Butterfly_Antennaes = cmds.polyUnite( Butterfly_R_Antennae,Butterfly_L_Antennae, n='Butterfly_Antennaes' )
    
    ######################################### Create Eyes ##################################################
    
    Butterfly_L_Eye = cmds. polySphere(r = 0.25,sx=6,sy=6, n= 'Butterfly_L_Eye')
    cmds.move(-3, 0, -0.5, Butterfly_L_Eye, os = True)
    
    Butterfly_R_Eye = cmds. polySphere(r = 0.25,sx=6,sy=6, n= 'Butterfly_R_Eye')
    cmds.move(-3, 0, 0.5, Butterfly_R_Eye, os = True)
    
    Butterfly_Eyes = cmds.polyUnite( Butterfly_L_Eye,Butterfly_R_Eye, n='Butterfly_Eyes' )
    
    ######################################### Group All ##################################################
    
    Butterfly_Main = cmds.polyUnite( Butterfly_Body,Butterfly_Antennaes, Butterfly_Eyes, n='Butterfly_Main' )
    
    ######################################### Create Wings ##################################################
    
    Butterfly_wing_Original = cmds. polyPlane( w = 15, h = 15, sx = 2, sy = 2, n = 'Butterfly_wing_Original')
    
    cmds.polyMoveVertex( 'Butterfly_wing_Original.vtx[8]', tx= -2, tz = 2)
    cmds.polyMoveVertex( 'Butterfly_wing_Original.vtx[2]', tx= -2, tz = -2)
    cmds.polyMoveVertex( 'Butterfly_wing_Original.vtx[6]', tx= 2, tz = 2)
    
    Butterfly_L_Forewing = cmds.duplicate( 'Butterfly_wing_Original', n = 'Butterfly_L_Forewing')
    cmds.move(  -4, 0, -10, Butterfly_L_Forewing, os = True)
    cmds.rotate( 0, 65, 0, Butterfly_L_Forewing, os = True)
    cmds.makeIdentity( Butterfly_L_Forewing,apply=True, t=1, r=1, s=1, n=0)
    
    Butterfly_L_Hindwing = cmds.duplicate( 'Butterfly_L_Forewing', n = 'Butterfly_L_Hindwing')
    
    cmds.scale( 0.7, 0.7, 0.7, Butterfly_L_Hindwing)
    cmds.rotate( 0, -50, 0, Butterfly_L_Hindwing, os = True)
    cmds.makeIdentity( Butterfly_L_Hindwing,apply=True, t=1, r=1, s=1, n=0)
    cmds.move(7.5, 0, 3.5, Butterfly_L_Hindwing, os = True)
    cmds.makeIdentity( Butterfly_L_Hindwing,apply=True, t=1, r=1, s=1, n=0)
    
    Butterfly_R_Forewing = cmds.duplicate( 'Butterfly_wing_Original', n = 'Butterfly_R_Forewing')
    
    cmds.rotate( 180, -65, 0, Butterfly_R_Forewing, os = True)
    cmds.makeIdentity( Butterfly_R_Forewing,apply=True, t=1, r=1, s=1, n=0)
    cmds.move(  -4, 0, 10, Butterfly_R_Forewing, os = True)
    cmds.makeIdentity( Butterfly_R_Forewing,apply=True, t=1, r=1, s=1, n=0)
    
    Butterfly_R_Hindwing = cmds.duplicate( 'Butterfly_R_Forewing', n = 'Butterfly_R_Hindwing')
    
    cmds.scale( 0.7, 0.7, 0.7, Butterfly_R_Hindwing)
    cmds.rotate( 0, 50, 0, Butterfly_R_Hindwing, os = True)
    cmds.makeIdentity( Butterfly_R_Hindwing,apply=True, t=1, r=1, s=1, n=0)
    cmds.move(7.5, 0, -3.5, Butterfly_R_Hindwing, os = True)
    cmds.makeIdentity( Butterfly_R_Hindwing,apply=True, t=1, r=1, s=1, n=0)
    
    cmds.select( Butterfly_wing_Original)
    cmds.delete()
    
    ########################### Move Pivot points to the center ##################################################
    
    cmds.move(0, 0, 0, Butterfly_L_Forewing[0]+".scalePivot",Butterfly_L_Forewing[0]+".rotatePivot", absolute=True)
    cmds.move(0, 0, 0, Butterfly_R_Forewing[0]+".scalePivot",Butterfly_R_Forewing[0]+".rotatePivot", absolute=True)
    cmds.move(0, 0, 0, Butterfly_L_Hindwing[0]+".scalePivot",Butterfly_L_Hindwing[0]+".rotatePivot", absolute=True)
    cmds.move(0, 0, 0, Butterfly_R_Hindwing[0]+".scalePivot",Butterfly_R_Hindwing[0]+".rotatePivot", absolute=True)
    
    Butterfly_L_Wings = cmds.group(Butterfly_L_Forewing, Butterfly_L_Hindwing, n = 'Butterfly_L_Wings')
    Butterfly_R_Wings = cmds.group(Butterfly_R_Forewing, Butterfly_R_Hindwing, n = 'Butterfly_R_Wings')
    
    Butterfly_Wings = cmds.group( Butterfly_L_Wings,Butterfly_R_Wings,n= 'Butterfly_Wings' )
    
    ######################################### Create Butterfly ##################################################
    
    Butterfly = cmds.group( Butterfly_Main, Butterfly_Wings)
    cmds.makeIdentity( Butterfly,apply=True, t=1, r=1, s=1, n=0)
    
    ######################################### Start Animation ##################################################
    
    AnimationSpeed (PlayBackTime,AnimationTime)
    
    StartTime = 1
    EndTime = PlayBackTime
    
    random (NumberOfButterfly, MinRangeX, MaxRangeX, MaxRangeY, MaxRangeZ, MinRangeZ)
    
    ######################################### Add Colour ##################################################
    
    cmds.shadingNode( 'lambert', asShader=True )
    cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='lambert1SG' )
    cmds.setAttr ( 'lambert1.color', rgb[0], rgb[1], rgb[2], type = 'double3')
    cmds.connectAttr( 'lambert1.outColor', 'lambert1SG.surfaceShader', f=True )
    cmds.sets(Butterfly_Main[0],edit=True, forceElement='lambert1SG')
    

    
    

    
    
    for i in range(0, AnimationTime, PlayBackTime):
        
        keyMovement( Butterfly_Main, StartTime, EndTime, 'translateY',0.8,-0.8)
        keyMovement( Butterfly_L_Forewing[0], StartTime, EndTime, 'rotateX',70,-70 )
        keyMovement( Butterfly_R_Forewing[0], StartTime, EndTime, 'rotateX',-70,70 )
        keyMovement( Butterfly_L_Hindwing[0], StartTime, EndTime, 'rotateX',65,-65 )
        keyMovement( Butterfly_R_Hindwing[0], StartTime, EndTime, 'rotateX',-65, 65 )
        
        StartTime = StartTime + PlayBackTime
        EndTime = EndTime + PlayBackTime
     

     
     

######################################### Start Animation ##################################################

cmds.select(all=True)
cmds.delete()

createUI( CreateCallback )




####################################################################
