
    if score>num:
      break
    bat=input("Take Strike: ")
    if bat.isdigit():
      bat=int(bat)
      if not 1<=bat<=6:
        print("Strike between 1 to 6")
        continue
      ball=bal()
      if ball!=bat: