import json


def main():
    with open("./data/patientData0.json") as f:
        data = json.load(f)
        print(f"Carl's name: {data['patient'][0]['name']}")


if __name__ == '__main__':
    main()
