import folium
import geocoder

from django.views.generic import CreateView


class DataMixin(CreateView):
    def get_address_map(self, name_place):
        if name_place is None:
            get_map = folium.Map(zoom_start=2)
            map_html = get_map._repr_html_()
            return map_html

        address = name_place
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
        country = location.country
        if lat == None or lng == None:
            return None

        # Create Map Object
        get_map = folium.Map(location=[19, -12], zoom_start=2)
        folium.Marker([lat, lng], tooltip='Click for more',
                      popup=country).add_to(get_map)
        # Get HTML Representation of Map Object
        map_html = get_map._repr_html_()
        return map_html
