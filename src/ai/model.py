import tensorflow as tf
import tensorflow_hub as tfhub


class AIModelController:
    def create_model(self):
        url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
        mobilenetv2 = tfhub.KerasLayer(url, input_shape=(224, 224, 3))
        mobilenetv2.trainable = False

        model = tf.keras.Sequential(
            [mobilenetv2, tf.keras.layers.Dense(1, activation="sigmoid")]
        )

        model.summary()
        return model

    def compile_model(self, model):
        model.compile(
            optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
        )
