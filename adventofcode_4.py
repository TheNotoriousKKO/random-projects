def read_char_array():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        char_array = [list(line.strip()) for line in lines]
    return char_array

def wordsearch():
    char_array = read_char_array()
    rows = len(char_array)
    cols = len(char_array[0]) if rows > 0 else 0
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    word = "XMAS"
    word_length = len(word)
    count = 0

    def check_direction(x, y, dx, dy):
        for i in range(1, word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or char_array[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            if char_array[x][y] == word[0]:
                for dx, dy in directions:
                    if check_direction(x, y, dx, dy):
                        count += 1
    print("Instances: ", count)
    return count

def count_crossing_mas_pairs():
    char_array = read_char_array()
    rows = len(char_array)
    cols = len(char_array[0]) if rows > 0 else 0
    count = 0
    diagonal_directions = [
        (-1, 1), (-1, -1), (1, 1), (1, -1)
    ]
    for x in range(rows):
        for y in range(cols):
            if char_array[x][y] == 'A':
                diagonal_letters = []
                for dx, dy in diagonal_directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        diagonal_letters.append((char_array[nx][ny], (dx, dy)))
                m_positions = [direction for letter, direction in diagonal_letters if letter == 'M']
                s_positions = [direction for letter, direction in diagonal_letters if letter == 'S']
                if len(m_positions) == 2 and len(s_positions) == 2:
                    if not ((m_positions[0] == (-1, -1) and m_positions[1] == (1, 1)) or
                            (m_positions[0] == (-1, 1) and m_positions[1] == (1, -1))):
                        count += 1
    print("Pairs: ", count)
    return count

if __name__ == "__main__":
    wordsearch()
    count_crossing_mas_pairs()
