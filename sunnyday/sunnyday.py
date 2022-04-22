import requests

api_key = '2a18e135bd7110b4eb8f7cc5b4e6f7dd'


class Weather:
    """
    The weather class uses the openweathermap.org to retrieve the forecasted
    weather in a location using either city name or latitude and longitude.

    Package Use Example:
    #create a weather object using an openweathermap api key and city name
    #API key may not work, one is available from openweathermap.org

    weather1 = Weather(apikey="2a18e135bd7110b4eb8f7cc5b4e6f7dd", city='Madrid')

    #using a latitute and longitude
    weather1 = Weather(apikey="2a18e135bd7110b4eb8f7cc5b4e6f7dd", lat_lon=(41.1, -4.1)

    #return complete weather data for the next 12 hours
    weather1.next_12h()

    #return simplified weather data for the next 12 hours
    weather1.next_12h_simplified()

    Methods defined here:
    __init__(self, apikey, city: str=None, lat_lon:tuple=None)
        initialize self

    next_12h(self)
        returns 12 hour forecast in 3 hour increments
    next_12h_simplified()
    __________________________________________________________________________
    data descriptors defined here:
    __dict__
        dictionary for instance variables

    """
    def __init__(self, apikey, city: str = None, lat_lon: tuple = None):
        self.apikey = apikey
        self.city = city
        self.lat_lon = lat_lon

        base_url = "https://api.openweathermap.org/data/2.5/forecast?"
        if self.city:
            base_url += "q={}".format(self.city)
        elif lat_lon:
            base_url += f"lat={self.lat_lon[0]}&lon={self.lat_lon[1]}"
        else:
            raise TypeError("object instantiation requires a city, or lat/lon attribute")

        base_url += f"&appid={self.apikey}&units=imperial"
        r = requests.get(base_url)
        self.forecast = r.json()

        if self.forecast['cod'] != '200':
            raise ValueError(f"http Response object yields: {self.forecast['cod']}, {self.forecast['message']}")

    def next_12h(self):
        """
        Returns weather forecast for the next 12 hours in 3 hour increments
        :return: dict
        """
        return self.forecast['list'][:4]

    def next_12h_simplified(self):
        """
        Returns simplified weather forecast for the next 12 hours in 3 hour increments
        :return: str
        """
        output_string = ""
        for i in range(0, 4):
            # print(self.forecast['list'][i])
            output_string += f"Time: {self.forecast['list'][i]['dt_txt']}, Temperature: {self.forecast['list'][i]['main']['temp']}F " \
                             f"Weather: {self.forecast['list'][i]['weather'][0]['description']}\n"
        return output_string


if __name__ == '__main__':
    forecast = Weather(api_key, 'Chumbawumba')
    # print(forecast.next_12h())
    # forecast.next_12h_simplified()
    print(forecast.next_12h_simplified())
