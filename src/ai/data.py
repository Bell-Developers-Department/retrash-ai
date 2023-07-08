from tensorflow.keras.preprocessing.image import ImageDataGenerator


class AIDataController:
    def get_data(self, images_folder_path):
        data_generator = ImageDataGenerator(
            rescale=1.0 / 255,
            rotation_range=30,
            width_shift_range=0.25,
            height_shift_range=0.25,
            shear_range=15,
            zoom_range=[0.5, 1.5],
            validation_split=0.2,
        )

        training_data = data_generator.flow_from_directory(
            images_folder_path,
            target_size=(224, 224),
            batch_size=32,
            subset="training",
            class_mode="binary",
        )

        testing_data = data_generator.flow_from_directory(
            images_folder_path,
            target_size=(224, 224),
            batch_size=32,
            shuffle=True,
            subset="validation",
            class_mode="binary",
        )

        print(training_data.class_indices)

        return [training_data, testing_data]
