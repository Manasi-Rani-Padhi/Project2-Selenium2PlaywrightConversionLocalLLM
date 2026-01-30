from tools.ollama_client import OllamaClient
import os

class Converter:
    def __init__(self, model="qwen2:0.5b"):
        self.client = OllamaClient(model=model)

    def convert(self, source_code, target_lang="typescript", framework="testng"):
        """
        Orchestrates the conversion process.
        """
        if not source_code.strip():
            return "Error: No source code provided."

        # Logic for conversion
        converted_code = self.client.generate_conversion(source_code, target_lang)
        
        # Post-processing can be added here (e.g., formatting, additional validation)
        return converted_code

if __name__ == "__main__":
    # Test conversion
    converter = Converter()
    test_code = """
    @Test
    public void simpleTest() {
        driver.get("https://example.com");
    }
    """
    print(f"Converted Code:\n{converter.convert(test_code)}")
