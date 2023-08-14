// cytometry/static/js/update_plots.js

const updatePlots = async () => {
    const file_id = getSessionData('file_id'); // Replace with your method to retrieve file_id
    const plotTypes = ['histogram', 'dot', 'density', 'time'];

    for (const plotType of plotTypes) {
        const response = await fetch(`/plot_${plotType}/${file_id}/`);
        const plotContainer = document.getElementById(`${plotType}-plot`);
        plotContainer.innerHTML = `<img src="${response.url}" alt="${plotType} plot">`;
    }
};

document.getElementById('file-input').addEventListener('change', updatePlots);