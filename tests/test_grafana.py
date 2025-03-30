from pages.dashboard import DashboardPage
from pages.datasource import DataSourcePage
from pages.login import LoginPage
from utils.csv_data import csv_data
from utils.compare_ss import compare_images

def test_grafana_login(initialize_browser):
    page = initialize_browser

    # Instantiate the Page Objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    datasource_page = DataSourcePage(page)

    # Perform actions
    login_page.fill_login_form("admin", "admin")
    login_page.submit_login()
    login_page.skip_password_confirmation()

    dashboard_page.create_first_dashboard()
    dashboard_page.add_visualization()

    datasource = dashboard_page.configure_new_data_source()

    datasource_page = DataSourcePage(datasource)
    datasource_page.filter_data_source("test")
    datasource_page.select_test_data()
    datasource_page.save_and_test()
    datasource_page.build_dashboard()
    datasource_page.add_visualization_to_datasource()
    datasource_page.select_grafana_test_data()
    datasource_page.select_scenario()
    datasource_page.select_csv_content()
    datasource_page.click_on_view_lines()
    datasource_page.enter_csv_data(csv_data)
    datasource_page.verify_data_entry()
    datasource_page.refresh_dashboard()
    datasource_page.zoom_to_data()
    screenshot_path = datasource_page.capture_screenshot()

    reference_path = "reference_visualization.png"
    if compare_images(screenshot_path, reference_path, threshold=2):
        print("Images are similar.")
    else:
        print("Images are different.")
