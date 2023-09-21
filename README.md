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

### Create a Trello Board

[Provide specific command and examples for creating a Trello board.]

### Delete a Trello Board

[Provide specific command and examples for deleting a Trello board.]

### List Cards

[Provide specific command and examples for listing cards in a Trello board.]

### Describe a Card

[Provide specific command and examples for describing a card in a Trello board.]

## Contributing

Contributions are greatly appreciated! Please review the [GitHub issues](https://github.com/mbeauv/trello_assist/issues) section of our repository to find something that interests you. Look for issues tagged with `enhancements` for areas where we plan future work.

## Future Work

For upcoming features and improvements, please refer to the issues tagged with `enhancements` in the [GitHub issues](https://github.com/mbeauv/trello_assist/issues) section of our repository.
```

