from tensorflow.keras.preprocessing.image import ImageDataGenerator

class TrainingService:
    def __init__(self, data_path):
        self.data_path = data_path

    def get_data_generators(self):
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            validation_split=0.2,

            # AUGMENTATION
            rotation_range=25,
            zoom_range=0.25,
            width_shift_range=0.1,
            height_shift_range=0.1,
            horizontal_flip=True,
            brightness_range=[0.8, 1.2]
        )

        # validation → augmentation YOk 
        val_datagen = ImageDataGenerator(
            rescale=1./255,
            validation_split=0.2
        )

        train_generator = train_datagen.flow_from_directory(
            self.data_path,
            target_size=(224, 224),
            batch_size=16,
            class_mode='sparse',
            subset='training',
            shuffle=True
        )

        val_generator = val_datagen.flow_from_directory(
            self.data_path,
            target_size=(224, 224),
            batch_size=16,
            class_mode='sparse',
            subset='validation',
            shuffle=False
        )

        return train_generator, val_generator