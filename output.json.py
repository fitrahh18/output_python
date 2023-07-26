import json

def generate_big_bang_array():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("BIGBANG")
        elif num % 3 == 0:
            result.append("BIG")
        elif num % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(num))
    return result

def save_to_json(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    big_bang_array = generate_big_bang_array()
    save_to_json('output.json', big_bang_array)
    print("Array generated and saved to 'output.json'.")
