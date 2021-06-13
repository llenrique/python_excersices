from typing import Collection


def run():
    collection = {
        "key1": 1,
        "key2": 2,
        "key3": 3
    }

    for k, v in collection.items():
        print(k + '->' + '{}'.format(v))


if __name__ == '__main__':
    run()