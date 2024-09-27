"""CQ04 Importing + Scope Assignment"""

__author__ = "730811558"


def get_coords(xs: str, ys: str) -> None:
    """Prints formatted pairs of each character in the two input strings."""
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):
        while idx2 < len(ys):
            # prints first idx of xs and subsequent idxs of ys
            print("(" + xs[idx1] + "," + ys[idx2] + ")")
            idx2 += 1
        # after idx >= the lenght of ys, start over with idx += 1
        idx1 += 1
        idx2 = 0


if __name__ == "__main__":
    get_coords("hi", "bye")
