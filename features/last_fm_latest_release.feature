Feature: Correcta fecha de ultimo lanzamiento
    Scenario: Validar la fecha del ultimo lanzamiento de Bruno Mars
        Given el usuario se encuentra en last.fm
        When el usuario busca el artista "Bruno Mars"
        And selecciona el primer resultado "Bruno Mars"
        Then se muestra en la pantalla del artista la fecha de ultimo lanzamiento "8 May 2026"
  