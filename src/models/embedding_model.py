from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

def create_embedding_model():
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224,224,3)
    )

    base_model.trainable = False

    x = base_model.output
    x = layers.GlobalAveragePooling2D()(x)

    model = models.Model(inputs=base_model.input, outputs=x)

    return model