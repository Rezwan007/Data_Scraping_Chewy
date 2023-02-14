from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import json

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

res = driver.page_source
soup1 = BeautifulSoup(res, 'lxml')

res3 = driver.page_source
soup3 = BeautifulSoup(res3, 'lxml')
containers = soup3.find_all(attrs={"data-list": "browse"})

allProductData = []
failedLinks=[]

links = [
    {
        "productName": "Pedigree  Choice Cuts In Gravy Beef & Country Stew Adult Canned Wet Dog Food Variety Pack, 13.2-...",
        "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-beef/dp/387570"
    },
    {
        "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy Variety Pack Canned Dog Food, 13-oz, c...",
        "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/138447"
    },
    {
        "productName": "Cesar  Classic Loaf in Sauce Beef Recipe, Filet Mignon, Grilled Chicken, & Porterhouse Steak Fla...",
        "url": "https://www.chewy.com/cesar-classic-loaf-in-sauce-beef/dp/114268"
    },
    {
        "productName": "Blue Buffalo  Homestyle Recipes Adult Variety Pack Chicken & Beef Dinner Canned Dog Food, 12.5-o...",
        "url": "https://www.chewy.com/blue-buffalo-homestyle-recipes-adult/dp/176651"
    },
    {
        "productName": "Purina Beneful  IncrediBites Variety Pack Canned Dog Food, 3-oz can, case of 30",
        "url": "https://www.chewy.com/purina-beneful-incredibites-variety/dp/303344"
    },
    {
        "productName": "Purina ONE  SmartBlend Classic Ground Beef & Brown Rice Entree Adult Canned Dog Food, 13-oz, cas...",
        "url": "https://www.chewy.com/purina-one-smartblend-classic-ground/dp/119369"
    },
    {
        "productName": "Pedigree  Chopped Ground Dinner Filet Mignon Flavor & Beef Adult Canned Wet Dog Food Variety Pac...",
        "url": "https://www.chewy.com/pedigree-chopped-ground-dinner-filet/dp/141611"
    },
    {
        "productName": "Purina Beyond  Alaskan Cod, Salmon & Sweet Potato Grain-Free Canned Dog Food, 13-oz, case of 12",
        "url": "https://www.chewy.com/purina-beyond-alaskan-cod-salmon/dp/169331"
    },
    {
        "productName": "Hill's Prescription Diet  i/d Digestive Care Low Fat Rice, Vegetable & Chicken Stew Wet Dog Food...",
        "url": "https://www.chewy.com/hills-prescription-diet-id-digestive/dp/120440"
    },
    {
        "productName": "Pedigree  Choice Cuts in Gravy Prime Rib, Rice & Vegetable Flavor & Roasted Chicken Adult Canned...",
        "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-prime/dp/387577"
    },
    {
        "productName": "Blue Buffalo  Homestyle Recipe Senior Chicken Dinner with Garden Vegetables Canned Dog Food, 12....",
        "url": "https://www.chewy.com/blue-buffalo-homestyle-recipe-senior/dp/49582"
    },
    # {
    #     "productName": "Nature's Recipe  Prime Blends Variety Pack Wet Dog Food, 2.75-oz, case of 12",
    #     "url": "https://www.chewy.com/natures-recipe-prime-blends-variety/dp/234458"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy with Real Beef & Wild-Caught Salmon Ca...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/168156"
    # },
    # {
    #     "productName": "Bundle: Pedigree Chopped Ground Dinner Variety Pack With Filet Mignon & Beef + Variety Pack Wit...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner/dp/393716"
    # },
    # {
    #     "productName": "Stella & Chewy's  Wild Red Variety Pack Grain-Free Wet Dog Food, 10-oz can, case of 3",
    #     "url": "https://www.chewy.com/stella-chewys-wild-red-variety-pack/dp/318010"
    # },
    # {
    #     "productName": "Purina Beneful  Chopped Blends Variety Pack Wet Dog Food Tray, 10-oz, case of 12",
    #     "url": "https://www.chewy.com/purina-beneful-chopped-blends-variety/dp/168187"
    # },
    # {
    #     "productName": "Evanger's  Classic Recipes Beef with Chicken & Liver Grain-Free Canned Dog Food, 12.5-oz, case o...",
    #     "url": "https://www.chewy.com/evangers-classic-recipes-beef-chicken/dp/35949"
    # },
    # {
    #     "productName": "Blue Buffalo  Divine Delights Roasted Chicken Flavor Hearty Gravy Dog Food Trays, 3.5-oz, case o...",
    #     "url": "https://www.chewy.com/blue-buffalo-divine-delights-roasted/dp/141572"
    # },
    # {
    #     "productName": "Cesar  Filets in Gravy Beef Flavors Variety Pack Adult Wet Dog Food, 3.5-oz tray, case of 24",
    #     "url": "https://www.chewy.com/cesar-filets-in-gravy-beef-flavors/dp/137903"
    # },
    # {
    #     "productName": "Purina Beyond  Natural Grain-Free Beef Potato & Green Bean Recipe Ground Entree Wet Dog Food, 13...",
    #     "url": "https://www.chewy.com/purina-beyond-natural-grain-free-beef/dp/113995"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Liver & Beef, Beef, Bacon & Cheese Flavor with Chicken Adult Can...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner-liver/dp/387584"
    # },
    # {
    #     "productName": "Rachael Ray Nutrish  Natural Variety Pack Wet Dog Food, 8-oz tub, case of 6",
    #     "url": "https://www.chewy.com/rachael-ray-nutrish-natural-variety/dp/128026"
    # },
    # {
    #     "productName": "Iams  ProActive Health Classic Ground with Chicken & Whole Grain Rice Adult Wet Dog Food, 13-oz,...",
    #     "url": "https://www.chewy.com/iams-proactive-health-classic-ground/dp/32851"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy with Real Chicken & Duck Canned Dog Fo...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/129895"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Variety Pack Filet Mignon, Grilled Chicken, Chicken Casserole & B...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-variety/dp/168573"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Chicken with Beef Adult Canned Wet Dog Food Variety Pack, 13.2 o...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner/dp/141609"
    # },
    # {
    #     "productName": "Purina Beneful  Medleys Tuscan, Romana & Mediterranean Style Variety Pack Wet Dog Food, 3-oz can...",
    #     "url": "https://www.chewy.com/purina-beneful-medleys-tuscan-romana/dp/303346"
    # },
    # {
    #     "productName": "Purina Pro Plan  Savor Classic 3 Entrees Variety Pack Grain-Free Canned Dog Food, 13-oz, case of...",
    #     "url": "https://www.chewy.com/purina-pro-plan-savor-classic-3/dp/183084"
    # },
    # {
    #     "productName": "Hill's Science Diet  Adult Sensitive Stomach & Skin Tender Turkey & Rice Stew Canned Dog Food, 1...",
    #     "url": "https://www.chewy.com/hills-science-diet-adult-sensitive/dp/184533"
    # },
    # {
    #     "productName": "Cesar  Poultry Variety Pack with Real Chicken, Turkey & Duck Dog Food Trays, 3.5-oz, case of 24",
    #     "url": "https://www.chewy.com/cesar-poultry-variety-pack-real/dp/114234"
    # },
    # {
    #     "productName": "Blue Buffalo  Divine Delights Pate Small Breed Variety Pack Filet Mignon & Porterhouse Flavor Do...",
    #     "url": "https://www.chewy.com/blue-buffalo-divine-delights-pate/dp/141547"
    # },
    # {
    #     "productName": "Purina Beyond  Chicken, Carrot & Pea Recipe Ground Entr\u00e9e Grain-Free Canned Dog Food, 13-oz, cas...",
    #     "url": "https://www.chewy.com/purina-beyond-chicken-carrot-pea/dp/113997"
    # },
    # {
    #     "productName": "OrgaNOMics  Salmon & Duck Dinner Grain-Free Pate Wet Dog Food, 12.5-oz can, case of 12",
    #     "url": "https://www.chewy.com/organomics-salmon-duck-dinner-grain/dp/204711"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Country Stew & Chicken & Rice Flavor Adult Canned Wet Dog Food Va...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-country/dp/387573"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend Grain-Free True Instinct Classic Ground with Real Chicken & Duck Canned D...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-grain-free-true/dp/129900"
    # },
    # {
    #     "productName": "Purina Bella  Natural Pate Variety Pack, Filet Mignon & Porterhouse Steak in Juices Small Breed ...",
    #     "url": "https://www.chewy.com/purina-bella-natural-pate-variety/dp/138164"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts In Gravy Beef & Country Stew Adult Canned Wet Dog Food Variety Pack, 13.2-...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-beef/dp/387570"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy Variety Pack Canned Dog Food, 13-oz, c...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/138447"
    # },
    # {
    #     "productName": "Cesar  Classic Loaf in Sauce Beef Recipe, Filet Mignon, Grilled Chicken, & Porterhouse Steak Fla...",
    #     "url": "https://www.chewy.com/cesar-classic-loaf-in-sauce-beef/dp/114268"
    # },
    # {
    #     "productName": "Blue Buffalo  Homestyle Recipes Adult Variety Pack Chicken & Beef Dinner Canned Dog Food, 12.5-o...",
    #     "url": "https://www.chewy.com/blue-buffalo-homestyle-recipes-adult/dp/176651"
    # },
    # {
    #     "productName": "Purina Beneful  IncrediBites Variety Pack Canned Dog Food, 3-oz can, case of 30",
    #     "url": "https://www.chewy.com/purina-beneful-incredibites-variety/dp/303344"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend Classic Ground Beef & Brown Rice Entree Adult Canned Dog Food, 13-oz, cas...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-classic-ground/dp/119369"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Filet Mignon Flavor & Beef Adult Canned Wet Dog Food Variety Pac...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner-filet/dp/141611"
    # },
    # {
    #     "productName": "Purina Beyond  Alaskan Cod, Salmon & Sweet Potato Grain-Free Canned Dog Food, 13-oz, case of 12",
    #     "url": "https://www.chewy.com/purina-beyond-alaskan-cod-salmon/dp/169331"
    # },
    # {
    #     "productName": "Hill's Prescription Diet  i/d Digestive Care Low Fat Rice, Vegetable & Chicken Stew Wet Dog Food...",
    #     "url": "https://www.chewy.com/hills-prescription-diet-id-digestive/dp/120440"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Prime Rib, Rice & Vegetable Flavor & Roasted Chicken Adult Canned...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-prime/dp/387577"
    # },
    # {
    #     "productName": "Blue Buffalo  Homestyle Recipe Senior Chicken Dinner with Garden Vegetables Canned Dog Food, 12....",
    #     "url": "https://www.chewy.com/blue-buffalo-homestyle-recipe-senior/dp/49582"
    # },
    # {
    #     "productName": "Nature's Recipe  Prime Blends Variety Pack Wet Dog Food, 2.75-oz, case of 12",
    #     "url": "https://www.chewy.com/natures-recipe-prime-blends-variety/dp/234458"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy with Real Beef & Wild-Caught Salmon Ca...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/168156"
    # },
    # {
    #     "productName": "Bundle: Pedigree Chopped Ground Dinner Variety Pack With Filet Mignon & Beef + Variety Pack Wit...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner/dp/393716"
    # },
    # {
    #     "productName": "Stella & Chewy's  Wild Red Variety Pack Grain-Free Wet Dog Food, 10-oz can, case of 3",
    #     "url": "https://www.chewy.com/stella-chewys-wild-red-variety-pack/dp/318010"
    # },
    # {
    #     "productName": "Purina Beneful  Chopped Blends Variety Pack Wet Dog Food Tray, 10-oz, case of 12",
    #     "url": "https://www.chewy.com/purina-beneful-chopped-blends-variety/dp/168187"
    # },
    # {
    #     "productName": "Evanger's  Classic Recipes Beef with Chicken & Liver Grain-Free Canned Dog Food, 12.5-oz, case o...",
    #     "url": "https://www.chewy.com/evangers-classic-recipes-beef-chicken/dp/35949"
    # },
    # {
    #     "productName": "Blue Buffalo  Divine Delights Roasted Chicken Flavor Hearty Gravy Dog Food Trays, 3.5-oz, case o...",
    #     "url": "https://www.chewy.com/blue-buffalo-divine-delights-roasted/dp/141572"
    # },
    # {
    #     "productName": "Cesar  Filets in Gravy Beef Flavors Variety Pack Adult Wet Dog Food, 3.5-oz tray, case of 24",
    #     "url": "https://www.chewy.com/cesar-filets-in-gravy-beef-flavors/dp/137903"
    # },
    # {
    #     "productName": "Purina Beyond  Natural Grain-Free Beef Potato & Green Bean Recipe Ground Entree Wet Dog Food, 13...",
    #     "url": "https://www.chewy.com/purina-beyond-natural-grain-free-beef/dp/113995"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Liver & Beef, Beef, Bacon & Cheese Flavor with Chicken Adult Can...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner-liver/dp/387584"
    # },
    # {
    #     "productName": "Rachael Ray Nutrish  Natural Variety Pack Wet Dog Food, 8-oz tub, case of 6",
    #     "url": "https://www.chewy.com/rachael-ray-nutrish-natural-variety/dp/128026"
    # },
    # {
    #     "productName": "Iams  ProActive Health Classic Ground with Chicken & Whole Grain Rice Adult Wet Dog Food, 13-oz,...",
    #     "url": "https://www.chewy.com/iams-proactive-health-classic-ground/dp/32851"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy with Real Chicken & Duck Canned Dog Fo...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/129895"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Variety Pack Filet Mignon, Grilled Chicken, Chicken Casserole & B...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-variety/dp/168573"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Chicken with Beef Adult Canned Wet Dog Food Variety Pack, 13.2 o...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner/dp/141609"
    # },
    # {
    #     "productName": "Purina Beneful  Medleys Tuscan, Romana & Mediterranean Style Variety Pack Wet Dog Food, 3-oz can...",
    #     "url": "https://www.chewy.com/purina-beneful-medleys-tuscan-romana/dp/303346"
    # },
    # {
    #     "productName": "Purina Pro Plan  Savor Classic 3 Entrees Variety Pack Grain-Free Canned Dog Food, 13-oz, case of...",
    #     "url": "https://www.chewy.com/purina-pro-plan-savor-classic-3/dp/183084"
    # },
    # {
    #     "productName": "Hill's Science Diet  Adult Sensitive Stomach & Skin Tender Turkey & Rice Stew Canned Dog Food, 1...",
    #     "url": "https://www.chewy.com/hills-science-diet-adult-sensitive/dp/184533"
    # },
    # {
    #     "productName": "Cesar  Poultry Variety Pack with Real Chicken, Turkey & Duck Dog Food Trays, 3.5-oz, case of 24",
    #     "url": "https://www.chewy.com/cesar-poultry-variety-pack-real/dp/114234"
    # },
    # {
    #     "productName": "Blue Buffalo  Divine Delights Pate Small Breed Variety Pack Filet Mignon & Porterhouse Flavor Do...",
    #     "url": "https://www.chewy.com/blue-buffalo-divine-delights-pate/dp/141547"
    # },
    # {
    #     "productName": "Purina Beyond  Chicken, Carrot & Pea Recipe Ground Entr\u00e9e Grain-Free Canned Dog Food, 13-oz, cas...",
    #     "url": "https://www.chewy.com/purina-beyond-chicken-carrot-pea/dp/113997"
    # },
    # {
    #     "productName": "OrgaNOMics  Salmon & Duck Dinner Grain-Free Pate Wet Dog Food, 12.5-oz can, case of 12",
    #     "url": "https://www.chewy.com/organomics-salmon-duck-dinner-grain/dp/204711"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Country Stew & Chicken & Rice Flavor Adult Canned Wet Dog Food Va...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-country/dp/387573"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend Grain-Free True Instinct Classic Ground with Real Chicken & Duck Canned D...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-grain-free-true/dp/129900"
    # },
    # {
    #     "productName": "Purina Bella  Natural Pate Variety Pack, Filet Mignon & Porterhouse Steak in Juices Small Breed ...",
    #     "url": "https://www.chewy.com/purina-bella-natural-pate-variety/dp/138164"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts In Gravy Beef & Country Stew Adult Canned Wet Dog Food Variety Pack, 13.2-...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-beef/dp/387570"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy Variety Pack Canned Dog Food, 13-oz, c...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/138447"
    # },
    # {
    #     "productName": "Cesar  Classic Loaf in Sauce Beef Recipe, Filet Mignon, Grilled Chicken, & Porterhouse Steak Fla...",
    #     "url": "https://www.chewy.com/cesar-classic-loaf-in-sauce-beef/dp/114268"
    # },
    # {
    #     "productName": "Blue Buffalo  Homestyle Recipes Adult Variety Pack Chicken & Beef Dinner Canned Dog Food, 12.5-o...",
    #     "url": "https://www.chewy.com/blue-buffalo-homestyle-recipes-adult/dp/176651"
    # },
    # {
    #     "productName": "Purina Beneful  IncrediBites Variety Pack Canned Dog Food, 3-oz can, case of 30",
    #     "url": "https://www.chewy.com/purina-beneful-incredibites-variety/dp/303344"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend Classic Ground Beef & Brown Rice Entree Adult Canned Dog Food, 13-oz, cas...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-classic-ground/dp/119369"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Filet Mignon Flavor & Beef Adult Canned Wet Dog Food Variety Pac...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner-filet/dp/141611"
    # },
    # {
    #     "productName": "Purina Beyond  Alaskan Cod, Salmon & Sweet Potato Grain-Free Canned Dog Food, 13-oz, case of 12",
    #     "url": "https://www.chewy.com/purina-beyond-alaskan-cod-salmon/dp/169331"
    # },
    # {
    #     "productName": "Hill's Prescription Diet  i/d Digestive Care Low Fat Rice, Vegetable & Chicken Stew Wet Dog Food...",
    #     "url": "https://www.chewy.com/hills-prescription-diet-id-digestive/dp/120440"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Prime Rib, Rice & Vegetable Flavor & Roasted Chicken Adult Canned...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-prime/dp/387577"
    # },
    # {
    #     "productName": "Blue Buffalo  Homestyle Recipe Senior Chicken Dinner with Garden Vegetables Canned Dog Food, 12....",
    #     "url": "https://www.chewy.com/blue-buffalo-homestyle-recipe-senior/dp/49582"
    # },
    # {
    #     "productName": "Nature's Recipe  Prime Blends Variety Pack Wet Dog Food, 2.75-oz, case of 12",
    #     "url": "https://www.chewy.com/natures-recipe-prime-blends-variety/dp/234458"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy with Real Beef & Wild-Caught Salmon Ca...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/168156"
    # },
    # {
    #     "productName": "Bundle: Pedigree Chopped Ground Dinner Variety Pack With Filet Mignon & Beef + Variety Pack Wit...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner/dp/393716"
    # },
    # {
    #     "productName": "Stella & Chewy's  Wild Red Variety Pack Grain-Free Wet Dog Food, 10-oz can, case of 3",
    #     "url": "https://www.chewy.com/stella-chewys-wild-red-variety-pack/dp/318010"
    # },
    # {
    #     "productName": "Purina Beneful  Chopped Blends Variety Pack Wet Dog Food Tray, 10-oz, case of 12",
    #     "url": "https://www.chewy.com/purina-beneful-chopped-blends-variety/dp/168187"
    # },
    # {
    #     "productName": "Evanger's  Classic Recipes Beef with Chicken & Liver Grain-Free Canned Dog Food, 12.5-oz, case o...",
    #     "url": "https://www.chewy.com/evangers-classic-recipes-beef-chicken/dp/35949"
    # },
    # {
    #     "productName": "Blue Buffalo  Divine Delights Roasted Chicken Flavor Hearty Gravy Dog Food Trays, 3.5-oz, case o...",
    #     "url": "https://www.chewy.com/blue-buffalo-divine-delights-roasted/dp/141572"
    # },
    # {
    #     "productName": "Cesar  Filets in Gravy Beef Flavors Variety Pack Adult Wet Dog Food, 3.5-oz tray, case of 24",
    #     "url": "https://www.chewy.com/cesar-filets-in-gravy-beef-flavors/dp/137903"
    # },
    # {
    #     "productName": "Purina Beyond  Natural Grain-Free Beef Potato & Green Bean Recipe Ground Entree Wet Dog Food, 13...",
    #     "url": "https://www.chewy.com/purina-beyond-natural-grain-free-beef/dp/113995"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Liver & Beef, Beef, Bacon & Cheese Flavor with Chicken Adult Can...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner-liver/dp/387584"
    # },
    # {
    #     "productName": "Rachael Ray Nutrish  Natural Variety Pack Wet Dog Food, 8-oz tub, case of 6",
    #     "url": "https://www.chewy.com/rachael-ray-nutrish-natural-variety/dp/128026"
    # },
    # {
    #     "productName": "Iams  ProActive Health Classic Ground with Chicken & Whole Grain Rice Adult Wet Dog Food, 13-oz,...",
    #     "url": "https://www.chewy.com/iams-proactive-health-classic-ground/dp/32851"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend True Instinct Tender Cuts in Gravy with Real Chicken & Duck Canned Dog Fo...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-true-instinct/dp/129895"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Variety Pack Filet Mignon, Grilled Chicken, Chicken Casserole & B...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-variety/dp/168573"
    # },
    # {
    #     "productName": "Pedigree  Chopped Ground Dinner Chicken with Beef Adult Canned Wet Dog Food Variety Pack, 13.2 o...",
    #     "url": "https://www.chewy.com/pedigree-chopped-ground-dinner/dp/141609"
    # },
    # {
    #     "productName": "Purina Beneful  Medleys Tuscan, Romana & Mediterranean Style Variety Pack Wet Dog Food, 3-oz can...",
    #     "url": "https://www.chewy.com/purina-beneful-medleys-tuscan-romana/dp/303346"
    # },
    # {
    #     "productName": "Purina Pro Plan  Savor Classic 3 Entrees Variety Pack Grain-Free Canned Dog Food, 13-oz, case of...",
    #     "url": "https://www.chewy.com/purina-pro-plan-savor-classic-3/dp/183084"
    # },
    # {
    #     "productName": "Hill's Science Diet  Adult Sensitive Stomach & Skin Tender Turkey & Rice Stew Canned Dog Food, 1...",
    #     "url": "https://www.chewy.com/hills-science-diet-adult-sensitive/dp/184533"
    # },
    # {
    #     "productName": "Cesar  Poultry Variety Pack with Real Chicken, Turkey & Duck Dog Food Trays, 3.5-oz, case of 24",
    #     "url": "https://www.chewy.com/cesar-poultry-variety-pack-real/dp/114234"
    # },
    # {
    #     "productName": "Blue Buffalo  Divine Delights Pate Small Breed Variety Pack Filet Mignon & Porterhouse Flavor Do...",
    #     "url": "https://www.chewy.com/blue-buffalo-divine-delights-pate/dp/141547"
    # },
    # {
    #     "productName": "Purina Beyond  Chicken, Carrot & Pea Recipe Ground Entr\u00e9e Grain-Free Canned Dog Food, 13-oz, cas...",
    #     "url": "https://www.chewy.com/purina-beyond-chicken-carrot-pea/dp/113997"
    # },
    # {
    #     "productName": "OrgaNOMics  Salmon & Duck Dinner Grain-Free Pate Wet Dog Food, 12.5-oz can, case of 12",
    #     "url": "https://www.chewy.com/organomics-salmon-duck-dinner-grain/dp/204711"
    # },
    # {
    #     "productName": "Pedigree  Choice Cuts in Gravy Country Stew & Chicken & Rice Flavor Adult Canned Wet Dog Food Va...",
    #     "url": "https://www.chewy.com/pedigree-choice-cuts-in-gravy-country/dp/387573"
    # },
    # {
    #     "productName": "Purina ONE  SmartBlend Grain-Free True Instinct Classic Ground with Real Chicken & Duck Canned D...",
    #     "url": "https://www.chewy.com/purina-one-smartblend-grain-free-true/dp/129900"
    # },
    # {
    #     "productName": "Purina Bella  Natural Pate Variety Pack, Filet Mignon & Porterhouse Steak in Juices Small Breed ...",
    #     "url": "https://www.chewy.com/purina-bella-natural-pate-variety/dp/138164"
    # }
]

