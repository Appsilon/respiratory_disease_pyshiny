# Respiratory Disease: PyShiny Version

This repository contains the result of the py-shiny app-sprint. The goal of this sprint was to "translate" an R/Shiny application into a "Shiny for Python" one, as well as to explore some PyShiny-specific features. Kindly find all the information about the original app in its [repository](https://github.com/Appsilon/respiratory_disease_app_sprint).

## Explore the app
The "normal" app is deployed at [Appsilon RSConnect](https://connect.appsilon.com/respiratory_disease_pyshiny/). The WASM version aka Shinylive is deployed at https://connect.appsilon.com/respiratory_disease_shinylive/. Please not that for a ShinyLive application a large bundle has to be downloaded which can take some time (but it will be cached and used later even without an internet connection).

To run the app locally, clone the repo, create a virtual environment, install the dependencies and run the app and navigate to `localhost:8000` in the browser:

```shell
git clone git@github.com:Appsilon/respiratory_disease_pyshiny.git
cd ./respiratory_disease_pyshiny
python -m virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
shiny run --port 8000 app.py
```

## Key Results
TBD: A comprehensive summary of the sprint is to be published in a blog post (WIP).

- Most of the original structure/logic has been preserved, unless a direct translation was impossible
- Some UI changes have been introduced
  - Grid layout
  - Mobile responsiveness
  - Workaround for dataset switch
- A working Shinylive version of the app was created

## Challenges
- Lack of any UI-component libraries
- `ipyleaflet` lacks features of its R counterpart, and documentation is not helpful
- Issues with CPU throttling
- Shinylive version is very sensitive to the packages in requirements.txt. Problems with packages like `geopandas`.
