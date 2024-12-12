# Adventure Game
print("🎮 Adventure Game! 🎮")
name = str(input("Hey, Type your gaming name: "))
print(f"Hello {name}, Welcome to my game!")

should_we_play: str = input("Do you want to play? (y/n): ").lower()

if should_we_play == "y":

    while True:
        weapon: str = input("Choose your weapon (sword/axe): ").lower()
        if weapon == "sword":
            print("🗡️ Sword selected!")
        elif weapon == "axe":
            print("🪓 Axe selected!")
        else:
            print("❌ Invalid option! Default sword is selected!")
            weapon = "sword"
        print("🎉 We are gonna play! 🎉")
        direction: str = input("Do you wanna go left or right? (left/right): ").lower()
        if direction == "left":
            choice: str = input("Okay, You can see a bridge. Do you wanna cross it or swim under it. (swim/cross): ").lower()

            if choice == "swim":
                print("🦈 You encountered an alligator and got eaten! 💀 You died! Game over!")
                try_again: str = input("Want to try again? (y/n): ").lower()
                if try_again == "y":
                    continue
                else:
                    break
            elif choice == "cross":
                if weapon == "axe":
                    print("⚔️ You encountered a bandit with a sword! Unfortunately, your axe wasn't enough. You died! Game over!")
                    try_again: str = input("Want to try again? (y/n): ").lower()
                    if try_again == "y":
                        continue
                    else:
                        break
                elif weapon == "sword":
                    print("⚔️ You encountered a bandit with a sword! You fought valiantly and defeated the bandit! 🎉")
                    print("💎 At the end of the bridge, you found a treasure box! 🏆 You win!")
                break
            else:
                print("❌ Invalid choice. You got lost in the woods and were never seen again. 😵 Game over!")
                break
        elif direction == "right":
            print("Okay, you went right and ☠️ fell off a cliff! Game over! ☠️")
            try_again: str = input("Want to try again? (y/n): ").lower()
            if try_again == "y":
                continue
            else:
                break
        else:
            print("❌ Invalid direction. You wandered aimlessly until nightfall. You died of hunger! 🥀 Game over!")
            break
    print("🎮 Thanks for playing! See you next time!")
else:
    print("We are NOT playing...")
    print("See you again. Goodbye!")



    