import unittest
import requests
booking_url="http://localhost:3001/"
movies_url="http://localhost:3002/"
user_url="http://localhost:3000/"

class myunittests(unittest.TestCase):
    def test_bookings(self):
        result=requests.get(booking_url+"/booking/chris_rivers").json()
        self.assertTrue(result['20151201'][0]=="267eedb8-0f5d-42d5-8f43-72426b9fb3e6")
    
    def test_movies(self):
        result=requests.get(movies_url+"/movie/720d006c-3a57-4b6a-b18f-9b713b073f3c").json()
        self.assertTrue(result['title']=="The Good Dinosaur")
    
    def test_user(self):
        result=requests.get(user_url+"/users/chris_rivers/bookings").json()
        print(result)
        self.assertTrue(result['20151201']['title']=="Creed")
if __name__=='__main__':
    unittest.main()

