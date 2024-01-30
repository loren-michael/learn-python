# Sal's Shipping

weight = 41.5
cost = 0.00
ground_flat = 20.00

if weight <= 2:
  cost = weight * 1.50 + ground_flat
  drone_cost = weight * 4.50
elif weight <= 6:
  cost = weight * 3.00 + ground_flat
  drone_cost = weight * 9.00
elif weight <= 10:
  cost = weight * 4.00 + ground_flat
  drone_cost = weight * 12.00
elif weight > 10:
  cost = weight * 4.75 + ground_flat
  drone_cost = weight * 14.25


print('Ground shipping cost: $', cost)
print('Premium ground shipping: $ 125.00')
print('Drone shipping: $', drone_cost)


