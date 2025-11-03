# and, not , or
# True, False

raining = True
temperature = 18

if temperature > 19 and not raining:
    print("Weather fine")
elif not raining:
    print("At least its's dry")  
else:
    print("Stay in") 

mood = "good" if not raining else "bad"
print(mood)

