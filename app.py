#all the libraries*********************************************
#****************************************************************
from flask import Flask, jsonify, request
import pymysql
import datetime
from flask_restful import Resource, Api
import random
import functools

#***********************************************************************

#initialize the main app********************************************
app = Flask(__name__)
api = Api(app)


# class initialization********************************************
class Getsensor(Resource):
    def get(self):
        db =pymysql.connect("remotemysql.com","cpemK6oAPi","xaypaRGy7e","cpemK6oAPi")
        cursor = db.cursor()
        query = """SELECT * FROM sensor_tbl"""
        cursor.execute(query)
        data = cursor.fetchall()
        payload = []
        content = {}
        for row in data:
            print(row)
            content = { 'sensor_data': row[1], 'data_desc': row[2]}
            payload.append(content)
        db.close()
        return jsonify(payload)

   

class Postsensor(Resource):
     def post(self):
        some_json = request.get_json()
        db = pymysql.connect("remotemysql.com","cpemK6oAPi","xaypaRGy7e","cpemK6oAPi")
        cursor = db.cursor()
        query = """insert into sensor_tbl(sensor_data,data_desc) values({},'{}')""".format(some_json["sensor_data"],some_json["data_desc"])
        print(query)
        cursor.execute(query)
        db.commit()
        return{'response': "record inserted successfully!"},202


api.add_resource(Getsensor, '/sensor/api/V1.0/data')
api.add_resource(Postsensor, '/sensor/api/V1.0/data')


if __name__ == "__main__":
    app.run(debug=True)
    
