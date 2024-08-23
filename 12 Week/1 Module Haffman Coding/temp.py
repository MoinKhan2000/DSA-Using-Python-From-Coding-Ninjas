# Open the file in write mode ('w')
with open("./temp.txt", "a") as file:
    for _ in range(1):
        for letter in "adsagjasgasdjkldjfglasjgaksdfjasddkfaskdfjklasdjfalskjfasdlkfjaskdfaslkdjfa":
            file.write(letter)
