# Interview Transcript Summarizer

This is a Python script that uses the GPT-3 API from OpenAI to summarize an interview transcript. The script reads in a transcript from a text file and then generates a summary of each dialogue using GPT-3.

## Requirements

- Python 3.6 or higher
- OpenAI API key
- openai Python package

## Installation

- Clone this repository to your local machine.
- Navigate to the project directory in your terminal.
- Create a virtual environment using virtualenv: <br>

  ```sh
  virtualenv venv
  ```

- Activate the virtual environment: <br>

  ```sh
  source venv/bin/activate
  ```

- Install required packages: <br>
  ```sh
  pip install -r requirements.txt
  ```

## Usage

- Add your OpenAI API key to a file named .env in the project directory: <br>

  ```sh
  OPENAI_API_KEY=<your-api-key>
  ```

- Create a text file with the transcript you want to summarize.
- Run the script with the following command: <br>

  ```sh
  python summarize_transcript.py <input_filename> <output_filename> [--prompt=<prompt>] [--length=<length>]
  ```

  - `<input_filename>`: The name of the input text transcript file along with the path.
  - `<output_filename>`: The name of the output that will be generated along with path.
  - `--prompt=<prompt>` (optional): The prompt to use for GPT-3. Defaults to "Summarize an interview transcript using GPT-3".
  - `--length=<length>` (optional): The maximum length of the summary in tokens. Defaults to 600.

  ### Example:

  ```sh
  python summarize_transcript.py transcript.txt summary.txt --prompt="Summarize this interview" --length=500
  ```

## License

This code is licensed under the MIT License. See the [LICENSE](https://github.com/dhanumamidi/Interview-Transcript-Summarizer/blob/main/LICENSE) file for details.
