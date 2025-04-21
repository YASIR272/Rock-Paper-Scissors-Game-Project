import random

def play_rps():
    options = ['rock', 'paper', 'scissors']
    print("🪨 Rock, 📄 Paper, ✂️ Scissors - Let's play!")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            print("👋 Thanks for playing!")
            break

        if user_choice not in options:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 It's a tie!\n")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 You win!\n")
        else:
            print("💻 Computer wins!\n")

# Start the game
play_rps()
