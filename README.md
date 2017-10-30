# Django Web Application for Gameboyz LLC

This website was built to facilitate the exchange of used video games between collectors in the U.S at a lower commission and with better features than current competitors.

There are five main components (apps):

## Core

This is the core application that dispatches requests to other applications.
It handles everything that should be site-wide, such as front-end styles or backend forms like user login/signup

## Games

This application handles video game titles and video game releases for a specific platform.
Users can upload listings of a video game release either for management purposes in their collection or for sale for other users to purchase.

## Consoles

This applications handles platforms and the consoles that run each platform.
Users can upload listings of a console either for management purposes in their collection or for sale for other users to purchase.

## Accessories

This application handles video game accessories related to certain games or platforms.
Users can upload listings of an accessory either for management purposes in their collection or for sale for other users to purchase.

## Sales

This application handles the sales data related to each product model: Games, Consoles, and Accessories.
It is used to approximate the market value of certain products available through the site.