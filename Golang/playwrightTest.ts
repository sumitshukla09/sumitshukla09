import { chromium } from 'playwright';

(async () => {
    // Launch browser
    const browser = await chromium.launch({ headless: false }); // `headless: false` will show the browser window
    const page = await browser.newPage();

    // Go to a website
    await page.goto('https://example.com');

    // Take a screenshot
    await page.screenshot({ path: 'example.png' });

    console.log('Screenshot taken successfully.');

    // Close the browser
    await browser.close();
})();
