# Twilio Messenger API

This is a simple Flask-based REST API that allows you to send SMS messages using Twilio. The API exposes an endpoint to send SMS messages to specified phone numbers.

## Installation

To get started, follow these steps:

### Prerequisites

- Python 3.6+
- A Twilio account (you can sign up [here](https://www.twilio.com/try-twilio))
- A Twilio phone number capable of sending SMS messages

### Setup

1. Clone the repository or download the source code.

    ```sh
    git clone https://github.com/yourusername/twilio-messenger-api.git
    cd twilio-messenger-api
    ```

2. Create a virtual environment and activate it.

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages.

    ```sh
    pip install flask twilio
    ```

4. Update the `send_sms` function in `main.py` with your Twilio credentials and phone number.

5. Run the Flask application.

    ```sh
    python main.py
    ```

The API will be available at `http://127.0.0.1:5000`.

## Usage

### Sending an SMS

To send an SMS, make a POST request to the `/send_sms` endpoint with a JSON payload containing the `to` and `body` fields.

Example request using `curl`:

```sh
curl -X POST http://127.0.0.1:5000/send_sms \
-H "Content-Type: application/json" \
-d '{
      "to": "+15558675310",
      "body": "Hello from Flask and Twilio!"
    }'
```

## Contributors
[Devakrishnan Gopal](https://www.github.com/gdevakrishnan)

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements, features, or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Twilio: [twilio.org](https://www.twilio.com/en-us)