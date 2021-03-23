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

- Ricardo Izecson dos Santos Leite > RIDSL

- Robert Downey, Jr > RDJ

#### First name, Middle Name, and Last Name 

1. First Name, Middle Name, and Last Name is from first, second, and third words of the name, if the fullname consists of 3 words.
2. Middle Name is empty string if fullname consists of 1 or 2 words.
3. Last Name is always the last words of the fullname. 
4. Middle Name is filled with any names between firstname and lastname

Examples:

**Fullname: Deodatus Andreas Deddy Cahyadi Sunjoyo**

- Firstname: Deodatus

- Middlename: Andreas Deddy Cahyadi

- Lastname: Sunjoyo


**Fullname: Akira Toriyama**

- Firstname: Akira

- Middlename: <empty string>

- Lastname: Toriyama


**Fullname: Rudy**

- Firstname: Rudy

- Middlename: <empty string>

- Lastname: <empty string>


### Data Format

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

### Prerequisites

- Python version 3.8 or above

- pip

- fastapi

- uvicorn

- GNU make

### Install Dependencies

```shell
pip install -r requirements.txt
```

### Running Tests

Running all tests.

```shell
make test
```

Running per test module, let's say we want to test `test_user_initial_name` module.

```shell
pytest -vv example/tests/test_user_initial_name.py
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
