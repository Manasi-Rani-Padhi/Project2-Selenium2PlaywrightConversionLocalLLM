# Findings & Research

## Project Discoveries
- Project started on 2026-01-31.
- Goal: Convert Selenium Java code to Playwright JS/TS.

## Constraints
- Potential use of Local LLM (Ollama) as per previous conversations.

## Conversion Mapping (Selenium Java -> Playwright JS/TS)

| Selenium (Java/TestNG) | Playwright (JS/TS) |
| :--- | :--- |
| `@Test` | `test('...', async ({ page }) => { ... })` |
| `@BeforeMethod` | `test.beforeEach(async ({ page }) => { ... })` |
| `@AfterMethod` | `test.afterEach(async ({ page }) => { ... })` |
| `driver.get(url)` | `await page.goto(url)` |
| `driver.findElement(By.id("id"))` | `page.locator('#id')` |
| `driver.findElement(By.name("n"))` | `page.locator('[name="n"]')` |
| `driver.findElement(By.xpath("x"))`| `page.locator('xpath=x')` |
| `element.sendKeys("text")` | `await element.fill("text")` |
| `element.click()` | `await element.click()` |
| `Assert.assertEquals(act, exp)` | `await expect(act).toBe(exp)` |
| `WebDriverWait` | Auto-waiting or `locator.waitFor()` |

## Key Concepts
- **Auto-waiting:** Playwright handles many waits automatically, reducing the need for explicit `WebDriverWait`.
- **Locators:** Use `locator()` for better resilience.
- **Async/Await:** All Playwright actions are asynchronous.
