Feature: Correcta calificacion de pelicula en IMDb
    Scenario: Validar titulo y calificacion de Inception
        Given el usuario se encuentra en IMDb
        When el usuario busca la pelicula "Inception"
        And selecciona el primer resultado
        Then se muestra el titulo "Origen"
        And la calificacion es mayor a "8"
