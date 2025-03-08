# Instagram Video Downloader

Instagram Video Downloader is a Django-based web application that allows users to download their favorite Instagram videos in HD quality. 

## Features

- Download Instagram videos by pasting the video URL.
- Simple and user-friendly interface.
- Uses Django framework for backend processing.
- Bootstrap for responsive design.

## Project Structure

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/instagram-video-downloader.git
    cd instagram-video-downloader
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

1. Copy the URL of the Instagram video you want to download.
2. Paste the URL in the input box on the landing page.
3. Click the "Download" button to get your video.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Instaloader](https://instaloader.github.io/)
