from src.recorder import camera, screen_tools
from src.ai.model import AIModelController
from src.adapters import adapt_image
from os import getcwd

model_controller = AIModelController()
model = model_controller.create_model()
model_controller.compile_model(model)
model.load_weights(getcwd() + r'\checkpoints\first.ckpt').expect_partial()


camera_controller = camera.CameraController()
video_capture = camera_controller.record_camera(0)
photo = None

counter = 0
result = ""

while True:
    is_recording, frame = camera_controller.read_frame(video_capture)

    if not is_recording:
        break

    if photo is not None and counter == 10:
        counter = 0
        photo_adapted = adapt_image(photo)
        ai_result = model.predict(photo_adapted)
        print(ai_result)
        result = 'Botella de plastico' if ai_result > 0.5 else "Comida rápida"
        print(result)

    counter += 1

    frame_with_square = screen_tools.place_square_at_center(
        frame, 350)

    frame_with_text = screen_tools.put_text(frame, result)
    camera_controller.show_frame('Camara', frame_with_text)

    photo = screen_tools.take_pixels_from_square(frame, 350)

    pressed_key = camera_controller.wait_key()
    if pressed_key == ord('e'):
        break
