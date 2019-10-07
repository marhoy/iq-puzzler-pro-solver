from dataclasses import dataclass
import numpy as np


@dataclass
class Piece:

    def __init__(self, data):
        self.variants = Piece._create_variants(data)

    @classmethod
    def _create_variants(cls, data):
        variants = []
        for piece in [data, np.fliplr(data)]:
            for k in range(4):
                candidate = np.rot90(piece, k)
                for existing in variants:
                    if np.array_equal(existing, candidate):
                        break  # candidate is equal to existing
                else:
                    variants.append(candidate)
        return variants


def pink(value=1):
    piece = np.zeros((4, 2), dtype=np.uint8)
    piece[:2, 0] = value
    piece[1:, 1] = value
    return Piece(piece)


def red(value=2):
    piece = np.zeros((4, 2), dtype=np.uint8)
    piece[0, 0] = value
    piece[:, 1] = value
    return Piece(piece)


def dark_red(value=3):
    piece = np.zeros((3, 2), dtype=np.uint8)
    piece[:2, 0] = value
    piece[1:, 1] = value
    return Piece(piece)


def blue(value=4):
    piece = np.zeros((3, 3), dtype=np.uint8)
    piece[:, 0] = value
    piece[-1, :] = value
    return Piece(piece)


def light_blue(value=5):
    piece = np.zeros((2, 2), dtype=np.uint8)
    piece[:, 0] = value
    piece[-1, :] = value
    return Piece(piece)


def dark_blue(value=6):
    piece = np.zeros((2, 3), dtype=np.uint8)
    piece[0, :] = value
    piece[1, 0] = value
    return Piece(piece)


def green(value=7):
    piece = np.zeros((2, 3), dtype=np.uint8)
    piece[0, :] = value
    piece[1, [0, 2]] = value
    return Piece(piece)


def light_green(value=8):
    piece = np.zeros((2, 3), dtype=np.uint8)
    piece[0, :2] = value
    piece[1, :] = value
    return Piece(piece)


def dark_green(value=9):
    piece = np.zeros((3, 2), dtype=np.uint8)
    piece[:, 0] = value
    piece[1, 1] = value
    return Piece(piece)


def purple(value=10):
    piece = np.zeros((3, 3), dtype=np.uint8)
    piece[0, 0] = value
    piece[1, :2] = value
    piece[2, 1:] = value
    return Piece(piece)


def yellow(value=11):
    piece = np.zeros((2, 4), dtype=np.uint8)
    piece[0, :] = value
    piece[1, 2] = value
    return Piece(piece)


def orange(value=12):
    piece = np.zeros((3, 3), dtype=np.uint8)
    piece[0, 1] = value
    piece[1, :2] = value
    piece[2, 1:] = value
    return Piece(piece)
