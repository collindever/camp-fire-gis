var map = L.map('map').setView([39.77,-121.55],12);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.light',
    accessToken: 'pk.eyJ1IjoiY29sbGluZGV2ZXIiLCJhIjoiY2pqbDF1OWM4MDMzODNwczM4Y2RjbGRodSJ9.yZGZgHkkPnbCSVBUE2IhbA'
}).addTo(map);

// L.geoJson(CAMP1111, {style: styleRecent}).addTo(map);
// L.geoJson(CAMP1110, {style: stylePast}).addTo(map);
// L.geoJson(CAMP1109, {style: stylePast}).addTo(map);
// L.geoJson(CAMP1108, {style: stylePast}).addTo(map);
L.geoJson(LANDSATIR1108, {style: stylePast}).addTo(map);


function styleRecent(feature) {
    return {
        fillColor: '#BD0026',
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

function stylePast(feature) {
    return {
        fillColor: 'red',
        weight: 1,
        opacity: 1,
        color: '#fdffc2',
        fillOpacity: 0.1
    };
}