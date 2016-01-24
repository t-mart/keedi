from os import path

import numpy as np


class Keyboard:
    def __init__(self, name, image_path, coord_map):
        self.name = name
        self.image_path = image_path
        self.coord_map = coord_map
        assert path.exists(image_path)
        assert path.isfile(image_path)

    @classmethod
    def create_coord_map_for_rows(cls, q_coord, a_coord, z_coord,
                                  width_btwn_keys):
        """Return a dict mapping characters to coordinates (for a particular
        image of a keyboard).

        All coordinates and distances should correspond to the pixel coordinates
        of a keyboard image that will be used to define a Keyboard object.

        This method takes advantage of 2 fairly common qualities of keyboards:
        * each rows' keys have a fixed Y-coordinate.
        * the width between adjacent keys is fixed.
        From these assumptions, we can reasonably generate the complete
        coordinate map of all 26 keys from just a few data points.

        q_coord is the X, Y-coordinate 2-tuple of the 'q' key on the keyboard
        image. a_coord and z_coord are specified respectively.

        width_btwn_keys is the distance between the center of a key and it's
        left/right neighboring key.
        """
        rows = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ]

        coord_map = {}

        for row_chars, row_leader_key_coord in zip(rows, (q_coord, a_coord,
                                                          z_coord)):
            for i, row_char in enumerate(row_chars):
                x = row_leader_key_coord[0] + i * width_btwn_keys
                y = row_leader_key_coord[1]
                coord_map[row_char] = np.array([x, y])

        return coord_map


KEYBOARD_IMAGE_ROOT = path.join(path.abspath(path.dirname(__file__)),
                                'images')

KEYBOARDS = {}

# Google Keyboard
google_keyboard = Keyboard("google_keyboard",
                           path.join(KEYBOARD_IMAGE_ROOT,
                                     "google_keyboard.png"),
                           Keyboard.create_coord_map_for_rows(
                                   q_coord=(13, 41),
                                   a_coord=(26, 78),
                                   z_coord=(43, 115),
                                   width_btwn_keys=27)
                           )
KEYBOARDS[google_keyboard.name] = google_keyboard

if __name__ == '__main__':
    import pprint
    pprint.pprint(google_keyboard.coord_map)
