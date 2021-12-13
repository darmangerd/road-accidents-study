import pandas as pd


class Acquisition:
    __df_caractersitics: pd.DataFrame
    __df_users: pd.DataFrame
    __df_places: pd.DataFrame
    __df_vehicles: pd.DataFrame

    def __init__(self):
        self.__df_caractersitics = pd.read_csv(
            'datas/caracteristics.csv', dtype={'long': str})
        self.__clean_caracteristics()
        self.__df_users = pd.read_csv('datas/users.csv')
        self.__clean_users()
        self.__df_places = pd.read_csv(
            'datas/places.csv', dtype='unicode')
        self.__clean_places()
        self.__df_vehicles = pd.read_csv('datas/vehicles.csv')
        self.__clean_vehicles()

    def get_accident_caracteristics(self, **kwargs):
        df = self.__df_caractersitics
        del_keys = []
        for i in kwargs.keys():
            if type(kwargs[i]) is list:
                df = df[df[i].isin(
                    kwargs[i])]
                del_keys.append(i)
        for i in del_keys:
            del kwargs[i]
        if len(kwargs.keys()) is not None:
            return df.loc[(df[list(kwargs)] == pd.Series(kwargs)).all(axis=1)]
        return df

    def get_places(self, **kwargs):
        df = self.__df_places
        del_keys = []
        for i in kwargs.keys():
            if type(kwargs[i]) is list:
                df = df[df[i].isin(
                    kwargs[i])]
                del_keys.append(i)
        for i in del_keys:
            del kwargs[i]
        if len(kwargs.keys()) is not None:
            return df.loc[(df[list(kwargs)] == pd.Series(kwargs)).all(axis=1)]
        return df

    def get_vehicles(self, vehicule_type=None):
        df = self.__df_vehicles
        del_keys = []
        for i in kwargs.keys():
            if type(kwargs[i]) is list:
                df = df[df[i].isin(
                    kwargs[i])]
                del_keys.append(i)
        for i in del_keys:
            del kwargs[i]
        if len(kwargs.keys()) is not None:
            return df.loc[(df[list(kwargs)] == pd.Series(kwargs)).all(axis=1)]
        return df

    def get_users(self, **kwargs):
        df = self.__df_users
        del_keys = []
        for i in kwargs.keys():
            if type(kwargs[i]) is list:
                df = df[df[i].isin(
                    kwargs[i])]
                del_keys.append(i)
        for i in del_keys:
            del kwargs[i]
        if len(kwargs.keys()) is not None:
            return df.loc[(df[list(kwargs)] == pd.Series(kwargs)).all(axis=1)]
        return df

    def __clean_caracteristics(self):
        self.__df_caractersitics = self.__df_caractersitics.dropna(
            subset=["lat", "long"])
        pass

    def __clean_places(self):
        pass

    def __clean_vehicles(self):
        pass

    def __clean_users(self):
        pass


if __name__ == '__main__':
    pass