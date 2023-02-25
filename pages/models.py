from django.db import models
import json
from pages.model.money import Money
from pages.model.receipt import Receipt
from pages.model.people import People

# Create your models here.
with open('./pages/json/monetaryUnit.json', 'r') as f:
    monetaryUnit = json.load(f)
    print(f)
class ReceiptInfo(models.Model):

    meetingTitle = ""
    meetingDate = '2023-02-11'
    receiptInfoList = []
    usedMoneyList = []
    unusedMoneyList = []
    monetaryUnit = ""
    participantList = []
    nonParticipantList = []

    def __init__(self):
        # with open('./pages/json/receiptInfoList.json', 'r') as receipt:
        #     self.receiptInfolist = json.load(receipt)

        self.meetingTitle =  '모임명'

        self.meetingDate = '0000-00-00'

        self.receiptInfoList = [Receipt(4, "가게", "메뉴", 200000).get()]

        # self.unusedMoneyList.append(Money("계금액", "22년 07월 ~ 23년 02월", 600000).get())
        self.unusedMoneyList = [Money("계금액", "00년 00월 ~ 0x년 0x월", 600000).get()]

        self.participantList = [
                                People("사람1").get(),
                                People("사람2").get(),
                                People("사람3").get(),
                                People("사람4").get(),
        ]

        self.nonParticipantList = [
                   People("사람5").get()
        ]


        # with open('./pages/json/unusedMoneyList.json', 'r') as money:
        #     self.unusedMoneyList = json.load(money)
    def usedMoneyList(self):
        usedMoneyList = []

        useMoney = 0

        for receiptInfo in self.receiptInfoList:
            for i in range(0, receiptInfo['amount']):
                useMoney += receiptInfo['price']

        usedMoneyList.append(
            Money('식당', '사용 금액', useMoney).get()
        )
        usedMoneyList.append(
            Money('기타', '미 참여자 환불 금액', 200000).get()
        )

        return usedMoneyList

    def get(self):
        return {
            'meetingTitle' : self.meetingTitle
            , 'meetingDate' : self.meetingDate
            , 'receiptInfoList' : self.receiptInfoList
            , 'usedMoneyList' : self.usedMoneyList()
            , 'unusedMoneyList' : self.unusedMoneyList
            , 'monetaryUnit' : monetaryUnit["kor"]
            , 'participantList' : self.participantList
            , 'nonParticipantList' : self.nonParticipantList
        }