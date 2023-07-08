from model import AIModelController
from data import AIDataController
from os import getcwd, path


model_controller = AIModelController()
model = model_controller.create_model()
model_controller.compile_model(model)

checkpoint_path = getcwd() + r"\checkpoints\my_checkpoint"
if path.isfile(checkpoint_path) == True:
    model.load_weights(checkpoint_path)


data_controller = AIDataController()
training_data, testing_data = data_controller.get_data(
    getcwd() + r"\dataset\images\binary"
)


history = model.fit(
    training_data, epochs=6, batch_size=32, validation_data=testing_data
)

model.save_weights(getcwd() + r"\checkpoints\my_checkpoint")
