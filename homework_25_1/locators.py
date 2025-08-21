xpath_locators = {
    "signin_btn": "//button[text()='Sign In']",

    "signup_btn": "//button[@class='btn btn-outline-white header_signin']",

    "logo": "//a[@class='header_logo']",

    "login_email_input": "//input[@id='signinEmail']",

    "login_password_input": "//input[@id='signinPassword']",

    "login_submit_btn": "//button[@class='btn btn-primary' and text()='Login']",

    "forgot_password_link": "//button[@class='btn btn-link' and text()='Forgot password']",

    "garage_title": "//h1[text()='Garage']",

    "add_car_btn": "//button[@class='btn btn-primary' and text()='Add car']",

    "cars_table_header": "//app-add-car-form//label[1]",

    "edit_car_btn_first": "(//button[contains(@class,'edit')])[1]",

    "delete_car_btn_first": "(//button[contains(@class,'btn btn-outline-danger')])[1]",

    "brand_dropdown": "//select[@id='addCarBrand']",

    "model_dropdown": "//select[@id='addCarModel']",

    "mileage_input": "//input[@id='addCarMileage']",

    "add_car_modal_btn": "//button[@class='btn btn-primary' and text()='Add']",

    "success_alert": "//div[contains(@class,'alert-success')]",

    "profile_btn": "//*[@id='userNavDropdown']",

    "settings_btn": "//app-user-nav//nav/div[1]",

    "logout_btn": "//button[@class='dropdown-item btn btn-link user-nav_link' and text()='Logout']",

    "profile_title": "//h1[text()='Profile']",
}

css_locators = {
    "signin_btn": "button.header_signin",

    "signup_btn": ".col-12.col-lg-4 > div > button",

    "logo": "a.header_logo",

    "login_email_input": "input#signinEmail",

    "login_password_input": "input#signinPassword",

    "login_submit_btn": ".modal-footer > button.btn.btn-primary",

    "forgot_password_link": "app-signin-form .form-group > button",

    "garage_title": "a.btn.header-link.-active",

    "add_car_btn": "button.btn-primary",

    "cars_table_header": "div.modal-header > h4",

    "edit_car_btn_first": "app-edit-car-modal .modal-footer > button",

    "delete_car_btn_first": "app-edit-car-modal .modal-footer > button",

    "brand_dropdown": "select#addCarBrand",

    "model_dropdown": "select#addCarModel",

    "mileage_input": "input#addCarMileage",

    "add_car_modal_btn": "app-edit-car-modal .modal-footer .btn-primary",

    "success_alert": "div.alert.alert-success",

    "profile_btn": "#userNavDropdown",

    "logout_btn": "app-user-nav nav > button",

}