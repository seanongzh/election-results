# Election Results Database
A searchable database of historical U.S. election results at the municipal level. Suitable for tracking local politics and voting trends. 

## Data types
- Candidates: name; party affiliation.
- Positions: name; level of government at which they operate (municipal, county, state, and national).
- Elections: year; position; special election or not.
- Results: election; candidate; incumbent or not; "overall winner" or not (where the candidate may have won the overall race but not locally or vice versa).

## Implementation
Using Django and postgresql. Comes with full-text search based on [Watson](https://github.com/etianen/django-watson), a Django search plugin. 

### Alpha version
Currently utilizing a set of historical election results from Kenilworth, NJ. Compiled via open source.

## License
This project is licensed under the terms of the MIT license.