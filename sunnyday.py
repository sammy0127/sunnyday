import requests

api_key = '2a18e135bd7110b4eb8f7cc5b4e6f7dd'


class Weather:
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

        base_url += "&appid={}&units=imperial".format(self.apikey)
        r = requests.get(base_url)
        self.forecast = r.json()

        if self.forecast['cod'] == '404':
            raise LookupError("api response returned no data, city or lat/long values return no result")

    def next_12h(self):
        return self.forecast['list'][:4]

    def next_12h_simplified(self):
        output_string = ""
        for i in range(0, 4):
            # print(self.forecast['list'][i])
            output_string += f"Time: {self.forecast['list'][i]['dt_txt']}, Temperature: {self.forecast['list'][i]['main']['temp']}F " \
                             f"Weather: {self.forecast['list'][i]['weather'][0]['description']}\n"
        return output_string


if __name__ == '__main__':
    forecast = Weather(api_key, 'Nashville')
    # print(forecast.next_12h())
    # forecast.next_12h_simplified()
    print(forecast.next_12h_simplified())
