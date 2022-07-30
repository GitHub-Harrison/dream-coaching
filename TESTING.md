# Dream Coaching Testing
Return back to the [README.md](/README.md)

The testing process has been broken down into two sections; one from a users point of view which focuses on how your typical user might interact with the website, the other is from an administrative point of view and how they might check the site is functioning as expected while also using features only available to them to adjust the site by adding/removing items etc.

![Am I Responsive](/documentation/am-i-responsive.png)

# User Focused Testing
This section consists of all the testing relating to the user features.

I manually tested the site throughout the whole of the development process primarily testing that all the functions work as expected and to ensure no bugs would stop the user from doing what it is they came to the site to do.

Below are some videos of me testing the final project:

## Testing as anonymous user

[![Anonymous User Testing Video](/documentation/testing/testing-videos-thumbnails/anon-user.png)](https://www.youtube.com/watch?v=ngE1HKeAjy0)

## Testing the register/login/logout feature

[![Register/Login/Logout Video Testing](/documentation/testing/testing-videos-thumbnails/register-login-logout.png)](https://www.youtube.com/watch?v=_KtDV91MD8k)

## Testing as a logged in user

[![Testing as a logged in user](/documentation/testing/testing-videos-thumbnails/logged-in-user.png)](https://www.youtube.com/watch?v=ThwxytYxS2E)

# Admin Focused Testing
This section consists of all the testing relating to the admin features.

Similar to the user focused testing I also repeatedly tested the features as I was implementing them to ensure they worked as expected.

Below are two videos of me testing the admin features:

## Testing the frontend admin

[![Testing the frontend admin](/documentation/testing/testing-videos-thumbnails/admin-frontend.png)](https://www.youtube.com/watch?v=9Mh7p3OwVL4)

## Testing the backend admin

[![Testing the backend admin](/documentation/testing/testing-videos-thumbnails/admin-backend.png)](https://www.youtube.com/watch?v=TjL_p6_3xy0)

# Bugs
While coding this project I have come across many issues/bugs, I took note of some of the bugs throught the GitHub issues tab and have linked them below:

# Solved Bugs

[[#23](https://github.com/GitHub-Harrison/dream-coaching/issues/23)] - **NameError at /products/1**

![NameError at /products/](/documentation/testing/bugs/name-error-product.png)

[[#24](https://github.com/GitHub-Harrison/dream-coaching/issues/24)] - **UnboundLocalError at /products/**

![UnboundLocalError at /products/](/documentation/testing/bugs/unboundlocalerror-at-products.png)

[[#25](https://github.com/GitHub-Harrison/dream-coaching/issues/25)] - **TemplateDoesNotExists at /contact/**

![TemplateDoesNotExists at /contact/](/documentation/testing/bugs/template-contact.png)

[[#27](https://github.com/GitHub-Harrison/dream-coaching/issues/27)] - **django.template.exceptions.TemplateSyntaxError: Invalid filter: 'crispy'**

![django.template.exceptions.TemplateSyntaxError: Invalid filter: 'crispy'](/documentation/testing/bugs/invalid-filter-crispy.png)

[[#28](https://github.com/GitHub-Harrison/dream-coaching/issues/28)] - **The 'image' attribute has no file associated with it**

![The 'image' attribute has no file associated with it](/documentation/testing/bugs/value-error-products.png)

[[#29](https://github.com/GitHub-Harrison/dream-coaching/issues/29)] - **NameError**

![NameError](/documentation/testing/bugs/name-error-checkout.png)

[[#30](https://github.com/GitHub-Harrison/dream-coaching/issues/30)] - **UnboundLocalError at /checkout/**

![UnboundLocalError at /checkout/](/documentation/testing/bugs/unboundlocalerror-at-checkout.png)

[[#31](https://github.com/GitHub-Harrison/dream-coaching/issues/31)] - **Order Success not showing all pricing**

![Order Success not showing all pricing](/documentation/testing/bugs/order-success.png)

[[#32](https://github.com/GitHub-Harrison/dream-coaching/issues/32)] - **Navigation hiding content on smaller screens**

![Navigation hiding content on smaller screens](/documentation/testing/bugs/content-hidden-by-nav.png)

# Remaining Bugs

There are no remaining bugs that I am aware of.

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

# JS Validation

This validation was done on [JSHint Validator](https://jshint.com/)

When validating my JS file it throws 'One undefined variable' even though when I look at the code it appears to be defined.

![JSHint Validation](/documentation/testing/js-validator/jshint-validator.png)

# Lighthouse Testing

I used the lighthouse feature in the developer tools of my browser to test the:

* Performance
* Accessibility
* Best Practices
* SEO

I tested the website twice, once for mobile and once for desktop to. The results are below:

## Lighthouse Test for Desktop

![Lighthouse test for desktop](/documentation/testing/lighthouse/lighthouse-test-desktop.png)

## Lighthouse Test for Mobile

![Lighthouse test for mobile](/documentation/testing/lighthouse/lighthouse-test-mobile.png)

# Browser Compatibility 

I have taken the time to test what the site looks like on various different sizes and browsers.

Below are some screenshots:

## Brave browser on PC

![Brave Browser On Pc](/documentation/testing/browser-comp/brave-pc.png)

## Brave browser on iPad Air

![Brave browser on ipad air](/documentation/testing/browser-comp/brave-ipad-air.png)

## Brave browser on iPhone 12 Pro

![Brave browser on iphone 12 pro](/documentation/testing/browser-comp/brave-iphone12.png)

## FireFox browser on PC

![Firefox browser on pc](/documentation/testing/browser-comp/firefox-pc.png)

## FireFox browser on Galaxy S20

![Firefox browser on galaxy s20](/documentation/testing/browser-comp/firefox-galaxy-s20.png)

## FireFox browser on Kindle Fire (Landscape)

![firefox browser on kindle fire](/documentation/testing/browser-comp/firefox-kindle-fire-landscape.png)

## Responsive mobile like size

![Responsive mobile like size](/documentation/testing/browser-comp/after-remove-ft-mobile.png)
