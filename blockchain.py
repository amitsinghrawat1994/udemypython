# Initializing our (empty) blockchain list
blockchain = []
open_transaction = []
owner = "Max"


def get_last_blockchain_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(sender, recipient, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: the sender of the coins
        :recipient: The recipient of the coins.
        :amount: the amount of the coins sent with the transaction
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    open_transaction.append(transaction)


def min_block():
    pass


def get_transaction_value():
    """Returns the input of the user (a new transaction amount) as a float."""
    # Get the user input, transform it from a string to a float and store it in user_input

    tx_recipient = input("Enter the recipient of the transaction")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input("Your choice: ")
    # write a code for
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            # break

    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        add_transaction(tx_data, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain")
        break
    # print("Choice registered!")
else:
    print("User left!")

print("Done!")
