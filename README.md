# Real-time Face Recognition Website

This project is a real-time face recognition website that captures video frames from a webcam and sends them to a backend server for face detection and recognition. The website allows users to upload and compare their face images against a database of family members.

## Key Features
- Real-time video stream from webcam
- Live face recognition using Flask-SocketIO backend
- Secure login and image upload
- AWS S3 integration for image storage

## Technologies Used
- Flask (for backend server)
- React (for frontend)
- Socket.IO (for real-time communication)
- OpenCV and face_recognition (for image processing)
- AWS S3 (for image storage)

## Setup Instructions

### Prerequisites
- Python 3.x
- Node.js and npm
- Flask and Flask-SocketIO
- OpenCV, face_recognition libraries

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/coderabhay332/facial-reco.git
   cd facial-reco
   ```

2. Install the backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Install the frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

4. Run the backend server:
   ```bash
   flask run
   ```

5. Start the frontend:
   ```bash
   npm start
   ```

## Features

### 1. Real-time Video Feed
The website captures video frames from the user’s webcam using the `getUserMedia` API and sends them to the Flask backend using Socket.IO.

### 2. Face Recognition
The backend processes video frames with OpenCV and `face_recognition` to detect and recognize faces. The system compares detected faces with pre-uploaded images stored in AWS S3.

### 3. User Authentication and Image Upload
Users can sign up, log in, and upload images to the platform. Each user’s images are securely stored in AWS S3. The system checks for face matches against these uploaded images.

## API Endpoints

- `POST /api/upload`: Uploads an image to AWS S3.
  - Input: FormData with image file.
  - Output: URL of uploaded image.

- `GET /api/recognize`: Processes video frame and returns recognition result.
  - Input: Base64-encoded image.
  - Output: JSON with recognition result.

## How to Use

1. Sign up and log in to the platform.
2. Start the camera by clicking "Start Camera."
3. The system will automatically detect and recognize faces in real-time.
4. Upload images to the platform for comparison.

## Troubleshooting

- **Issue**: Camera not working.
  - **Solution**: Ensure the browser has permission to access the webcam.

- **Issue**: Recognition is slow.
  - **Solution**: Try reducing video quality or ensure the backend server is running efficiently.

## Conclusion

This project demonstrates a real-time face recognition system using modern web technologies. Feel free to contribute to the project by opening issues or submitting pull requests.

For more information, contact the project owner at: [akgabhay11@gmail.com, softgpt9299@gmail.com]
