from database.crud import crud



if __name__ == '__main__':
    crud.start(drop_tables=False)