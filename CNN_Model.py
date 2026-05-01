import tensorflow as tf
from tensorflow.keras import layers, models, datasets

# Load Data
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Build a Stronger Model
model = models.Sequential([
    # Layer 1: Find basic edges & colors
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    
    # Layer 2: Find complex shapes (like wheels or hulls)
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    
    # Layer 3: Deep feature recognition
    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    
    layers.Flatten(),
    layers.Dropout(0.5), # This stops "lazy" guessing
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train for 10 epochs for better "study time"
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

model.save('cnn_model.h5')
print("Upgraded model saved successfully!")