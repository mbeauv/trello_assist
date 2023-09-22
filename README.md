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
   git clone https://github.com/mbeauv/trello_assist
   cd trello_assist
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
   python main.py
   ```

### Docker Setup

1. **Build the Docker Image**:
   ```sh
   docker build -t trello_assist .
   ```

2. **Run the Docker Container**:
   ```sh
   docker run trello_assist
   ```


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
```

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
```


## Agile Sprint Schema Documentation

This project utilizes a JSON schema to define Agile Sprints and their associated User Stories. Below is a detailed explanation of the schema's structure.

### Schema Overview

The schema is designed to represent an Agile Sprint, containing metadata about the sprint itself and an array of User Stories. Each User Story has its own set of properties, including title, user story statement, description, acceptance criteria, notes, priority, and estimation.

### Schema Structure

#### Sprint

- `sprintId` (string, required): The unique identifier or number for the sprint.
- `duration` (integer, required): The duration of the sprint in days.
- `description` (string, optional): A description or theme of the sprint.
- `userStories` (array of [UserStory](#userstory), required): A list of user stories included in the sprint.

#### UserStory

- `title` (string, required): The title of the user story.
- `userStory` (string, required): The main user story statement, typically representing a feature or requirement.
- `description` (string, optional): A detailed description of the user story.
- `acceptanceCriteria` (array of string, required): A list of conditions that must be fulfilled for the user story to be considered complete.
- `notes` (array of string, optional): Any additional notes or considerations regarding the user story.
- `priority` ([Priority](#priority), required): The priority level of the user story.
- `estimation` ([FibonacciEstimation](#fibonacciestimation) or [TShirtSizeEstimation](#tshirtsizeestimation), required): The estimation of effort required for the user story, represented either in Fibonacci sequence or T-Shirt sizes.

#### Priority

- Enum of string ["Low", "Medium", "High"]: Represents the priority levels for tasks or user stories.

#### FibonacciEstimation

- Enum of integer [1, 2, 3, 5, 8, 13]: Represents the estimation values based on the Fibonacci sequence.

#### TShirtSizeEstimation

- Enum of string ["XS", "S", "M", "L", "XL", "XXL"]: Represents the estimation values based on T-Shirt sizes.

### Example

```json
{
  "sprintId": "Sprint1",
  "duration": 14,
  "description": "This sprint focuses on initial feature development.",
  "userStories": [
    {
      "title": "User Story 1",
      "userStory": "As a user, I want to be able to log in so that I can access my account.",
      "description": "This user story is focused on developing a login feature.",
      "acceptanceCriteria": ["User can log in using their credentials and access their account."],
      "notes": ["Consider implementing OAuth for enhanced security."],
      "priority": "High",
      "estimation": 5
    },
    {
      "title": "User Story 2",
      "userStory": "As a user, I want to be able to log out so that I can secure my account.",
      "description": "This user story is focused on developing a logout feature.",
      "acceptanceCriteria": ["User can log out, and their session is terminated securely."],
      "notes": ["Ensure that session termination is handled securely to prevent unauthorized access."],
      "priority": "Medium",
      "estimation": "S"
    }
  ]
}
```

## Contributing

Contributions are greatly appreciated! Please review the [GitHub issues](https://github.com/mbeauv/trello_assist/issues) section of our repository to find something that interests you. Look for issues tagged with `enhancements` for areas where we plan future work.

## Future Work

For upcoming features and improvements, please refer to the issues tagged with `enhancements` in the [GitHub issues](https://github.com/mbeauv/trello_assist/issues) section of our repository.


