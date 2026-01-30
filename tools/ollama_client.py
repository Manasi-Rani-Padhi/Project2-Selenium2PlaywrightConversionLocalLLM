import requests
import json
import os

class OllamaClient:
    def __init__(self, model="qwen2:0.5b", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = f"{base_url}/api/generate"

    def generate_conversion(self, source_code, target_lang="typescript"):
        system_prompt = f"""
        You are an expert test automation engineer specializing in Selenium Java and Playwright.
        Your task is to convert Selenium Java (TestNG) code into Playwright {target_lang}.
        
        Rules:
        1. Prioritize readability and idiomatic Playwright patterns.
        2. Use `await` for all asynchronous actions.
        3. Map TestNG annotations to Playwright test hooks (@Test -> test, @BeforeMethod -> test.beforeEach).
        4. Use locators: page.locator() is preferred over older selectors.
        5. Convert assertions to `expect(...)`.
        6. If you find complex logic, maintain the logic but adapt it to Playwright's style.
        7. Only return the code. Do not include explanations or markdown blocks in the actual code string if possible, or wrap them in comments.
        """
        
        prompt = f"{system_prompt}\n\nConvert this Selenium Java code:\n\n{source_code}\n\nPlaywright {target_lang} code:"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    client = OllamaClient()
    test_java = """
    @Test
    public void loginTest() {
        driver.get("https://example.com");
        driver.findElement(By.id("user")).sendKeys("admin");
        driver.findElement(By.id("pass")).sendKeys("123");
        driver.findElement(By.id("login")).click();
        Assert.assertEquals(driver.getTitle(), "Dashboard");
    }
    """
    print(client.generate_conversion(test_java))
