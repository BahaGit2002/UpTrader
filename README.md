# UpTrader

UpTrader is a Python Django application designed to provide a robust and scalable platform for managing trading activities. This project leverages Docker and Docker Compose for easy setup and deployment, and Poetry for dependency management.

## Table of Contents

- [UpTrader](#uptrader)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Deployment](#deployment)
  - [License](#license)
  - [Contributing](#contributing)
  - [Contact](#contact)

## Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed.
- [Poetry](https://python-poetry.org/docs/#installation) installed.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/BahaGit2002/UpTrader.git
   cd uptrader
   ```
   
2. **Install Python dependencies:**
   ```sh
   poetry install --no-root
   ```

3. **Create a .env file:**
   ```sh
   cp .env.example .env
   ```

4. **docker-compose up --build -d**
  ```sh
  docker-compose up --build -d
  ```