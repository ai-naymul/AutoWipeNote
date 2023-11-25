# AutoWipeNote

AutoWipeNote is a simple note-taking application built with Python's Tkinter library. It features a unique functionality where the text in the note automatically gets deleted after a certain period of inactivity.

## Installation

1. Ensure you have Python installed on your system. If not, download and install Python from [here](https://www.python.org/downloads/).

2. Clone the repository:
    ```git clone https://github.com/ai-naymul/AutoWipeNote.git```
3. Navigate to the project directory:
    ```cd AutoWipeNote```

## Usage

1. Run the `main.py` script:
    ```python main.py```

2. The application window will open. You can start typing in the text box.

3. If there is no typing activity for a certain period (default is 3000 milliseconds), the text will automatically get deleted.

## Customization

You can customize the delay time before the text gets deleted. To do this, modify the [delete_delay](file:///e%3A/Professional%20Python%20Project/AutoWipeNote/main.py#9%2C37-9%2C37) argument when creating an instance of `DeleteText` in `main.py`:
    ```inputs = DeleteText(window, delete_delay=5000) # delay time is now 5000 milliseconds```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)