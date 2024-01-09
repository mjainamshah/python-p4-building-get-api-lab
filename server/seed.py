#!/usr/bin/env python3

from random import choice as rc

from app import app
from models import db, Bakery, BakedGood

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    bakeries.append(Bakery(name='Delightful donuts'));
    bakeries.append(Bakery(name='Incredible crullers'));
    db.session.add_all(bakeries)

    baked_goods = []
    baked_goods.append(BakedGood(name='Chocolate dipped donut', price=2, bakery_id=1));
    baked_goods.append(BakedGood(name='Apple-spice filled donut', price=3, bakery_id=1));
    baked_goods.append(BakedGood(name='Glazed honey cruller', price=3, bakery_id=2));
    baked_goods.append(BakedGood(name='Chocolate cruller', price=3, bakery_id=2));

    db.session.add_all(baked_goods)
    db.session.commit()
