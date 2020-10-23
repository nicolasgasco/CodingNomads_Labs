'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

# We have distance and time. We need to convert both in kms and hours.
distance_km = 10 * 1.6
time_hr = 30.5 / 60

# Calculate speed
speed = distance_km / time_hr

# Final output
print("The runner speed is", round(speed, 2), "km/h")