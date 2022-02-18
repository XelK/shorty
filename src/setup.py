
import flask


if "__name__" == "__main__":
    # — to initialize the database at the beginning (to be used only once)
    flask db init 
    #— to migrate the new changes to the database (to be used every time we make changes in the database tables)
    flask db migrate 
    # — to upgrade our database with the new changes (to be used with the migrate command)
    flask db upgrade 
