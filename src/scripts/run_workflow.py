import expense_notify


def main():
    print(
        """
           _____                                  _   _       _   _  __       
| ____|_  ___ __   ___ _ __  ___  ___  | \ | | ___ | |_(_)/ _|_   _ 
|  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \ |  \| |/ _ \| __| | |_| | | |
| |___ >  <| |_) |  __/ | | \__ \  __/ | |\  | (_) | |_| |  _| |_| |
|_____/_/\_\ .__/ \___|_| |_|___/\___| |_| \_|\___/ \__|_|_|  \__, |
           |_|                                                |___/ 
          """
    )
    expense_notify.run_expense_notify()


if __name__ == "__main__":
    main()