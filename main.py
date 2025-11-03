from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.secrets import get_secrets, add_already_applied_job

import time

data = get_secrets()
EMAIL = data.get("email")
FIRST_NAME = data.get("first_name")
LAST_NAME = data.get("last_name")
ALREADY_APPLIED_JOBS = data.get("applied_jobs", [])

JOB_SEARCH_BUTTON_XPATH = '//*[@id="configurable-navbar"]/div[2]/a[3]'

JOB_LOCATION_CSS = '.position-location'
APPLY_BUTTON_XPATH = '//*[@id="fixed-apply-button"]'

LOCATION_SEARCH_INPUT_XPATH = '//*[@id="location-search-box"]'
LOCATION = "United States-Utah-Roy"
SEARCH_GO_BUTTON_CSS = '[data-testid="search-bar-search-with-filters-go"]'

RECOMMENDED_JOBS_CSS = '.link-button'

LOAD_MORE_JOBS_CSS = '.load-more-button'
JOB_CARD_CLASS_NAME = 'common-entity-card'

# Contact Information
FIRST_NAME_INPUT_XPATH = '//*[@id="Contact_Information_firstname"]'
LAST_NAME_INPUT_XPATH = '//*[@id="Contact_Information_lastname"]'

# Consideration for Additional Positions
CONSIDERATION_CHECKBOX_XPATH = '//*[@id="Consideration_for_Additional_Positions_consent_choice-country_only"]'

# Ethnicity/Race Definitions
ETHNICITY_DECLINE_XPATH = '//*[@id="Ethnicity_Race_Definitions_Ethnicity_ID-USA_Declined_to_Answer"]'
ETHNICITY_MULTIRACIAL_XPATH = '//*[@id="Ethnicity_Race_Definitions_Ethnicity_ID-USA_Multi"]'

# Protected Veteran Definition
PROTECTED_VETERAN_CHECKBOX_XPATH = '//*[@id="Protected_Veteran_Definition_vevraa_question"]'
NOT_A_VETERAN_OPTION_XPATH = '//*[@id="I Am Not A Veteran-2"]'
VETERAN_DO_NOT_WISH_TO_ANSWER_OPTION_XPATH = '//*[@id="I Do Not Wish To Self-Identify-3"]'

# Personal Information Questions
PERSONAL_INFO_INPUT_XPATH = '//*[@id="Personal_Information_Questions_Q_GENDER"]'
MALE_OPTION_XPATH = '//*[@id="Male-1"]'
GENDER_DO_NOT_WISH_TO_ANSWER_OPTION_XPATH = '//*[@id="Prefer Not to Answer-3"]'

# Disability Status
DISABILITY_STATUS_DECLINE_XPATH = '//*[@id="Voluntary_Self_Identification_of_Disability_Q_DISABILITY_STATUS_EN-DECLINE_REV_2026"]'

# Position Specific Questions
SECURITY_CLEARANCE_NONE_XPATH = '//*[@id="Position_Specific_Questions_QUESTION_SETUP_6_542_a-QUESTION_MULTIPLE_CHOICE_ANSWER-6-1031"]'

CITIZEN_OF_ANOTHER_COUNTRY_XPATH = '//*[@id="Position_Specific_Questions_Dual_Citizenship_s"]'
YES_CITIZEN_OF_ANOTHER_COUNTRY_XPATH = '//*[@id="Yes-0"]'

# Terms and Conditions
TERMS_AND_CONDITIONS_CHECKBOX_XPATH = '//*[@id="Terms_and_Conditions_Terms_Acceptance-Yes"]'

# Submit Application
SUBMIT_APPLICATION_BUTTON_CSS = '[data-test-id="submitApplicationButton"]'

def wait(seconds=3):
    time.sleep(seconds)

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    wait(0.5)

