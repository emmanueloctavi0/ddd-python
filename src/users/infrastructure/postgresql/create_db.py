import os
import sys

# Set the path to the current directory
# to avoid the error of the relative path
cwd = os.getcwd()
sys.path.insert(0, cwd)

from users.infrastructure.postgresql import db
from users.infrastructure.postgresql import models


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