for x in links:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(x['url'])
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Collecting data from web
    try:
        try:
            productName = soup.find('h1', class_='styles_productName__vSdxx').text
            print(productName)
        except:
            productName = ''

        try:
            productBrand = soup.find('a', class_='styles_brandLink__MdoyO').text
            print(productBrand)
        except:
            productBrand = ''

        try:
            # productPrice = soup.find('div', class_='kib-product-price kib-product-price--xl tablescraper-next-button')
            productPrice = driver.find_element(By.XPATH,
                                               "//div[@data-testid='price-block']/div/div[@data-testid='advertised-price'][contains(text(),'')]").text.replace(
                '\n', '').strip()
            print(productPrice)
        except:
            productPrice = ''

        try:
            imageNextButton = driver.find_element(By.XPATH, "//button[@data-testid='carousel-next-arrow']").click()
            time.sleep(2)
            productImageArray = []
            productImage = driver.find_elements(By.XPATH,
                                                "//img[@class='styles_mainCarouselImage__wj_bU']")
            for productImageAll in productImage:
                productImageSrc = productImageAll.get_attribute('src')
                print(productImageSrc)
                productImageArray.append(productImageSrc)
        except:
            pass
        for i in range(6):
            driver.execute_script("window.scrollBy(0, 200)")
            time.sleep(1)

        try:
            ntriInfoBTN = driver.find_element(By.XPATH, "//button[@aria-label='Nutritional Information']")
            time.sleep(1)
            ntriInfoBTN.click()
            time.sleep(1)
            ntriIngredients = driver.find_element(By.XPATH,
                                                  "//div[@class='kib-accordion-new-item__content enter-done']/section[@class='styles_infoGroupSection__ArCb9'][1]")
            ntriIngredientsTXT = ntriIngredients.text.replace('\n', '').strip()
            print("Ingredients:" + ntriIngredientsTXT)

            time.sleep(1)
            nrtiCaloricContent = driver.find_element(By.XPATH,
                                                     "//div[@class='kib-accordion-new-item__content enter-done']/section[@class='styles_infoGroupSection__ArCb9'][2]")
            nrtiCaloricContentTXT = nrtiCaloricContent.text.replace('\n', '').strip()
            print("caloricContent:" + nrtiCaloricContentTXT)

            time.sleep(1)
            nrtiCaloricContentArray = []

            nrtiGauranteedAnalysisTable = driver.find_elements(By.XPATH,
                                                               "//section[@id='GUARANTEED_ANALYSIS-section']/div/div[@class='styles_markdownTable__Mtq7h']/table")
            nrtiGauranteedAnalysisTableLen = len(nrtiGauranteedAnalysisTable)

            for i in range(2):
                driver.execute_script("window.scrollBy(0, 200)")
                time.sleep(3)

            v = 1
            for v in range(nrtiGauranteedAnalysisTableLen):
                vall = v + 1
                print(vall)
                guaranteedAnalysisType = driver.find_element(By.XPATH,
                                                             "//section[@id='GUARANTEED_ANALYSIS-section']/div/p[position()='" + str(
                                                                 vall) + "']/strong").text
                crudeProtein = driver.find_element(By.XPATH,
                                                   "//section[@id='GUARANTEED_ANALYSIS-section']/div/div[@class='styles_markdownTable__Mtq7h'][position()='" + str(
                                                       vall) + "']/table/tbody/tr[1]/td").text

                for i in range(2):
                    driver.execute_script("window.scrollBy(0, 200)")
                    time.sleep(1)

                crudeFat = driver.find_element(By.XPATH,
                                               "//section[@id='GUARANTEED_ANALYSIS-section']/div/div[@class='styles_markdownTable__Mtq7h'][position()='" + str(
                                                   vall) + "']/table/tbody/tr[2]/td").text
                crudeFiber = driver.find_element(By.XPATH,
                                                 "//section[@id='GUARANTEED_ANALYSIS-section']/div/div[@class='styles_markdownTable__Mtq7h'][position()='" + str(
                                                     vall) + "']/table/tbody/tr[3]/td").text
                moisture = driver.find_element(By.XPATH,
                                               "//section[@id='GUARANTEED_ANALYSIS-section']/div/div[@class='styles_markdownTable__Mtq7h'][position()='" + str(
                                                   vall) + "']/table/tbody/tr[4]/td").text

                print("guaranteedAnalysisType" + ":" + guaranteedAnalysisType)
                print("crudeProtein" + ":" + crudeProtein)
                print("crudeFat" + ":" + crudeFat)
                print("crudeFiber" + ":" + crudeFiber)
                print("moisture" + ":" + moisture)

                nrtiCaloricContentAll = {
                    'guaranteedAnalysisType': guaranteedAnalysisType,
                    'crudeProtein': crudeProtein,
                    'crudeFat': crudeFat,
                    'crudeFiber': crudeFiber,
                    'moisture': moisture
                }
                nrtiCaloricContentArray.append(nrtiCaloricContentAll)
        except:
            failedLinks.append(x)
            nrtiCaloricContentAll = {
                'guaranteedAnalysisType': '',
                'crudeProtein': '',
                'crudeFat': '',
                'crudeFiber': '',
                'moisture': ''
            }
            nrtiCaloricContentArray.append(nrtiCaloricContentAll)
    except:
        failedLinks.append(x)

    # saving data in json
    productInfo={

        'productName': productName,
        'productBrand': productBrand,
        'productPrice': productPrice,
        'productImage': productImageArray,
        'nutritionInfo': {
            'ingredients': ntriIngredientsTXT,
            'specifications':nrtiCaloricContentTXT
        },
        'guaranteedAnalysis': {
            'nrtiCaloricContentTrAll':nrtiCaloricContentArray
        }


    }
    allProductData.append(productInfo)



    print("....................")
    time.sleep(2)
    driver.quit()


f = open('pantryData.json', 'a')
f.write(json.dumps(allProductData, indent=4))

f = open('failedLinks.json', 'a')
f.write(json.dumps(failedLinks, indent=4))
