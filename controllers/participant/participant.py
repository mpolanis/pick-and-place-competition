"""Sample Webots controller for the pick and place benchmark."""

from controller import Robot

# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Initialize base motors.
wheels = []
wheels.append(robot.getDevice("wheel1"))
wheels.append(robot.getDevice("wheel2"))
wheels.append(robot.getDevice("wheel3"))
wheels.append(robot.getDevice("wheel4"))
for wheel in wheels:
    # Activate controlling the motors setting the velocity.
    # Otherwise by default the motor expects to be controlled in force or position,
    # and setVelocity will set the maximum motor velocity instead of the target velocity.
    wheel.setPosition(float('+inf'))

# Initialize arm motors.
armMotors = []
armMotors.append(robot.getDevice("arm1"))
armMotors.append(robot.getDevice("arm2"))
armMotors.append(robot.getDevice("arm3"))
armMotors.append(robot.getDevice("arm4"))
armMotors.append(robot.getDevice("arm5"))
# Set the maximum motor velocity.
armMotors[0].setVelocity(1.5708)
armMotors[1].setVelocity(1.5708)
armMotors[2].setVelocity(1.5708)
armMotors[3].setVelocity(1.5708)

# Initialize arm position sensors.
# These sensors can be used to get the current joint position and monitor the joint movements.
armPositionSensors = []
armPositionSensors.append(robot.getDevice("arm1sensor"))
armPositionSensors.append(robot.getDevice("arm2sensor"))
armPositionSensors.append(robot.getDevice("arm3sensor"))
armPositionSensors.append(robot.getDevice("arm4sensor"))
armPositionSensors.append(robot.getDevice("arm5sensor"))
for sensor in armPositionSensors:
    sensor.enable(timestep)

# Initialize gripper motors.
finger1 = robot.getDevice("finger1")
finger2 = robot.getDevice("finger2")
# Set the maximum motor velocity.
finger1.setVelocity(10) #max
finger2.setVelocity(10)
# Read the minium and maximum position of the gripper motors.
fingerMinPosition = finger1.getMinPosition()
fingerMaxPosition = finger1.getMaxPosition()

# Move forward.
for wheel in wheels:
    wheel.setVelocity(14.79) #max - 0.02 because we reach to the belt before it stops with 14.81

# Move arm and open gripper. #do this action will going to belt
armMotors[1].setPosition(-1.13446) #max
armMotors[2].setPosition(-0.7)
armMotors[3].setPosition(-0.03)
finger1.setPosition(fingerMaxPosition)
finger2.setPosition(fingerMaxPosition)

# Wait until the robot is in front of the box.
robot.step(237 * timestep)

# Stop moving forward. #no need to stop
#for wheel in wheels:
    #wheel.setVelocity(0.0)

# Monitor the arm joint position to detect when the motion is completed. #this stopped the sim
#while robot.step(timestep) != -1:
    #if abs(armPositionSensors[3].getValue() - (-1.2)) < 0.01:
        # Motion completed.
        #break

# Close gripper.
finger1.setPosition(0.013)
finger2.setPosition(0.013)
# Wait until the gripper is closed.
robot.step(30 * timestep)

# Lift arm. #no need to lift
#armMotors[1].setPosition(0)
# Wait until the arm is lifted.
#robot.step(200 * timestep)

# Rotate the robot.
#wheels[0].setVelocity(12.5)
#wheels[1].setVelocity(-12.5)
#wheels[2].setVelocity(2.5)
#wheels[3].setVelocity(-2.5)
# Wait for a fixed amount to step that the robot rotates.
#robot.step(690 * timestep)

# Move forward.
#wheels[1].setVelocity(2.5)
#wheels[3].setVelocity(2.5)
#robot.step(900 * timestep)

# Rotate the robot.
#wheels[0].setVelocity(1.0)
#wheels[1].setVelocity(-1.0)
#wheels[2].setVelocity(1.0)
#wheels[3].setVelocity(-1.0)
#robot.step(200 * timestep)

# Move forward.
#wheels[1].setVelocity(1.0)
#wheels[3].setVelocity(1.0)
#robot.step(300 * timestep)

# Rotate the robot.
#wheels[0].setVelocity(1.0)
#wheels[1].setVelocity(-1.0)
#wheels[2].setVelocity(1.0)
#wheels[3].setVelocity(-1.0)
#robot.step(130 * timestep)

# Move forward.
#wheels[1].setVelocity(1.0)
#wheels[3].setVelocity(1.0)
#robot.step(310 * timestep)

#instead of rotating and moving we will go backwords and rotate one time
wheels[0].setVelocity(-14.81) #go back at max speed
wheels[1].setVelocity(-14.81) 
wheels[2].setVelocity(-14.81)
wheels[3].setVelocity(-14.81)
robot.step(292 * timestep)
wheels[0].setVelocity(13) #turn left
wheels[1].setVelocity(-14.81) 
wheels[2].setVelocity(13)
wheels[3].setVelocity(-14.81)
robot.step(60 * timestep)
wheels[0].setVelocity(14.81) #move a bit forward
wheels[1].setVelocity(14.81) 
wheels[2].setVelocity(14.81)
wheels[3].setVelocity(14.81)
robot.step(47 * timestep)

# Stop.
for wheel in wheels:
    wheel.setVelocity(0.0)

# Move arm down
armMotors[3].setPosition(0)
armMotors[2].setPosition(-0.3)
robot.step(50 * timestep)

armMotors[1].setPosition(-1.0)
robot.step(50 * timestep)

armMotors[3].setPosition(-1.0)
robot.step(50 * timestep)

armMotors[2].setPosition(-0.4)
robot.step(50 * timestep)

# Open gripper.
finger1.setPosition(fingerMaxPosition)
finger2.setPosition(fingerMaxPosition)
robot.step(50 * timestep)
