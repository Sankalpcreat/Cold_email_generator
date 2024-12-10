# Cold Email Generator

## Overview

The Cold Email Generator is a React-based web application that helps users generate personalized cold emails based on job descriptions. The application utilizes Tailwind CSS for styling and Vite as the build tool for a fast development experience.

## Features

- **Job Description Analysis**: Input a job description URL to analyze and extract relevant information.
- **Cold Email Generation**: Automatically generate a personalized cold email based on the job description.
- **Responsive Design**: The application is designed to be responsive and user-friendly across various devices.

## Technologies Used

- **React**: A JavaScript library for building user interfaces.
- **Vite**: A fast build tool and development server for modern web projects.
- **Tailwind CSS**: A utility-first CSS framework for styling.
- **TypeScript**: A typed superset of JavaScript that compiles to plain JavaScript.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Node.js (version 14 or higher)
- npm (Node package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cold_email_generator.git
   cd cold_email_generator
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```

### Running the Application

To start the development server, run:

```bash
npm run dev
```

Open your browser and navigate to `http://localhost:5173` to view the application.

### Building for Production

To build the application for production, run:

```bash
npm run build
```

This will create an optimized build in the `dist` directory.

## Usage

1. Enter the job description URL in the input form.
2. Click the "Generate" button to analyze the job description and generate a cold email.
3. View the results in the output cards.

## Directory Structure

### `src/`

The `src` directory contains the core functionality of the application, including agents for processing job descriptions and generating cold emails.

- **`agent/`**: Contains the logic for the cold email writer and job description parser agents.
  - **`agent.py`**: Base agent functionality.
  - **`cold_email_writer_agent/`**: Handles the generation of cold emails based on job descriptions.
    - **`agent.py`**: Implements the cold email writing logic.
    - **`model.py`**: Defines the input and output models for the cold email writer.
  - **`job_description_parser_agent/`**: Parses job descriptions from URLs.
    - **`agent.py`**: Implements the job description parsing logic.
    - **`model.py`**: Defines the input and output models for the job description parser.
  
- **`utils.py`**: Contains utility functions for web scraping and text cleaning.
- **`config.py`**: Loads configuration settings, including API keys.
- **`app.py`**: The main FastAPI application that exposes endpoints for parsing job descriptions and generating cold emails.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for the libraries and tools that made this project possible.
