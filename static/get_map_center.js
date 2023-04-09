// get_map_center.js

function getMapCenter() {
    const map = document.querySelector("deckgl-mapbox").deck.getMapboxMap();
    const center = map.getCenter();
    const lat = center.lat;
    const lng = center.lng;
    return { lat, lng };
}

getMapCenter();
