shot-scraper javascript 'https://www.google.com/search?q=$1' '() => {
    function findParentWithHveid(element) {
        while (element && !element.hasAttribute("data-hveid")) {
            element = element.parentElement;
        }
        return element;
    }
    return Array.from(
        document.querySelectorAll("h3"),
        el => findParentWithHveid(el).innerText
    );
}'