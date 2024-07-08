document.addEventListener('DOMContentLoaded', () => {
    console.log("Script loaded and DOM fully loaded");

    let explanationElement = document.querySelector('.responsive-text');
    if (explanationElement) {
        console.log("Element found:", explanationElement);

        let explanationText = explanationElement.innerHTML;
        console.log("Original text:", explanationText);

        let paragraphs = explanationText.split('<br>');
        console.log("Split paragraphs:", paragraphs);

        // Clear the existing content
        explanationElement.innerHTML = '';

        // Append new paragraphs
        paragraphs.forEach(paragraphText => {
            let p = document.createElement('p');
            p.innerHTML = paragraphText.trim();
            explanationElement.appendChild(p);
        });

        console.log("Updated HTML:", explanationElement.innerHTML);
    } else {
        console.log("Element not found");
    }
});
