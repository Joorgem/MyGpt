# MyGPT

MyGPT is an interactive chat application using the OpenAI GPT-3.5-turbo or GPT-4 model, developed with Streamlit. The project is structured to facilitate future updates and improvements, using two utility files (`utils_files.py` and `utils_openai.py`) to organize the code modularly.

## Features

- Save and load conversations using `pickle` files
- Convert and revert message file names
- List all saved conversations
- Save and load API keys
- Interact with the OpenAI API to generate chat responses
- Interactive interface with tabs for conversations and settings

## Requirements

- Python 3.7 or higher
- Libraries listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/joorgem/MyGpt.git
    cd MyGpt
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run MyGpt.py
    ```

2. Access the application in your browser at `http://localhost:8501`.

## Project Structure

- **MyGpt.py**: Main application file that initializes the user interface with Streamlit.
- **utils_files.py**: Contains utility functions for saving, loading, and listing conversations, as well as saving and loading the API key.
- **utils_openai.py**: Contains the function for interacting with the OpenAI API.
- **requirements.txt**: Project dependency list.

## Configuration

### Conversations Tab

- Create a new conversation or select an existing conversation.
- Conversations are listed in descending order of modification date.

### Settings Tab

- Select the language model (`gpt-3.5-turbo` or `gpt-4`).
- Add your OpenAI API key. The key will be saved for future use.

## Contribution

If you want to contribute to the project, follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b my-new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin my-new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

Jorge M.  
GitHub: [joorgem](https://github.com/joorgem)
