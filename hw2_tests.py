import data
import hw2
import unittest

from hw2 import create_rectangle, shorter_duration_than, song_shorter_than, running_time, longest_repetition


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        p1 = data.Point(2,2)
        p2 = data.Point(10,10)
        input = create_rectangle(p1,p2)
        expected = data.Rectangle(data.Point(2,10),data.Point(10,2))
        self.assertEqual(input,expected)

    def test_create_rectangle2(self):
        p1 = data.Point(4,5)
        p2 = data.Point(7,8)
        input = create_rectangle(p1,p2)
        expected = data.Rectangle(data.Point(4,8),data.Point(7,5))
        self.assertEqual(input,expected)

    # Part 2
    def test_shorter_duration_than1(self):
        d1 = data.Duration(5,30)
        d2 = data.Duration(4,30)
        input = shorter_duration_than(d1,d2)
        expected = False
        self.assertEqual(input,expected)

    def test_shorter_duration_than2(self):
        d1 = data.Duration(5,30)
        d2 = data.Duration(4,30)
        input = shorter_duration_than(d1,d2)
        expected = False
        self.assertEqual(input,expected)


    # Part 3
    def test_songs_shorter_than1(self):
        s1 = data.Song("Lady Gaga and Bruno Mars","Die with a smile", data.Duration(4,11))
        s2 = data.Song("Billie Eilish", "Wildflower",data.Duration(4,21))
        s3 = data.Song("Kanye west","Carnival",data.Duration(4,24))
        songs = [s1,s2,s3]
        compDuration = data.Duration(4,20)
        input = song_shorter_than(songs,compDuration)
        expected = [data.Song("Lady Gaga and Bruno Mars","Die with a smile", data.Duration(4,11))]
        self.assertEqual(input,expected)

    def test_songs_shorter_than2(self):
        s1 = data.Song("Taylor swift","All too well", data.Duration(10,13))
        s2 = data.Song("Rolling Stones", "Come on",data.Duration(1,48))
        s3 = data.Song("Kanye west","Carnival",data.Duration(4,24))
        songs = [s1,s2,s3]
        compDuration = data.Duration(5,15)
        input = song_shorter_than(songs,compDuration)
        expected = [data.Song("Rolling Stones", "Come on",data.Duration(1,48)),  data.Song("Kanye west","Carnival",data.Duration(4,24))]
        self.assertEqual(input,expected)

    # Part 4
    def test_running_time1(self):
        s1 = data.Song("Lady Gaga and Bruno Mars", "Die with a smile", data.Duration(4, 11))
        s2 = data.Song("Billie Eilish", "Wildflower", data.Duration(4, 21))
        s3 = data.Song("Kanye west", "Carnival", data.Duration(4, 24))
        songs = [s1,s2,s3]
        ints = [0,2,2]
        input  = running_time(songs,ints)
        expected = data.Duration(12,59)
        self.assertEqual(input,expected)

    def test_running_time2(self):
        s1 = data.Song("Lady Gaga and Bruno Mars", "Die with a smile", data.Duration(6, 7))
        s2 = data.Song("Billie Eilish", "Wildflower", data.Duration(10, 21))
        s3 = data.Song("Kanye west", "Carnival", data.Duration(6, 24))
        songs = [s1,s2,s3]
        ints = [0,2,2]
        input  = running_time(songs,ints)
        expected = data.Duration(18,55)
        self.assertEqual(input,expected)

    # Part 5
    def test_validate_route1(self):
            links = [["A", "B"], ["C", "D"], ["E", "F"]]
            names = ["A", "C", "E"]
            input = hw2.validate_route(links,names)
            expected = False
            self.assertEqual(input,expected)

    def test_validate_route2(self):
        city_links =[
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['pismo beach','atascadero'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]

        names = ['san luis obispo','santa margarita','pismo beach','atascadero','creston']
        expected = hw2.validate_route(city_links,names)
        result = True
        self.assertEqual(expected,result)




    # Part 6
    def test_longest_repetition1(self):
        ints = [3,3,3,4,4,5,6,1,1,1,1]
        input = longest_repetition(ints)
        expected = 7
        self.assertEqual(input,expected)

    def test_longest_repetition2(self):
        ints = [1,1,2,2,3,3,3,4,4,4,4,5,6]
        input = longest_repetition(ints)
        expected = 7
        self.assertEqual(input,expected)



if __name__ == '__main__':
    unittest.main()
