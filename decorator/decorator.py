from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        print(f"Writing data {data}  to file {self.filename}")

    def read_data(self):
        print('Reading data from file', self.filename)


# base decorator
class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self.wrappee = source

    def write_data(self, data):
        self.wrappee.write_data(data)

    def read_data(self):
        self.wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource):
        super().__init__(source)

    def write_data(self, data):
        self.wrappee.write_data('encrypt' + '_' + data)

    def read_data(self):
        self.wrappee.read_data()


class CompressionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource):
        super().__init__(source)

    def write_data(self, data):
        self.wrappee.write_data('compress' + '_' + data)

    def read_data(self):
        self.wrappee.read_data()


if __name__ == '__main__':
    source = FileDataSource('filename.txt')
    # source.write_data('test_data')
    #
    source = CompressionDecorator(source)
    source.write_data('test_data')

    print(dir(source))

    source = EncryptionDecorator(source)
    source.write_data('test_data')