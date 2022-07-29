# Dream Coaching Testing
Return back to the [README.md](/README.md)

The testing process has been broken down into two sections; one from a users point of view which focuses on how your typical user might interact with the website, the other is from an administrative point of view and how they might check the site is functioning as expected while also using features only available to them to adjust the site by adding/removing items etc.

# Am-i-responsive screenshot ?

# User Focused Testing
This section consists of all the testing relating to the user features.

# Admin Focused Testing
This section consists of all the testing relating to the admin features.

# Bugs
While coding this project I have come across many issues/bugs, I took note of some of the bugs throught the GitHub issues tab and have linked them below:

## Solved Bugs

[[#23](https://github.com/GitHub-Harrison/dream-coaching/issues/23)] - **NameError at /products/1**

[[#24](https://github.com/GitHub-Harrison/dream-coaching/issues/24)] - **UnboundLocalError at /products/**

[[#25](https://github.com/GitHub-Harrison/dream-coaching/issues/25)] - **TemplateDoesNotExists at /contact/**

[[#27](https://github.com/GitHub-Harrison/dream-coaching/issues/27)] - **django.template.exceptions.TemplateSyntaxError: Invalid filter: 'crispy'**

[[#28](https://github.com/GitHub-Harrison/dream-coaching/issues/28)] - **The 'image' attribute has no file associated with it**

[[#29](https://github.com/GitHub-Harrison/dream-coaching/issues/29)] - **NameError**

[[#30](https://github.com/GitHub-Harrison/dream-coaching/issues/30)] - **UnboundLocalError at /checkout/**

[[#31](https://github.com/GitHub-Harrison/dream-coaching/issues/31)] - **Order Success not showing all pricing**

## Remaining Bugs

As far as I am aware there are currently no bugs.

# HTML Validation
All pages were passed through the [W3C Validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fdream-coaching.herokuapp.com%2F)

I passed all the pages through using both the URL and the actual page source to be sure that there were no errors.

## Home

![Home URL Validation](/documentation/testing/html-validation/home-page-validation.png)
![Home Page Source Validation](/documentation/testing/html-validation/home-page-source.png)

## Products

![Products Main Page URL](/documentation/testing/html-validation/products-page-validation.png)
![Products Main Page Source](/documentation/testing/html-validation/products-page-source.png)
![Products By Price URL](/documentation/testing/html-validation/products-by-price-validation.png)
![Products By Price Page Source](/documentation/testing/html-validation/product-by-price-page-source.png)
![Products By Duration URL](/documentation/testing/html-validation/products-by-duration-validation.png)
![Products By Duration Source](/documentation/testing/html-validation/product-by-duration-page-source.png)

## Product Details

![Products Details URL](/documentation/testing/html-validation/product-details-url.png)
![Products Details Page Source](/documentation/testing/html-validation/product-details-page-source.png)

## Sorting By Games

![Games By All URL](/documentation/testing/html-validation/games-by-all-games.png)
![Games By Apex URL](/documentation/testing/html-validation/games-by-apex.png)
![Games By Apex Source](/documentation/testing/html-validation/games-by-apex-source.png)
![Games By CSGO URL](/documentation/testing/html-validation/games-by-csgo.png)
![Games By CSGO Source](/documentation/testing/html-validation/games-by-csgo-source.png)
![Games By R6 URL](/documentation/testing/html-validation/games-by-r6.png)
![Games By R6 Source](/documentation/testing/html-validation/games-by-r6-source.png)
![Games By League URL](/documentation/testing/html-validation/games-by-league.png)
![Games By League Source](/documentation/testing/html-validation/games-by-league-source.png)
![Games By Overwatch URL](/documentation/testing/html-validation/games-by-overwatch.png)
![Games By Overwatch Source](/documentation/testing/html-validation/games-by-overwatch-page-source.png)
![Games By Valorant URL](/documentation/testing/html-validation/games-by-valorant.png)
![Games By Valorant Source](/documentation/testing/html-validation/games-by-valorant-source.png)

## Contact

![Contact Page URL](/documentation/testing/html-validation/contact.png)
![Contact Page Source](/documentation/testing/html-validation/contact-source.png)

## Newsletter

![Newsletter Page URL](/documentation/testing/html-validation/newsletter.png)
![Newsletter Page Source](/documentation/testing/html-validation/newsletter-source.png)

## Bag

![Bag Page URL](/documentation/testing/html-validation/bag.png)
![Bag Page Source](/documentation/testing/html-validation/bag-source.png)

## Checkout

![Checkout Page URL](/documentation/testing/html-validation/checkout.png)
![Checkout Page Source](/documentation/testing/html-validation/checkout-source.png)

## Checkout Success

![Checkout Success Page URL](/documentation/testing/html-validation/checkout-success-url.png)
![Checkout Success Page Source](/documentation/testing/html-validation/checkout-success-source.png)

## Register

![Register Page URL](/documentation/testing/html-validation/signup.png)
![Register Page Source](/documentation/testing/html-validation/register-source.png)

## Login

![Login Page URL](/documentation/testing/html-validation/login-url.png)
![Login Page Source](/documentation/testing/html-validation/login-source.png)

## Logout

![Logout Page URL](/documentation/testing/html-validation/logout-url.png)
![Logout Page Source](/documentation/testing/html-validation/logout-source.png)

## Profile Page

![Profile Page URL](/documentation/testing/html-validation/profile-page-url.png)
![Profile Page Source](/documentation/testing/html-validation/profile-page-source.png)

## Add Product

![Add Product Page URL](/documentation/testing/html-validation/add-product.png)
![Add Product Page Source](/documentation/testing/html-validation/add-game-source.png)

## Search Box

![Search Box URL](/documentation/testing/html-validation/search-box.png)

# PEP8 Validation

I passed my code through a [PEP8 Validator](http://pep8online.com/checkresult) and the results are below: 

## Bag

### contexts.py
![Contexts.py Validation](/documentation/testing/pep8-validator/bag/contexts.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/bag/urls.py.png)

### views.py
![Views.py Validation](/documentation/testing/pep8-validator/bag/views.py.png)

## Checkout

### admin.py
![Admin.py Validation](/documentation/testing/pep8-validator/checkout/admin.py.png)

### forms.py
![Forms.py Validation](/documentation/testing/pep8-validator/checkout/forms.py.png)

### models.py
![Models.py Validation](/documentation/testing/pep8-validator/checkout/models.py.png)

### signals.py
![Signals.py Validation](/documentation/testing/pep8-validator/checkout/signals.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/checkout/urls.py.png)

### views.py
![Views.py Validation](/documentation/testing/pep8-validator/checkout/views.py.png)

### webhook_handler.py
![Webhook_handler.py](/documentation/testing/pep8-validator/checkout/webhook_handler.py.png)

### webhooks.py
![Webhooks.py Validation](/documentation/testing/pep8-validator/checkout/webhooks.py.png)

## Contact

### admin.py 
![Admin.py Validation](/documentation/testing/pep8-validator/contact/admin.py.png)

### forms.py
![Forms.py Validation](/documentation/testing/pep8-validator/contact/forms.py.png)

### models.py
![Models.py Validation](/documentation/testing/pep8-validator/contact/models.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/contact/urls.py.png)

### views.py
![Views.py Validation](/documentation/testing/pep8-validator/contact/views.py.png)

## Dream Coaching

### settings.py
![Settings.py Validation](/documentation/testing/pep8-validator/dream-coaching/settings.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/dream-coaching/urls.py.png)

## Home

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/home/urls.py.png)

### views.py
![Views.py Validation](/documentation/testing/pep8-validator/home/views.py.png)

## Newsletter

### admin.py
![Admin.py Validation](/documentation/testing/pep8-validator/newsletter/admin.py.png)

### forms.py
![Forms.py Validation](/documentation/testing/pep8-validator/newsletter/forms.py.png)

### models.py
![Models.py Validation](/documentation/testing/pep8-validator/newsletter/models.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/newsletter/urls.py.png)

### views.py
![Views.py Validation](/documentation/testing/pep8-validator/newsletter/views.py.png)

## Products

### admin.py
![Admin.py Validation](/documentation/testing/pep8-validator/products/admin.py.png)

### forms.py
![Forms.py Validation](/documentation/testing/pep8-validator/products/forms.py.png)

### models.py
![Models.py Validation](/documentation/testing/pep8-validator/products/models.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/products/urls.py.png)

### views.py

* I have chosen to leave this 'error' as I am concerned that changing the layout of this line may break the code.

![Views.py Validation](/documentation/testing/pep8-validator/products/views.py.png)

### widgets.py
![Widgets.py Validation](/documentation/testing/pep8-validator/products/widgets.py.png)

## Profiles

### forms.py
![Forms.py Validation](/documentation/testing/pep8-validator/profiles/forms.py.png)

### models.py
![Models.py Validation](/documentation/testing/pep8-validator/profiles/models.py.png)

### urls.py
![Urls.py Validation](/documentation/testing/pep8-validator/profiles/urls.py.png)

### views.py
![Views.py Validation](/documentation/testing/pep8-validator/profiles/views.py.png)

# CSS Validation

This validation was done on [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) via the deployed sites url.

![CSS Validation](/documentation/testing/css-validator/css-url.png)

# Browser Compatibility 

* Video testing.
* Browser Compatibility.