#!/bin/bash

export SECRET_KEY="your secret key"
export DATABASE_URI="mysql+mysqldb://root:${PASS}@localhost:3306/companyservice"
export FLASK_APP=app
export FLASK_ENV=development