from playwright.sync_api import expect


class DataSourcePage:
    def __init__(self, page):
        self.page = page


    def filter_data_source(self, name):
        self.page.get_by_placeholder("Filter by name or type").fill(name)

    def select_test_data(self):
        self.page.get_by_role("button").get_by_text("TestData").click()

    def save_and_test(self):
        self.page.get_by_role("button").get_by_text("Save & test").click()

    def build_dashboard(self):
        self.page.locator(".css-1riaxdn").get_by_text("Build a dashboard").click()

    def add_visualization_to_datasource(self):
        self.page.locator(".css-1riaxdn").filter(has_text="Add visualization").click()

    def select_grafana_test_data(self):
        self.page.locator(".css-1pwf3hg").filter(has_text="grafana-testdata-datasource").nth(0).click()

    def select_scenario(self):
        self.page.locator(".css-v249xx").get_by_text("Scenario").click()

    def select_csv_content(self):
        self.page.locator(".css-1i88p6p").nth(0).click()
        self.page.locator(".css-h2c6cn-grafana-select-option").get_by_text("CSV Content").click()

    def click_on_view_lines(self):
        self.page.locator("//div[@class='view-lines monaco-mouse-cursor-text']").click()

    def enter_csv_data(self, csv_data):
        # Add the header
        self.page.locator("//div[@class='view-lines monaco-mouse-cursor-text']").type("time,value")
        self.page.wait_for_timeout(500)
        self.page.locator("//div[@class='view-lines monaco-mouse-cursor-text']").press("Enter")

        # Loop through csv_data and enter each row
        for timing, value in csv_data:
            self.page.locator("//div[@class='view-lines monaco-mouse-cursor-text']").type(f"{timing},{value}")
            self.page.locator("//div[@class='view-lines monaco-mouse-cursor-text']").press("Enter")
            self.page.wait_for_timeout(500)

        # Wait a bit more after entering all data
        self.page.wait_for_timeout(1000)

    def verify_data_entry(self):
        expect(self.page.locator("//div[@class='view-lines monaco-mouse-cursor-text']")).to_contain_text("2024-03-25T12:00:00Z,20", timeout=5000)

    def refresh_dashboard(self):
        """Clicks the Refresh button to update the dashboard."""
        print("Ensuring data is saved...")
        self.page.get_by_role("button").get_by_text("Refresh").click()

    def zoom_to_data(self):
        """Clicks the Zoom to Data button."""
        self.page.locator(".css-1riaxdn").get_by_text("Zoom to data").click()

    def capture_screenshot(self, screenshot_path="current_visualization.png"):
        """Captures a screenshot of the visualization."""
        self.page.locator(".css-itdw1b-panel-container").screenshot(path=screenshot_path)
        return screenshot_path
