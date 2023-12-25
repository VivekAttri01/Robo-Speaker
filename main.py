import os
if __name__ == '__main__':
    print("Welcome to Robo Speaker ")
    while True:
        x = input("what you want me to speak :")
        if x == "v":
            os.system("say 'thank you my friend")
            break
        command = f"say {x}"
        os.system(command)
