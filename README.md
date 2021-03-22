# Test Driven Development (TDD) example

## Overview

This repository shows an example of TDD practice.

## Use Case

**As a Product Owner I want to have functionality to create new User**

User should have the following fields:

- id: string
- email: string
- first_name: string
- middle_name: string
- last_name: string
- initial_name: string

### Rules

#### User Id is in uuid version 4 format.

#### Initial name is a capitalised letters from each of all first words of the fullname the user.

Any punctuation characters from fullname is removed.

For example:

- Richard M Stallman > RMS

- Rama > R

- Ebet Kadarusman > EK

- Mirza Akbar Mulya Sudradjat > MAMS

- Robert Downey, Jr. > RDJ

#### Middlename is filled with any names between firstname and lastname

For example:

Fullname: Deodatus Andreas Deddy Cahyadi Sunjoyo

- Firstname: Deodatus

- Middlename: Andreas Deddy Cahyadi

- Lastname: Sunjoyo

Data will be sent to the server in the following format in JSON

```json
{
    "fullname": "Hisma Mulya Sudradjat",
    "email": "some@email.com"
}
```

Upon completion server will return in JSON format

```json
{
    "status": "ok",
    "data": {
        "id": "3bb656e9-6b4f-489f-87ba-0eed08282e26",
        "email": "hisma.mulya@gmail.com",
        "first_name": "Hisma",
        "middle_name": "Mulya",
        "last_name": "Sudradjat",
        "initial_name": "HMS"
    }
}
```

## Usage

### Prerequisite

- Python version 3.8 or above

- pip

- fastapi

- uvicorn

### Install Dependencies

```shell
pip install -r requirements.txt
```

### Running Tests

```shell
make test
```

### Running The Application

Run the application withoud hot reloading

```shell
make run
```

Run the application with hot reloading

```shell
make run_dev
```

## License

MIT
