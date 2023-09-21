# Trello Assist

Trello Assist is a Python-based application designed to facilitate the creation of Trello boards from JSON files that define Agile sprints. Initially developed to generate rudimentary Scrum sprints, future enhancements aim to support a broader range of Agile methodologies. The tool was conceived to streamline the process of transforming conversations and interactions with ChatGPT into structured, actionable Trello boards, allowing for seamless transition from user story discussions to sprint creation.

## Features

Trello Assist currently supports the following features:

1. **Create a Trello Board**: Generate a new Trello board from a given sprint JSON file.
2. **Delete a Trello Board**: Remove an existing Trello board.
3. **List Cards**: Display the cards of a specified Trello board.
4. **Describe a Card**: Provide detailed information about a given card in a specified board.

## Installation & Setup

### Standard Python Setup

1. **Clone the Repository**:
   ```sh
   git clone [Your Repository URL]
   cd [Your Repository Name]
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```sh
   python [Your Main Script].py
   ```

### Docker Setup

1. **Build the Docker Image**:
   ```sh
   docker build -t trello_assist .
   ```

2. **Run the Docker Container**:
   ```sh
   docker run -p 8000:8000 trello_assist
   ```

   Replace `8000:8000` with the actual port mapping you need.

### Configuration

After installation, don't forget to set up your Trello API key and token using the `set_config` command:

```sh
python trello_cli.py set_config --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN
```

Or, to be prompted for the values:

```sh
python trello_cli.py set_config
```

## Usage

### Create Board Command

The `create_board` command is used to create a new Trello board. 

#### Parameters:
- `--api-key` (Required): Your Trello API key. If not provided, you will be prompted to enter it.
- `--oauth-token` (Required): Your Trello OAuth token. If not provided, you will be prompted to enter it.
- `--board-name` (Required): The name of the board to be created. You will be prompted to enter it if not provided.
- `--board-desc` (Optional): An optional description for the board.

#### Description:
This command will create a new Trello board with the specified name and description. If the board is successfully created, the command will output the ID of the newly created board. If the board creation fails, it will output an error message.

#### Invocation Example:
```sh
python trello_cli.py create_board --api-key YOUR_API_KEY --oauth-token YOUR_OAUTH_TOKEN --board-name "New Board" --board-desc "Description of the new board"


### Create Sprint Command

The `create_sprint` command is used to process a user story file and create a corresponding Trello board.

#### Parameters:
- `--api-key` (Required): Your Trello API key. If not provided, you will be prompted to enter it.
- `--oauth-token` (Required): Your Trello OAuth token. If not provided, you will be prompted to enter it.
- `--filename` (Optional): The name of the file containing sprint info. Defaults to `sample_sprint.json` if not provided.

#### Description:
This command will read a user story file specified by `--filename`, validate it against a predefined schema, and create a corresponding Trello board. If the board is successfully created, the command will output the result. If the board creation fails, it will output an error message. If the file processing fails, it will print a failure message.

#### Invocation Example:
```sh
python trello_cli.py create_sprint --api-key YOUR_API_KEY --oauth-token YOUR_OAUTH_TOKEN --filename "your_sprint_file.json"


## Contributing

Contributions are greatly appreciated! Please review the [GitHub issues](https://github.com/mbeauv/trello_assist/issues) section of our repository to find something that interests you. Look for issues tagged with `enhancements` for areas where we plan future work.

## Future Work

For upcoming features and improvements, please refer to the issues tagged with `enhancements` in the [GitHub issues](https://github.com/mbeauv/trello_assist/issues) section of our repository.
```

