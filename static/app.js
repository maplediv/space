document.addEventListener('DOMContentLoaded', () => {
    console.log("Script loaded and DOM fully loaded");

    const loadingMessage = document.getElementById('loadingMessage');
    const galacticCenterContainer = document.getElementById('galacticCenterContainer');

    // Show loading message and hide the main content initially
    loadingMessage.style.display = 'block';
    galacticCenterContainer.style.display = 'none';

    // Simulate a data loading delay
    setTimeout(() => {
        // This simulates data fetching; remove this if data is rendered server-side
        loadingMessage.style.display = 'none';
        galacticCenterContainer.style.display = 'block';
    }, 2000); // 2 seconds delay, adjust if needed
});
