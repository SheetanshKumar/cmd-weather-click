import requests
import json
import click
import test
# city_name = input("Enter city name:")
#
# api_key = "f26179addbf7fcfdaa8d3915341ac169"
# url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,api_key)
# response = requests.get(url)
# print(json.dumps(response.json(),indent=4, sort_keys=True))
#

@click.group()
def cli():
     pass

@cli.command()
@click.argument('token', nargs=1)
def cityname(token):
    city_name = token
    api_key = "f26179addbf7fcfdaa8d3915341ac169"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    response = requests.get(url)
    print(json.dumps(response.json(), indent=4, sort_keys=True))

if __name__ == '__main__':
    cli(obj={})