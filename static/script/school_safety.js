// Initialize the map
var map = L.map('map').setView([41.8781, -87.6298], 10); // Centered on Chicago

// Add a tile layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Add a marker for a school (example coordinates)
var schoolMarker = L.marker([41.8781, -87.6298]).addTo(map);
schoolMarker.bindPopup("<b>Example School</b><br>123 Main St, Chicago, IL").openPopup();