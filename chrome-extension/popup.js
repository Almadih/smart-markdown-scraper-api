document.addEventListener("DOMContentLoaded", () => {
  const apiKeyInput = document.getElementById("apiKey");
  const btnScrape = document.getElementById("btnScrape");
  const statusDiv = document.getElementById("status");

  // Load saved key
  chrome.storage.local.get(["rapidapiKey"], (res) => {
    if (res.rapidapiKey) apiKeyInput.value = res.rapidapiKey;
  });

  btnScrape.addEventListener("click", async () => {
    const key = apiKeyInput.value.trim();
    if (!key) {
      statusDiv.textContent = "❌ Please enter your RapidAPI key.";
      return;
    }
    chrome.storage.local.set({ rapidapiKey: key });

    statusDiv.textContent = "⏳ Scraping & converting page...";

    // Get active tab URL
    chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
      const targetUrl = tabs[0]?.url;
      if (!targetUrl) {
        statusDiv.textContent = "❌ Could not retrieve active tab URL.";
        return;
      }

      try {
        const response = await fetch("https://smart-markdown-web-scraper.p.rapidapi.com/scrape", {
          method: "POST",
          headers: {
            "x-rapidapi-key": key,
            "x-rapidapi-host": "smart-markdown-web-scraper.p.rapidapi.com",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ url: targetUrl })
        });

        if (!response.ok) throw new Error(`Status ${response.status}`);
        const data = await response.json();
        const markdown = data.markdown || JSON.stringify(data);

        await navigator.clipboard.writeText(markdown);
        statusDiv.textContent = "✅ Clean Markdown copied to clipboard!";
      } catch (err) {
        statusDiv.textContent = `❌ Scraping failed: ${err.message}`;
      }
    });
  });
});