def apply(driver, actions, job_id):
    # job_location = driver.find_element(by=By.CSS_SELECTOR, value=JOB_LOCATION_CSS)
    # location = job_location.text

    # apply_button = driver.find_element(by=By.XPATH, value=APPLY_BUTTON_XPATH)
    # apply_button.click()

    driver.get(f"https://jobs.northropgrumman.com/careerhub/explore/jobs/apply?pid={job_id}")

    # Fill Contact Information
    try:
        first_name_input = driver.find_element(by=By.XPATH, value=FIRST_NAME_INPUT_XPATH)
    except: # Already applied
        add_already_applied_job(job_id)
        return
    first_name_input.clear()
    first_name_input.send_keys(FIRST_NAME)

    wait()

    last_name_input = driver.find_element(by=By.XPATH, value=LAST_NAME_INPUT_XPATH)
    last_name_input.clear()
    last_name_input.send_keys(LAST_NAME)

    # Consideration for Additional Positions
    consideration_checkbox = driver.find_element(by=By.XPATH, value=CONSIDERATION_CHECKBOX_XPATH)
    scroll_to_element(driver, consideration_checkbox)
    actions.move_to_element(consideration_checkbox).click().perform()

    # Ethnicity/Race Definitions
    ethnicity_multiracial_checkbox = driver.find_element(by=By.XPATH, value=ETHNICITY_MULTIRACIAL_XPATH)
    scroll_to_element(driver, ethnicity_multiracial_checkbox)
    actions.move_to_element(ethnicity_multiracial_checkbox).click().perform()
    wait()
    ethnicity_checkbox = driver.find_element(by=By.XPATH, value=ETHNICITY_DECLINE_XPATH)
    actions.move_to_element(ethnicity_checkbox).click().perform()

    # Protected Veteran Definition
    protected_veteran_dropdown = driver.find_element(by=By.XPATH, value=PROTECTED_VETERAN_CHECKBOX_XPATH)
    scroll_to_element(driver, protected_veteran_dropdown)
    actions.move_to_element(protected_veteran_dropdown).click().perform()
    wait()
    not_a_veteran_option = driver.find_element(by=By.XPATH, value=NOT_A_VETERAN_OPTION_XPATH)
    actions.move_to_element(not_a_veteran_option).click().perform()
    wait()
    actions.move_to_element(protected_veteran_dropdown).click().perform()
    wait()
    do_not_wish_option = driver.find_element(by=By.XPATH, value=VETERAN_DO_NOT_WISH_TO_ANSWER_OPTION_XPATH)
    actions.move_to_element(do_not_wish_option).click().perform()

    # Personal Information Questions
    gender_dropdown = driver.find_element(by=By.XPATH, value=PERSONAL_INFO_INPUT_XPATH)
    scroll_to_element(driver, gender_dropdown)
    actions.move_to_element(gender_dropdown).click().perform()
    wait()
    male_option = driver.find_element(by=By.XPATH, value=MALE_OPTION_XPATH)
    actions.move_to_element(male_option).click().perform()
    wait()
    actions.move_to_element(gender_dropdown).click().perform()
    wait()
    prefer_not_option = driver.find_element(by=By.XPATH, value=GENDER_DO_NOT_WISH_TO_ANSWER_OPTION_XPATH)
    actions.move_to_element(prefer_not_option).click().perform()

    # Disability Status
    disability_status_decline = driver.find_element(by=By.XPATH, value=DISABILITY_STATUS_DECLINE_XPATH)
    scroll_to_element(driver, disability_status_decline)
    actions.move_to_element(disability_status_decline).click().perform()

    # Position Specific Questions
    # try:
    #     security_clearance_none = driver.find_element(by=By.XPATH, value=SECURITY_CLEARANCE_NONE_XPATH)
    #     scroll_to_element(driver, security_clearance_none)
    #     actions.move_to_element(security_clearance_none).click().perform()
    # except:
    #     pass

    try:
        citizen_of_another_country = driver.find_element(by=By.XPATH, value=CITIZEN_OF_ANOTHER_COUNTRY_XPATH)
        scroll_to_element(driver, citizen_of_another_country)
        actions.move_to_element(citizen_of_another_country).click().perform()

        wait()

        yes_citizen_option = driver.find_element(by=By.XPATH, value=YES_CITIZEN_OF_ANOTHER_COUNTRY_XPATH)
        actions.move_to_element(yes_citizen_option).click().perform()
    except:
        pass

    # Terms and Conditions
    terms_and_conditions_checkbox = driver.find_element(by=By.XPATH, value=TERMS_AND_CONDITIONS_CHECKBOX_XPATH)
    scroll_to_element(driver, terms_and_conditions_checkbox)
    actions.move_to_element(terms_and_conditions_checkbox).click().perform()

    # Submit Application
    submit_application_button = driver.find_element(by=By.CSS_SELECTOR, value=SUBMIT_APPLICATION_BUTTON_CSS)
    wait()
    # move mouse to button to click slowly and jiter a bit
    scroll_to_element(driver, submit_application_button)
    actions.move_to_element(submit_application_button).click().perform()

    # Check for successful submission
    wait(10)
    driver.get(f"https://jobs.northropgrumman.com/careerhub/explore/jobs/apply?pid={job_id}")
    try:
        first_name_input = driver.find_element(by=By.XPATH, value=FIRST_NAME_INPUT_XPATH)
    except: # Successfully applied
        print(f"Successfully applied to job {job_id}.")
        add_already_applied_job(job_id)
        return
    print(f"Failed to apply to job {job_id}.")

if __name__ == "__main__":
    driver = webdriver.Firefox()
    actions = webdriver.ActionChains(driver)

    driver.get("https://jobs.northropgrumman.com/careerhub/")

    driver.implicitly_wait(10)

    input("Press Enter when ready...")

    # Go to Job Search
    job_search_button = driver.find_element(by=By.XPATH, value=JOB_SEARCH_BUTTON_XPATH)
    job_search_button.click()

    # Set location
    location_search_input = driver.find_element(by=By.XPATH, value=LOCATION_SEARCH_INPUT_XPATH)
    location_search_input.clear()
    location_search_input.send_keys(LOCATION)
    wait()

    search_go_button = driver.find_element(by=By.CSS_SELECTOR, value=SEARCH_GO_BUTTON_CSS)
    actions.move_to_element(search_go_button).click().perform()

    # wait(5)
    # recommended_jobs = driver.find_element(by=By.CSS_SELECTOR, value=RECOMMENDED_JOBS_CSS)
    # actions.move_to_element(recommended_jobs).click().perform()

    # Load all jobs
    while True:
        try:
            load_more_button = driver.find_element(by=By.CSS_SELECTOR, value=LOAD_MORE_JOBS_CSS)
            scroll_to_element(driver, load_more_button)
            actions.move_to_element(load_more_button).click().perform()
        except:
            break

    # Get job IDs
    job_cards = driver.find_elements(by=By.CLASS_NAME, value=JOB_CARD_CLASS_NAME)
    job_ids = [card.get_attribute("data-card-id") for card in job_cards]
    job_ids = [id.split("::")[1] for id in job_ids]

    for job_id in job_ids:
        if job_id in ALREADY_APPLIED_JOBS:
            print(f"Already applied to job {job_id}, skipping.")
            continue
        apply(driver, actions, job_id)
        wait()

    driver.quit()