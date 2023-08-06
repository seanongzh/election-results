# Election Results Database
**Alpha version:** A searchable database of historical U.S. election results at the municipal level. Suitable for tracking local politics and voting trends. 

## Data types
- Candidates are stored by name and party affiliation.
- Positions are stored by name and the level of government at which they operate: currently set as municipal, county, state, and national.
- Elections are stored by year and position, with the option to set it as a special election that filled a vacant seat.
- Results are stored by election and candidate, with the option to indicate that the candidate was an incumbent and/or "won" the overall race but not at the local level, in cases where the municipality has different political leanings than higher levels of government.

## Implementation
Using Django and postgresql. Comes with full-text search based on [Watson](https://github.com/etianen/django-watson), a Django search plugin. 

## License
This project is licensed under the terms of the MIT license.