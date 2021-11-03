# PythonATM

# SPECIFICATIONS

The main functions of the ATM simulator may be summarized as follows:

Before performing any transaction, the user must enter his or her username and PIN (personal identification number) at an input screen/prompt (GUI or otherwise).

The system must validate the user information against the information that is pre-built into the system. For the purposes of this project, the system will have the following three username: PIN pairings to start.

Deposit, The user must enter the amount to be deposited into his or her account. The amount of the deposit must be added to the current balance into the account. Appropriate confirmation messages must be provided indicating the amount of the deposit and the new current balance. Proper data input validation to ensure that numerical data is input must be used along with error handling.

Keep in mind that if you are working with the Basic Functionality model, the balances are stored in the list, which will be lost once the program ends. If you use files to store the information, then the new balances should be saved and available when the program runs subsequent times.
Withdrawal, The user must enter the amount to withdraw. Each withdrawal transaction is subject to a maximum of $1,000 per transaction. If the user enters an amount greater than $1000, the system must present a message indicating that $1000 is the maximum per withdrawal. The ATM accepts only transactions for which the amount entered is a multiple of $10. There is no daily maximum amount apart from the user’s account balance in which case the system must also inform the user if the account balance is less than the transaction amount.

Account Balance When the user selects this option, the system simply checks the data for that user and displays the current balance. Checking the account balance does not alter the balance itself.

Changing the PIN Changing the PIN is available to all users. The difference in how this functions is dependant on how you set up the program. If you are using the Basic Functionality model using lists to store user information, the change in PIN will only be effective during the current running of the program. Once you quit the program and start it again all data values return to the original values. However if you are working with the Extended Functionality model and you are using files to store the information, the change in PIN will be committed to the file and be available for subsequent accesses using this new value.

Administrator Functions (Extended Functionality)

The following functions concern the ATM's functioning with respect to the system administrator and the internal mechanisms of the ATM, not the user.

Plot Account Balances

This feature of the Administrator menu is not something that is realistic, however it is used in this project for the sole purpose of having you implement the use of Python’s graph and plotting feature.

![1](https://user-images.githubusercontent.com/72087494/140218023-d0537e16-66b9-478b-9385-41be967dc5b8.jpg)

![2](https://user-images.githubusercontent.com/72087494/140217998-c84196bd-1a7a-469d-9c7d-dcf1ca1c0e0a.jpg)

![3](https://user-images.githubusercontent.com/72087494/140218010-a93f7fc2-81a9-4cb4-ac7e-06790ceb2904.jpg)

![4](https://user-images.githubusercontent.com/72087494/140218018-fc78777e-d625-48e8-985d-7bf3c8fa46db.jpg)
