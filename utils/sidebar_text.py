from htmltools import TagList, tags

about_text = TagList(
    tags.h3("About"),
    tags.br(),
    tags.p(
        """
        The app gives a visual overview of PM2.5 air pollution
        for different
        countries over the years and its potential relationship
        to respiratory
        diseases and their prevalence.
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

slider_text = TagList(
    tags.p(
        """
        Please use the slider below to choose the year. The map will
        reflect data for the input
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    )
)

dataset_information = TagList(
    tags.strong(tags.h3("Dataset Information")),
    tags.p(
        """
        For the app, we have chosen data from the World Bank and
        Organisation for Economic Co-operation and Development (OECD).
        Also, for the data regarding the Death Rate, we relied on
        Our World in Data. References
        to all three can be found below.
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.ul(
        tags.li(
            tags.a(
                "World Bank",
                href=(
                    "https://data.worldbank.org/indicator/"
                    + "EN.ATM.PM25.MC.M3"
                ),
            )
        ),
        tags.li(
            tags.a(
                "OECD",
                href=(
                    "https://stats.oecd.org/"
                    + "Index.aspx?DataSetCode=EXP_PM2_5"
                ),
            )
        ),
        tags.li(
            tags.a(
                "Our World in Data",
                href=(
                    "https://ourworldindata.org/"
                    + "grapher/respiratory-disease-death-rate"
                ),
            )
        ),
    ),
)

missing_note = TagList(
    tags.p(
        tags.strong("Note: "),
        """
        For years 1990 to 2010, the PM2.5 data was collected
        at every
        five-year mark. That is, the PM2.5 data is only
        available for
        1990, 1995, 2000, 2005, 2010, and 2010 onwards.
        """,
        style="""
        font-size: 14px;
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)
