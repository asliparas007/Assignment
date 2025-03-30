from pages.dashboard import DashboardPage
from pages.datasource import DataSourcePage
from pages.login import LoginPage
from utils.csv_data import csv_data
from utils.compare_ss import compare_images

def test_grafana_login(initialize_browser):
    """
    Test case to log in to Grafana, create a dashboard, add a visualization, and compare the generated screenshot with a reference image.
    """
    page = initialize_browser  # Get Playwright Page instance

    # Instantiate Page Object classes
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    datasource_page = DataSourcePage(page)

    # Perform login actions
    login_page.fill_login_form("admin", "admin")  # Enter credentials
    login_page.submit_login()  # Click login button
    login_page.skip_password_confirmation()  # Skip password confirmation if prompted

    # Create a new dashboard
    dashboard_page.create_first_dashboard()
    dashboard_page.add_visualization()

    # Configure a new data source
    datasource = dashboard_page.configure_new_data_source()
    datasource_page = DataSourcePage(datasource)  # Reinitialize with updated datasource instance

    # Set up data source and add visualization
    datasource_page.filter_data_source("test")  # Filter available data sources
    datasource_page.select_test_data()  # Select test data source
    datasource_page.save_and_test()  # Save and validate data source
    datasource_page.build_dashboard()  # Build a new dashboard
    datasource_page.add_visualization_to_datasource()  # Add visualization
    datasource_page.select_grafana_test_data()  # Choose Grafana test data
    datasource_page.select_scenario()  # Select a specific test scenario
    datasource_page.select_csv_content()  # Choose CSV content as input
    datasource_page.click_on_view_lines()  # View CSV data in line format
    datasource_page.enter_csv_data(csv_data)  # Input CSV data into the visualization
    datasource_page.verify_data_entry()  # Validate that data is correctly entered
    datasource_page.refresh_dashboard()  # Refresh the dashboard to update visualization
    datasource_page.zoom_to_data()  # Zoom into the data visualization for better visibility

    # Capture and compare visualization screenshot
    screenshot_path = datasource_page.capture_screenshot()  # Take a screenshot
    reference_path = "reference_visualization.png"  # Reference image for comparison

    # Compare captured screenshot with reference image
    if compare_images(screenshot_path, reference_path, threshold=2):
        print("Images are similar.")
    else:
        print("Images are different.")


    #clean-up datasource
    datasource_page.cleanup()