import __init__
from models.database import engine
from models.model import Subscription
from sqlmodel import Session
from datetime import date

class SubscriptionSevice:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription

ss = SubscriptionSevice(engine)
subscription = Subscription(empresa='Netflix', site='Netflix.com.br', data_assinatura=date.today(), valor=29)
ss.create(subscription)