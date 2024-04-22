
# 2021.05.03


# battery
# -------

# number of lipo cells
numberOfLiPoCells = 3
      
# voltage per lipo cell
liPoCellVoltage = 3.7

# estimated actual lipo voltage
estimatedTotalLiPoVoltage = 10.5

# 100% lipo voltage
totalLiPoVoltagePercentage = 100

# lipo milliamp rating
liPomAh = 2200

# lipo 'C' amp rating
liPoCRating = 20

# lipo mAh reserve - 90%
LiPoReserve = 0.90

totalLiPoVoltage = round(numberOfLiPoCells * liPoCellVoltage, 1)


# lipo efficiency percentage
liPoEfficiencyPercentage = round(
    totalLiPoVoltagePercentage - (((totalLiPoVoltage - estimatedTotalLiPoVoltage) / totalLiPoVoltage) * 100))

estimatedLiPoVoltage = round(totalLiPoVoltage * (liPoEfficiencyPercentage / 100), 1)
      
liPoAmps = round((liPomAh * liPoCRating) / 1000)
      
estimatedLiPoWatts = round(estimatedLiPoVoltage * liPoAmps)


print('')
print("Battery")
print("-------")
print('')

print("LiPo Cells = " + str(numberOfLiPoCells) + "S")

print("LiPo Cell Voltage = " + str(liPoCellVoltage) + "V")

print("Total LiPo Voltage = " + str(totalLiPoVoltage) + "V")

print("LiPo mAh = " + str(liPomAh) + "mAh")

print("LiPo 'C' rating = " + str(liPoCRating) + "C")

print("LiPo Amps ( mAh * 'C' rating ) = " + str(liPoAmps) + " Amps")

print('')

print("Estimated LiPo efficiency = " + str(liPoEfficiencyPercentage) + "%")

print("Estimated LiPo Voltage = " + str(estimatedLiPoVoltage) + "V")

print("Estimated LiPo Watts ( Estimated voltage * Amps ) = " + str(estimatedLiPoWatts) + "W")

print('')


# motor
motorKVRating = 1100  # 3800
      
estimatedMaximumMotorAmpRating = 22  # 25


# Efficiency of motor - 85%
MotorEfficiency = 0.85

# Efficiency of mechanics - 90%
MechanicsEfficiency = 0.90

# If motor rating in Watts
# amps = watts / volts

# watts = volts * amps

# Ohms Law
# volts (E) = amps (I) * ohms (R)
# amps (I) = volts (E) / ohms (R)
# ohms (R) = volts (E) / amps (I)

# Estimated Motor Amp draw 80%
EstimatedMotorAmpDraw = 0.80

# Calculate estimated average motor Amp draw
EstimatedAverageMotorAmpDraw = estimatedMaximumMotorAmpRating * EstimatedMotorAmpDraw

# Calculate LiPo Amp hours
LiPoAmpHours = (liPomAh * LiPoReserve) / 1000

# Calculate LiPo Amp minutes
LiPoAmpMinutes = LiPoAmpHours * 60

# calculate estimated running time
EstimatedLiPoRunningTime = round(LiPoAmpMinutes / EstimatedAverageMotorAmpDraw, 2)

EstimatedMotorEfficiency = MotorEfficiency * 100

EstimatedMechanicsEfficiency = MechanicsEfficiency * 100


print('')
print("Motor")
print("-----")
print('')

print("Motor kV rating = " + str(motorKVRating) + "kV")

print("Estimated Maximum Motor Amp Rating = " + str(estimatedMaximumMotorAmpRating) + " Amps")

print("Estimated Average Motor Amp Draw = " + str(EstimatedAverageMotorAmpDraw) + " Amps")
print('')

print("Estimated running time = " + str(EstimatedLiPoRunningTime) + " minutes")
print('')

EstimatedMaximumMotorRPM = estimatedLiPoVoltage * motorKVRating

EstimatedDriveTrainEfficiency = EstimatedMaximumMotorRPM * MotorEfficiency * MechanicsEfficiency

print("Estimated motor efficiency = " + str(EstimatedMotorEfficiency) + "%")

print("Estimated mechanics efficiency = " + str(EstimatedMechanicsEfficiency) + "%")
print('')
print("Estimated Maximum Motor RPM ( Estimated voltage * Motor kV Rating ) = " + str(EstimatedMaximumMotorRPM) + " RPM")

print("Estimated actual motor RPM ( Estimated maximum motor RPM * Estimated drivetrain efficiency ) = " + str(EstimatedDriveTrainEfficiency) + " RPM")
print('')


# Rotor Head
MainGearTeeth = 140
      
PinionGearTeeth = 11


actualMotorRPM = round(MainGearTeeth / PinionGearTeeth, 2)

print('')
print("Main Rotor")
print("----------")
print('')

print("Main Gear Teeth = " + str(MainGearTeeth))
print("Pinion Gear Teeth = " + str(PinionGearTeeth))
print('')

print("1 RPM of Main rotor = " + str(actualMotorRPM) + " Actual Motor RPM")
print('')

EstimatedMaximumMainRotorRPM = EstimatedMaximumMotorRPM / actualMotorRPM

print("Estimated maximum main rotor RPM ( Estimated maximum motor RPM / Actual motor RPM ) = " + str(EstimatedMaximumMainRotorRPM) + " RPM")
