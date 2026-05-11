from behave import given, when, then
from selenium import webdriver
from pages.lastfm_landing_page import LastFmLandingPage
from pages.lastfm_results_page import LastfmResultsPage
from pages.lastfm_artist_page import LastfmArtistPage


@given("el usuario se encuentra en last.fm")
def step_landing_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_landing = LastFmLandingPage(context.driver)


@when('el usuario busca el artista "{artist_name}"')
def step_search_artist(context, artist_name):
    context.lastfm_landing.search_artist(artist_name)
    context.lastfm_results = LastfmResultsPage(context.driver)


@when('selecciona el primer resultado "{artist_name}"')
def step_select_first_result(context, artist_name):
    context.lastfm_results.go_to_artist(artist_name)
    context.lastfm_artist = LastfmArtistPage(context.driver)


@then('se muestra en la pantalla del artista la fecha de ultimo lanzamiento "{expected_date}"')
def step_validate_release_date(context, expected_date):
    actual = context.lastfm_artist.get_latest_release_date()
    assert actual == expected_date, f"Fecha de ultimo lanzamiento erronea: {actual}"
