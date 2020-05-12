from login import *
from download_movie import *
from ssq import *
from read import *
from insert import *
from sql_1 import *
from sql_2 import *
from sql_3 import *
from sql_4 import *
from sql_5 import *
from sql_6 import *
from sql_7 import *
from sql_8 import *
from sql_9 import *
from sql_10 import *
app = Flask(__name__)
get_ssq_num(app)
login(app)
download_movie(app)
inserts(app)
seq1(app)
seq2(app)
seq3(app)
seq4(app)
seq5(app)
seq6(app)
seq7(app)
seq8(app)
seq9(app)
seq10(app)
app.run()