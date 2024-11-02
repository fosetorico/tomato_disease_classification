# Detection and Classification of Tomato Diseases for Farmers in Nigeria.

## Overview
An AI-powered system that uses computer vision to detect and classify tomato plant diseases, specifically designed to address agricultural challenges in Nigeria. This project aims to provide early disease detection capabilities to help prevent crop losses and improve food security.

## Background
Following the devastating 2015 Nigerian tomato crisis caused by Tuta absoluta (tomato leaf miner) infestation, which resulted in massive crop losses and economic impact, there has been an urgent need for better disease detection and management systems. This project leverages modern technology to address these ongoing agricultural challenges.

## Features
- Real-time disease detection and classification
- Support for three disease categories:
    - Early Blight
    - Late Blight
    - Healthy Plant Identification
- User-friendly web interface
- Cloud-deployed API for widespread accessibility
- Mobile-responsive design

## Technical Architecture

### Model Development
- **Dataset:**
    - Total Images: 4,500
    - Classes: 3 (Early Blight, Late Blight, Healthy)
    - Distribution:
        - Training: 80% (3,600 images)
        - Validation: 10% (450 images)
        - Testing: 10% (450 images)

- **Model Architecture:**
    - Base Model: VGG19 (pre-trained)
    - Configuration:
        - Top layers removed
        - Base layers frozen
        - Custom classification head added
    - Batch Size: 32
    - Training Epochs: 20

### Implementation Stack
- **Frontend:**
    - React.js
    - Material-UI/Tailwind (for styling)
    - Axios (for API communication)

- **Backend:**
    - FastAPI
    - Python 3.8+
    - TensorFlow/Keras

- **Deployment:**
    - Google Cloud Platform (GCP)
    - Docker containerization
    - Cloud Run for serverless deployment

## Performance Metrics
![Training vs Validation Performance](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/6c6ffd45-2303-488c-80f2-8699c3529087)

The model demonstrates robust performance with:
- High accuracy in disease classification
- Low false positive rate
- Real-time processing capability

## Interface Screenshots
### Disease Detection Interface
![Frontend View](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/5e2dec56-d869-4c5c-af82-03cab8317528)

### Results Display
![Results Interface](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/4cf199fc-436b-4fed-b98b-1eeacc69f1ee)

## Deployment Details
The system is deployed on Google Cloud Platform for scalability and accessibility:
![GCP Deployment Logs](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/6dc2d6bf-e033-4409-8eb0-139b507a199f)

## Installation and Setup

### Prerequisites
```bash
- Python 3.8+
- Node.js 14+
- Git
```

### Local Development Setup
1. Clone the repository:
```bash
git clone https://github.com/fosetorico/tomato_disease_detection.git
cd tomato_disease_detection
```

2. Backend setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

3. Frontend setup:
```bash
cd frontend
npm install
npm start
```

## API Documentation
The API provides the following endpoints:

- `POST /predict`
    - Accepts image file for disease detection
    - Returns prediction results with confidence scores

- `GET /health`
    - System health check endpoint
    - Returns service status

## Future Enhancements
- Integration with mobile applications
- Support for additional tomato diseases
- Offline mode capability
- Multi-language support for Nigerian farmers
- Integration with weather data for predictive analytics

## Contributing
We welcome contributions! Please see our contributing guidelines for more details.
