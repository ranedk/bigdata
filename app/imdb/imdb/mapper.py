from core.models import (
    Genre,
    Format,
    Region,
    Language,
    Profession,
    Category,
    Title,
    TitleAka,
    Person,
    Crew,
    Principal,
    Rating,
    Episode
)


def read_file(filename):
    lines = open(filename).read().split("\n")
    return lines


def parse_title_basics(lines):
    """
    tconst: title_id
    titleType: title_format
    primaryTitle: primary_title
    originalTitle: original_title
    isAdult: is_adult
    startYear: start_year
    endYear: end_year
    runtimeMinutes: runtime_minutes
    genres: genres
    """
    for l in lines:
        (
            title_id,
            title_format,
            primary_title,
            original_title,
            is_adult,
            start_year,
            end_year,
            runtime_minutes,
            genres,
        ) = l.split("\t")

        title_format = Format.objects.get_or_create(
            name=title_format.strip().lower()
        )

        genres = [
            Genre.objects.get_or_create(name=genre.strip().lower())
            for genre in genres.split(",")
        ]

        if not Title.objects.exists(title_id=title_id):
            title = Title.objects.create(
                title_id=title_id,
                title_format=title_format,
                primary_title=primary_title,
                original_title=original_title,
                is_adult=is_adult,
                start_year=start_year,
                end_year=end_year,
                runtime_minutes=runtime_minutes,
            )
            title.genres.add(*genres)


def parse_title_akas(lines):
    """
    titleId: title_id
    ordering: ordering,
    title: name
    region: region
    language: language
    types: ttypes
    attributes: attributes
    isOriginalTitle: is_original_title
    """
    for l in lines:
        (
            title_id,
            ordering,
            name,
            region,
            language,
            ttypes,
            attributes,
            is_original_title,
        ) = l.split("\t")

        title = Title.objects.get(title_id=title_id)
        region = Region.objects.get_or_create(name=region)
        language = language.objects.get_or_create(name=language)

        if not TitleAka.objects.exists(title=title):
            title_aka = TitleAka.objects.create(
                title=title,
                ordering=ordering,
                name=name,
                region=region,
                language=language,
                ttypes=ttypes,
                attributes=attributes,
                is_original_title=is_original_title,
            )


def parse_name_basics(lines):
    """
    nconst: person_id
    primaryName: name
    birthYear: birth_year
    deathYear: death_year
    primaryProfession: professions
    knownForTitles: titles
    """
    for l in lines:
        (
            person_id,
            name,
            birth_year,
            death_year,
            professions,
            titles
        ) = l.split("\t")

        titles = [
            Title.objects.get(title_id=title_id.strip().lower())
            for title_id in titles.split(",")
        ]
        professions = [
            Profession.objects.get_or_create(name=profession.strip().lower())
            for profession in professions.split(",")
        ]

        if not Person.objects.exists(person_id=person_id):
            person = Person.objects.create(
                person_id=person_id,
                name=name,
                birth_year=birth_year,
                death_year=death_year
            )
            person.professions.add(*professions)
            person.titles.add(*titles)


def title_crew(lines):
    """
    tconst: title_id
    directors: directors
    writers: writers
    """
    for l in lines:
        (
            title_id,
            directors,
            writers
        ) = l.split("\t")

        title = Title.objects.get(title_id=title_id.strip().lower())
        directors = [
            Person.objects.get(person_id=director.strip().lower())
            for director in directors.split(",")
        ]
        writers = [
            Person.objects.get(person_id=writer.strip().lower())
            for writer in writers.split(",")
        ]

        crew = Crew.objects.get_or_create(title=title)
        crew.directors.add(*directors)
        crew.writers.add(*writers)


def title_principals(lines):
    """
    tconst: title_id
    ordering: ordering
    nconst: person_id
    category: category
    job: job
    characters: characters
    """
    for l in lines:
        (
            title_id,
            ordering,
            person_id,
            category,
            job,
            characters
        ) = l.split("\t")

        title = Title.objects.get(title_id=title_id.strip().lower())
        person = Person.objects.get(person_id=person_id)
        category = Category.objects.get_or_create(name=category)

        if not Principal.objects.exists(title=title, person=person):
            Principal.objects.create(
                title=title,
                ordering=ordering,
                person=person,
                category=category,
                job=job,
                characters=characters
            )


def title_episode(lines):
    """
    tconst: title_id
    parentTconst: parent_title_id
    seasonNumber: season_number
    episodeNumber: episode_number
    """
    for l in lines:
        (
            title_id,
            parent_title_id,
            season_number,
            episode_number
        ) = l.split("\t")

        title = Title.objects.get(title_id=title_id.strip().lower())
        parent_title = Title.objects.get(title_id=parent_title_id.strip().lower())

        if Episode.object.exists(title=title):
            Episode.objects.create(
                title=title,
                parent_title=parent_title,
                season_number=season_number,
                episode_number=episode_number
            )


def title_rating(lines):
    """
    tconst: title_id
    averageRating: avg_rating
    numVotes: number_of_votes
    """
    for l in lines:
        (
            title_id,
            avg_rating,
            number_of_votes
        ) = l.split("\t")

        title = Title.objects.get(title_id=title_id.strip().lower())

        if Rating.object.exists(title=title):
            Rating.objects.create(
                title=title,
                avg_rating=avg_rating,
                number_of_votes=number_of_votes
            )


