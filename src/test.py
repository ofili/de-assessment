# access keys in dictionary
def keys(self):
    return self.keys()


def values(self):
    return self.values()


# return keys and values
def get_keys_and_values(self):
    ''' return keys and values '''
    return self.keys(), self.values()


# access nested keys
def nested_keys(self):
    return self.keys()[0].keys()


def __getitem__(self, key):
    return self.__getitem__(key)


def __setitem__(self, key, value):
    return self.__setitem__(key, value)


if __name__ == '__main__':
    print(keys(dict(name='John', age=42)))
    print(keys(dict(name='John', age=42, job='dev')))
    print(keys(dict(name='John', age=42, job='dev', city='SF')))
    print(keys(dict(name='John', age=42, job='dev', city='SF', country='US')))
    print(keys(dict(name='John', age=42, job='dev', city='SF', country='US', phone='555-1234')))
    print(keys(dict(name='John', age=42, job='dev', city='SF', country='US', phone='555-1234', address='123 Main St')))

    print(
        get_keys_and_values({
            "AF": "Africa",
            "AN": "Antarctica",
            "AS": "Asia",
            "EU": "Europe",
            "NA": "North America",
            "OC": "Oceania",
            "SA": "South America"
        })
    )
    print(
        values({
            "AF": "Africa",
            "AN": "Antarctica",
            "AS": "Asia",
            "EU": "Europe",
            "NA": "North America",
            "OC": "Oceania",
            "SA": "South America"
        })
    )
    print(__getitem__(dict(name='John', age=42), 'name'))
