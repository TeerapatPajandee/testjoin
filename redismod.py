from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Init app
app = Flask(__name__)

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://webadmin:TGPboi81761@10.100.2.203:5432/join"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

###############################################################################
#member Class/Model
class member(db.Model):
    id = db.Column(db.String(10), primary_key=True, unique=True)
    name = db.Column(db.String(25))
    Tel = db.Column(db.String(10))
    def __init__(self, id, name, Tel):
        self.id = id
        self.name = name
        self.Tel = Tel

# member Schema
class MemberSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'Tel')

# Init Schema 
memberSchema = MemberSchema()
memberSchema = MemberSchema(many=True)

# Get Member
@app.route('/member', methods=['GET'])
def get_staffs():
    all_staffs = member.query.all()
    result = memberSchema.dump(all_staffs)
    return jsonify(result)

################################################################################
#train_ticket Class/Model
class train_ticket(db.Model):
    id = db.Column(db.String(10), primary_key=True, unique=True)
    typecard = db.Column(db.String(25))
    codestart = db.Column(db.String(10))
    codeend = db.Column(db.String(10))
    def __init__(self, id, typecard, codestart, codeend):
        self.id = id
        self.typecard = typecard
        self.codestart = codestart
        self.codeend = codeend

# member Schema
class TrainSchema(ma.Schema):
    class Meta:
        fields =('id', 'typecard', 'codestart', 'codeend')

# Init Schema 
trainSchema = TrainSchema()
trainSchema = TrainSchema(many=True)

# Get ticket
@app.route('/ticket', methods=['GET'])
def get_ticket():
    train = train_ticket.query.all()
    result = trainSchema.dump(train)
    return jsonify(result)

###############################################################################
## JOIN ##











# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud DB1'})

# Run Server
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
