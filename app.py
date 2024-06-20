import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Load the pre-trained object detection model from TensorFlow Hub
model = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")

# Function to perform object detection
def detect_objects(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (320, 320))
    image_np = np.expand_dims(image_resized, axis=0)
    
    results = model(image_np)
    
    detection_scores = results['detection_scores'][0].numpy()
    detection_classes = results['detection_classes'][0].numpy().astype(int)
    detection_boxes = results['detection_boxes'][0].numpy()

    for i in range(len(detection_scores)):
        if detection_scores[i] > 0.5:
            ymin, xmin, ymax, xmax = detection_boxes[i]
            (left, right, top, bottom) = (xmin * image.shape[1], xmax * image.shape[1],
                                          ymin * image.shape[0], ymax * image.shape[0])
            cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)
            cv2.putText(image, f'{detection_classes[i]}: {detection_scores[i]:.2f}', (int(left), int(top) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'path/to/your/image.jpg'
    detect_objects(image_path)

