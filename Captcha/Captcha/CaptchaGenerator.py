import numpy as np
import cv2
from random import randint, uniform
import base64

W = 80
H = 80

VERTICAL_LAYER = 2
HORIZONTAL_LAYER = 3

font = cv2.FONT_ITALIC

INPUT_CHOICES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Captcha:

    def generate_captcha(self):
        try:
            GENERATED_CHOICES = []
            ans = ""
            root_layer = np.full((H * VERTICAL_LAYER, W * HORIZONTAL_LAYER, 3), fill_value=[255, 255, 255],
                                 dtype=np.uint8)

            for x in range(VERTICAL_LAYER):
                for y in range(HORIZONTAL_LAYER):
                    R, G, B = randint(0, 255), randint(0, 255), randint(0, 255)

                    generated_index = randint(0, len(INPUT_CHOICES) - 1)
                    gi = 0
                    while generated_index in GENERATED_CHOICES and gi < len(INPUT_CHOICES):
                        generated_index = randint(0, len(INPUT_CHOICES) - 1)
                        gi += 1

                    GENERATED_CHOICES.append(generated_index)
                    input_text = INPUT_CHOICES[generated_index]
                    ans += input_text

                    temp_image = np.full((H, W, 3), fill_value=[R, G, B], dtype=np.uint8)
                    font_scale = uniform(1.2, 2.0)
                    cv2.putText(temp_image, str(input_text), (10, 55), font, font_scale, (255 - R, 255 - G, 255 - B), 4)

                    if randint(2, 9) % 3 == 0 and (255 - R, 255 - G, 255 - B) != (0, 0, 0):
                        kernel = np.ones((2, 2), np.uint8)
                        temp_image = cv2.morphologyEx(temp_image, cv2.MORPH_GRADIENT, kernel)

                    root_layer[x * H:(x + 1) * H, y * W:(y + 1) * W] = temp_image

            r, buffer = cv2.imencode('.jpg', root_layer)
            return {"data": 'data:image/jpeg;base64, ' + base64.b64encode(buffer).decode(), "answer": ans }


        except Exception as e:
            return "Exception as {}".format(e)
