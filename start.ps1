jupyter nbconvert --to notebook --inplace --execute notebooks/scraper.ipynb;
uvicorn main:app --reload
