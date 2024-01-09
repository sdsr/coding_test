N, r, c = map(int, input().split())


def z_search(n, r, c):
    # Base case: 1x1 grid
    if n == 0:
        return 0

    # Half size of the current grid
    half = 2 ** (n - 1)

    # First quadrant
    if r < half and c < half:
        return z_search(n - 1, r, c)

    # Second quadrant
    if r < half and c >= half:
        return half * half + z_search(n - 1, r, c - half)

    # Third quadrant
    if r >= half and c < half:
        return 2 * half * half + z_search(n - 1, r - half, c)

    # Fourth quadrant
    return 3 * half * half + z_search(n - 1, r - half, c - half)


def main():
    global N, r, c
    print(z_search(N, r, c))


main()
