from behave import given, when, then
from selenium import webdriver
from pages.imdb_landing_page import ImdbLandingPage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage


@given("el usuario se encuentra en IMDb")
def step_imdb_landing(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com")
    context.imdb_landing = ImdbLandingPage(context.driver)


@when('el usuario busca la pelicula "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_landing.search_movie(movie_name)
    context.imdb_results = ImdbResultsPage(context.driver)


@when('selecciona el primer resultado')
def step_select_first_result(context):
    context.imdb_results.go_to_first_result()
    context.imdb_movie = ImdbMoviePage(context.driver)


@then('se muestra el titulo "{expected_title}"')
def step_validate_title(context, expected_title):
    actual = context.imdb_movie.get_title()
    assert actual == expected_title, f"Titulo incorrecto: {actual}"


@then('la calificacion es mayor a "{min_rating}"')
def step_validate_rating(context, min_rating):
    actual = context.imdb_movie.get_rating()
    assert float(actual.replace(",", ".")) > float(min_rating), f"Calificacion incorrecta: {actual}"
