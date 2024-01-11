################### Scope ####################

enemies = 1
# Global constants -> use upper case -> Only namming convention, nothing restricts in changing..
PI = 3.14

def increase_enemies():
  global enemies
  enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# There is no block scope.