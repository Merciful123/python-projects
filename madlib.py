# suppose we want to create a string that says "subscribe to ____"

# youtuber = "abc"  # some string variable

# A few ways to do this

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adj:")
verb1 = input("verb1:")
verb2 = input("verb2:")
famous_person = input("famous person:")

madlib = f"Computer programming is so {adj}! It makes me so excited all the \ntime because I love to {verb1}.Stay hydrated and {verb2} like a {famous_person}!"

print(madlib)
  
