Feature: IANA Website Functionality

    Background:
        Given I am on the IANA website homepage

    Rule: About page navigation and content
        Scenario Outline: Navigate through About page sections
            When I am on the About page
            And I click on the "<link>" link in the side navigation
            Then I should be redirected to the "<url>" page
            And the page should contain relevant content

            Examples:
            | link              | url                      |
            | Audits           | /about/audits            |
            | Excellence       | /about/excellence        |
            | Archive          | /archive                 |
            | Contact us       | /contact                 |

        Scenario: Verify About page mission statement
            When I am on the About page
            Then I should see the mission statement

    Rule: Website structure and common elements
        Scenario: Verify page structure
            When I am on any page
            Then I should see the IANA logo

        Scenario: Verify footer content
            When I scroll to the bottom of the page
            Then I should see links to Privacy Policy and Terms of Service

    Rule: External website navigation
        Scenario Outline: Verify external links
            When I click on the "<link>" external link
            Then I should be redirected to the correct external website

            Examples:
            | link                    | url                          |
            | Public Technical Identifiers | https://pti.icann.org/     |
            | ICANN                  | https://www.icann.org        |
            | Privacy Policy         | https://www.icann.org/privacy/policy |
            | Terms of Service       | https://www.icann.org/privacy/tos |
