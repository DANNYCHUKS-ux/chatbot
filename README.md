# Basic Chatbot Using Python

## Project Overview

The Basic Chatbot is a simple, rule-based chatbot developed using Python. It interacts with users through a command-line interface and responds to specific messages using predefined responses.

The chatbot recognises inputs such as "hello", "how are you", and "bye". It also handles unrecognised messages by informing the user that it does not understand the input. Users can type "exit" to end the conversation.

This project demonstrates how Python can be used to build a simple interactive program using fundamental programming concepts.

## Features

- Welcomes users when the program starts.
- Responds to predefined messages.
- Converts user input to lowercase for consistent matching.
- Removes unnecessary spaces from user input.
- Uses a loop to keep the conversation running.
- Provides a default response for unrecognised messages.
- Allows users to exit the chatbot using the `exit` command.

## Technologies Used

- **Python 3**
- Functions
- `while` loops
- `if`, `elif`, and `else` statements
- User input and output
- String methods such as `.strip()` and `.lower()`

## How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in your terminal or code editor.
4. Run the following command:

```bash
python basic_chatbot.py
```

Replace `basic_chatbot.py` with the actual name of your Python file if it is different.

## How to Use the Chatbot

1. Run the Python program.
2. Type `hello` to receive a greeting.
3. Type `how are you` to receive a predefined response.
4. Type `bye` to receive a goodbye message.
5. Enter an unrecognised message to see the chatbot's default response.
6. Type `exit` to close the chatbot.

## Example Interaction

```text
Welcome to Basic Chatbot!
Type 'hello', 'how are you', or 'bye' to chat.
You can also type 'exit' to close the chatbot.

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: bye
Bot: Goodbye!

You: exit
Bot: Chatbot closed. Have a nice day!
```

## What I Learned

Through this project, I practised defining and calling functions, using `while` loops, implementing conditional logic, accepting user input, and processing strings.

I also learned how to keep a program running until a specific condition is met and how to handle messages that do not match the chatbot's predefined responses.

## Limitations

This chatbot uses predefined rules and responses. It does not use artificial intelligence or natural language processing, so it cannot understand messages outside the patterns explicitly programmed into it.

## Future Improvements

- Add more predefined questions and responses.
- Recognise different ways of expressing the same message.
- Support additional conversational topics.
- Introduce a graphical user interface.
- Explore natural language processing in a future version.

## Acknowledgement

This project was completed as part of my learning experience with Code Alpha.

## Author

Daniel Ohaezu
