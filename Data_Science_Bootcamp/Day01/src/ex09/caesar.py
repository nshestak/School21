import sys

def caesar_cipher(text, shift, mode='encode'):
    if mode not in ['encode', 'decode']:
        raise ValueError("Mode must be 'encode' or 'decode'.")
    
    if mode == 'decode':
        shift = -shift

    result = []
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            raise ValueError('The script does not support your language yet.')
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        sys.exit('Error: Incorrect number of arguments. 3 arguments were expected: mode, text and shift.')    
    mode = sys.argv[1]
    text = sys.argv[2]

    try:
        shift = int(sys.argv[3])
    except ValueError:
        sys.exit('The shift must be an integer.')

    try:
        result = caesar_cipher(text, shift, mode)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()