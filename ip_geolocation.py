import socket
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.geocoders import Nominatim

def ip_details(ip: str):
    res = DbIpCity.get(ip, api_key="free")
    geolocator = Nominatim(user_agent="OhShint!")
    address = geolocator.reverse(f"{res.latitude}, {res.longitude}")
    details = f"""IP Address: {res.ip_address}
Location: {res.city}, {res.region}, {res.country}
Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})
Address: {address}"""
    return details


def url2ip(url: str = "") -> str:
    ip_add = socket.gethostbyname(url)
    return ip_add


if __name__ == "__main__":
    ip = url2ip("www.youtube.com")
    print(ip)
    print(ip_details(ip))


