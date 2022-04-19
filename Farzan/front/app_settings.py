""" Settings required by django-app. """
from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import get_script_prefix
from django.utils.functional import lazy
import os

# Lazy-evaluate URLs so including pwa.urls in root urlconf works
resolve_url = lazy(resolve_url, str)

# Get script prefix for apps not mounted under /
_PWA_SCRIPT_PREFIX = get_script_prefix()

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates',
                                               'serviceworker.js'))
# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'MyApp')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'My Progressive Web App')
PWA_APP_ROOT_URL = resolve_url(getattr(settings, 'PWA_APP_ROOT_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_BACKGROUND_COLOR = getattr(settings, 'PWA_APP_BACKGROUND_COLOR', '#fff')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_SCOPE = resolve_url(getattr(settings, 'PWA_APP_SCOPE', _PWA_SCRIPT_PREFIX))
PWA_APP_DEBUG_MODE = getattr(settings, 'PWA_APP_DEBUG_MODE', True)
PWA_APP_ORIENTATION = getattr(settings, 'PWA_APP_ORIENTATION', 'any')
PWA_APP_START_URL = resolve_url(getattr(settings, 'PWA_APP_START_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_FETCH_URL = resolve_url(getattr(settings, 'PWA_APP_FETCH_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_STATUS_BAR_COLOR = getattr(settings, 'PWA_APP_STATUS_BAR_COLOR', 'default')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS',[
    {
   "src": "static/img/android-icon-36x36.png",
   "sizes": "36x36",
   "type": "image/png",
   "density": "0.75",
   "purpose": "any maskable"
  },
  {
   "src": "static/img/android-icon-48x48.png",
   "sizes": "48x48",
   "type": "image/png",
   "density": "1.0",
   "purpose": "any maskable"
  },
  {
   "src": "static/img/android-icon-72x72.png",
   "sizes": "72x72",
   "type": "image/png",
   "density": "1.5",
   "purpose": "any maskable"
  },
  {
   "src": "static/img/android-icon-96x96.png",
   "sizes": "96x96",
   "type": "image/png",
   "density": "2.0",
   "purpose": "any maskable"
  },
  {
    "src": "static/img/android-icon-144x144.png",
    "sizes": "144x144",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
   "src": "static/img/android-icon-192x192.png",
   "sizes": "192x192",
   "type": "image/png",
   "density": "4.0",
   "purpose": "any maskable"
  },
  {
    "src": "static/img/256x256.png",
    "sizes": "256x256",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/1024x1024.png",
    "sizes": "1024x1024",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/GooglePlayStore.png",
    "sizes": "512x512",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-57x57.png",
    "sizes": "57x57",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-60x60.png",
    "sizes": "60x60",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-72x72.png",
    "sizes": "72x72",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-76x76.png",
    "sizes": "76x76",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-144x144.png",
    "sizes": "144x144",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-152x152.png",
    "sizes": "152x152",
    "type": "image/png",
    "purpose": "any maskable"
  },
  {
    "src": "static/img/apple-icon-180x180.png",
    "sizes": "180x180",
    "type": "image/png",
    "purpose": "any maskable"
  },
  


])
PWA_APP_SPLASH_SCREEN = getattr(settings, 'PWA_APP_SPLASH_SCREEN', [
    {
        'src': 'static/img/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-750x1334.png',
        'media': '(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-1242x2208.png',
        'media': '(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-1125x2436.png',
        'media': '(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-828x1792.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-1242x2688.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-1536x2048.png',
        'media': '(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-1668x2224.png',
        'media': '(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-1668x2388.png',
        'media': '(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    },
    {
        'src': 'static/img/splash-2048x2732.png',
        'media': '(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)',
        'type': 'image/png',
        'purpose':'any'
    }

])
PWA_APP_DIR = getattr(settings, 'PWA_APP_DIR', 'auto')
PWA_APP_LANG = getattr(settings, 'PWA_APP_LANG', 'en-US')