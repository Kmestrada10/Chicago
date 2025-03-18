function createBubbleChart(regionData) {
    // Set up the SVG canvas
    const width = 800;
    const height = 600;
    const svg = d3.select("#bubble-chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    // Create a scale for bubble sizes
    const maxCount = d3.max(regionData, d => d.count);
    const radiusScale = d3.scaleSqrt()
        .domain([0, maxCount])
        .range([10, 50]);

    // Create a force simulation
    const simulation = d3.forceSimulation(regionData)
        .force("charge", d3.forceManyBody().strength(5))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("collision", d3.forceCollide().radius(d => radiusScale(d.count) + 2));

    // Draw bubbles
    const bubbles = svg.selectAll("circle")
        .data(regionData)
        .enter()
        .append("circle")
        .attr("r", d => radiusScale(d.count))
        .attr("fill", "steelblue")
        .attr("stroke", "black")
        .attr("stroke-width", 1);

    // Add labels
    const labels = svg.selectAll("text")
        .data(regionData)
        .enter()
        .append("text")
        .text(d => `${d.region}: ${d.count}`)
        .attr("text-anchor", "middle")
        .attr("font-size", "12px")
        .attr("fill", "white");

    // Update bubble and label positions
    simulation.on("tick", () => {
        bubbles
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        labels
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    });
}