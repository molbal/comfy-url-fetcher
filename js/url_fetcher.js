import { app } from "../../../scripts/app.js";
import { api } from "../../../scripts/api.js";

app.registerExtension({
    name: "example.url_fetcher",
    async setup() {
        function messageHandler(event) {
            console.log('URL Fetcher event', event.detail.message);
        }
        api.addEventListener("url_fetcher.message", messageHandler);
    },
});