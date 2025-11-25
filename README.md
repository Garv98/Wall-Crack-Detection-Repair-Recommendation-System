# Wall Crack Detection & Repair Recommendation System

A comprehensive project for detecting cracks in wall images and videos, assessing severity, and providing AI-generated repair suggestions based on Indian engineering codes (IRC, IS). Includes static image analysis, live video processing, and a Streamlit web app.

## Features
- **Image Crack Detection**: Analyze uploaded images for cracks using OpenCV edge detection.
- **Severity Assessment**: Calculate crack area and decide if repair is needed.
- **Live Video Detection**: Real-time crack detection from IP camera feeds.
- **AI Repair Suggestions**: Generate recommendations using a local Ollama LLM (llama3.2 model).
- **Web App**: Interactive Streamlit interface for easy use.

## Installation
1. Clone the repo:
   ```
   git clone https://github.com/Garv98/Wall-Crack-Detection-Repair-Recommendation-System.git
   cd Wall-Crack-Detection-Repair-Recommendation-System
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. For AI suggestions, run a local Ollama server with `llama3.2:latest` at `http://127.0.0.1:11434/v1`.

## Usage

### Web App (app_merged.py or app_merged2.py)
Run the Streamlit app for interactive crack detection:
```
streamlit run app_merged.py
```
- Upload a JPEG/PNG image.
- View detection results, severity, and AI repair suggestions.

### Jupyter Notebook (crack.ipynb)
For static image analysis:
- Open in Jupyter: `jupyter notebook crack.ipynb`
- Run cells to detect cracks in wallcrack.jpg (or your image).
- Displays original and processed images with repair decision.

### Live Video Detection (live_video_detection.py)
For real-time video processing:
```
python live_video_detection.py
```
- Update `url` with your IP camera address (e.g., from IP Webcam app).
- Press 'q' to quit. Outputs a video file `crack_detection_output.avi`.

## Files Description
- **app_merged.py / app_merged2.py**: Merged Streamlit apps for web-based crack detection and AI suggestions.
- **crack.ipynb**: Jupyter notebook for image crack detection, severity assessment, and visualization.
- **requirements.txt**: Python dependencies (opencv-python, streamlit, numpy, pillow, requests, matplotlib).
- **wallcrack.jpg**: Sample wall image for testing crack detection.
- **live_video_detection.py**: Script for live video crack detection from IP camera.

## Notes
- Ensure images are in JPEG/PNG format.
- For deployment, update the Ollama server URL or integrate a cloud AI service.
- Thresholds (e.g., area=5000) are configurable for severity.
