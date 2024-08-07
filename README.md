# BMI Calculator Web Application

A FastAPI web application for calculating Body Mass Index (BMI). Features a responsive HTML interface with static assets for styling and functionality.

## Features

- **BMI Calculation**: Calculate your BMI based on weight (kg) and height (m).
- **Responsive Design**: User-friendly interface with HTML, CSS, and JavaScript.
- **Static Assets**: Includes CSS for styling, JavaScript for dynamic functionality, and SVG logo.

## Getting Started

### Prerequisites

- [Python 3.8 or later](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/khabzox/BmiCalc.git
    cd BmiCalc
    ```

### Running the Application

1. **Start the FastAPI Server**

    ```sh
    uvicorn main:app --reload
    ```

2. **Open Your Browser**

    Navigate to `http://127.0.0.1:8000` to view the application.

## Project Structure

```markdown
python-api/
│
├── BmiCalc.py # Module for BMI calculation logic
├── main.py # FastAPI application entry point
├── vercel.json # Vercel deployment configuration
├── requirements.txt # Python dependencies
└── templates/
├── assets/
│ ├── main.js # JavaScript for dynamic functionality
│ ├── style.css # CSS for styling
│ └── logo.svg # Logo image
└── index.html # Main HTML file
```

## How to Use

1. Enter your weight in kilograms and height in meters into the form on the main page.
2. Submit the form to calculate your BMI.
3. View the result along with a health category based on your BMI value.

## How BMI is Interpreted

- **Less than 18.5**: Underweight
- **18.5 - 24.9**: Healthy weight
- **25 - 29.9**: Overweight
- **30 and above**: Obesity

> [!NOTE]
> BMI is a general guide. For a comprehensive health evaluation, consult with a healthcare professional.

## Contributing

Feel free to submit issues or pull requests to improve the project. Please follow the standard contribution guidelines and ensure that your changes are tested.