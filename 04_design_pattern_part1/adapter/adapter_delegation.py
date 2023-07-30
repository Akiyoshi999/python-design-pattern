from abc import ABCMeta, abstractclassmethod


class Target(metaclass=ABCMeta):
    @abstractclassmethod
    def get_csv_data(self) -> str:
        pass


class NewLibraly():
    def get_json_data(self) -> list[dict[str, str]]:
        return [
            {
                "data1": "json_dataA",
                "data2": "json_dataB"
            },
            {
                "data1": "json_dataC",
                "data2": "json_dataD"
            }
        ]


class jsonToCsvAdapter(Target):
    def __init__(self, adaptee: NewLibraly):
        self.__adaptee = adaptee

    def get_csv_data(self) -> str:
        json_data = self.__adaptee.get_json_data()
        header = ",".join(list(json_data[0].keys())) + "\n"
        body = "\n".join([",".join(list(d.values())) for d in json_data])

        return header + body


if __name__ == "__main__":
    adaptee = NewLibraly()
    print("=== Adapteeが提供するデータ ===")
    print(adaptee.get_json_data())

    print("")

    adapter = jsonToCsvAdapter(adaptee)
    print("=== Adapterに変換されたデータ ===")
    print(adapter.get_csv_data())
