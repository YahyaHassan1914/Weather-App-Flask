# Weather App

A simple Flask-based weather application that fetches current weather conditions for a given location using the WeatherAPI. The app displays weather information such as temperature, description, and an icon representing the weather.

## Features

- Search for weather conditions by city.
- Display current temperature, weather description, and an icon.
- Responsive design with a clear layout.

## Requirements

- Python 3.x
- Flask
- Requests
- WeatherAPI account (for API key)

## Installation

### Clone the Repository

```bash
git clone https://github.com/YahyaHassan1914/Weather-App-Flask.git
cd weather-app
```

### Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Obtain API Key

1. Sign up for a free account at [WeatherAPI](https://www.weatherapi.com/).
2. Obtain your API key from the dashboard.

### Configure the API Key

Create a file named `api_key.json` in the root directory of your project and add your API key:

```json
{
  "api_key": "YOUR_API_KEY_HERE"
}
```

## Usage

### Running the Application

Run the Flask app:

```bash
python app.py
```

The application will start and be accessible at `http://127.0.0.1:5000/`.

### How to Use

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter a city name in the search box and click "Get Weather."
3. The current weather conditions for the specified city will be displayed, including temperature, description, and an icon.

## Project Structure

```
weather-app/
│
├── app.py               # Main Flask application
├── requirements.txt     # List of dependencies
├── api_key.json         # API key for WeatherAPI
├── static/
│   └── style.css        # CSS styles for the application
└── templates/
    ├── base.html        # Base HTML template
    └── index.html       # Template for the main page
```

## Contributing

Feel free to contribute to this project by opening an issue or submitting a pull request. Please ensure that your code adheres to the project's coding style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [WeatherAPI](https://www.weatherapi.com/) for providing the weather data.
- Flask and its contributors for creating the Flask web framework.

## Contact

For any questions or issues, please contact [yahyahassanmohamed1914@gmail.com](mailto:yahyahassanmohamed1914@gmail.com).
