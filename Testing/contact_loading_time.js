const { webkit } = require('playwright');

(async () => {
  const browser = await webkit.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // Navigate to your PWA
  await page.goto('http://d3n19dccznxr2d.cloudfront.net');

  // Measure performance
  const startTime = new Date();
  await page.click('[data-testid="duplicateContactsButton"]');
  const endTime = new Date();
  const duration = endTime - startTime; // duration will hold the time it took to execute the duplicateContacts function

  console.log(`Duplicate contacts operation took ${duration} milliseconds.`);

  // Validate the operation
  // This part depends on the way your app updates the DOM after adding contacts
  // Replace it with the actual way to validate the operation in your app
  const contactItems = await page.$$('.contactItem');
  console.log(`Number of contacts after duplication: ${contactItems.length}`);

  // Close the browser
  await browser.close();
})();
