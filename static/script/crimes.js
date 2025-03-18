document.addEventListener("DOMContentLoaded", function () {
    const neighborhoodSelect = document.getElementById("neighborhood");
    const crimesTableBody = document.querySelector("#crimes-table tbody");

    // Fetch and display initial crime data
    fetchCrimes();

    // Fetch and populate neighborhoods
    fetch("/api/neighborhoods")
        .then(response => response.json())
        .then(data => {
            data.forEach(neighborhood => {
                const option = document.createElement("option");
                option.value = neighborhood.id;
                option.textContent = neighborhood.name;
                neighborhoodSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching neighborhoods:", error));

    // Add event listener for neighborhood filter
    neighborhoodSelect.addEventListener("change", function () {
        fetchCrimes(this.value);
    });

    // Function to fetch crimes
    function fetchCrimes(neighborhood = "") {
        fetch(`/api/crimes?neighborhood=${neighborhood}`)
            .then(response => response.json())
            .then(data => {
                // Clear the table
                crimesTableBody.innerHTML = "";

                // Populate the table
                data.forEach(crime => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${new Date(crime.date).toLocaleString()}</td>
                        <td>${crime.primary_type}</td>
                        <td>${crime.description}</td>
                        <td>${crime.block}</td>
                    `;
                    crimesTableBody.appendChild(row);
                });
            })
            .catch(error => console.error("Error fetching crimes:", error));
    }

    // Optional: Add D3.js chart here
});