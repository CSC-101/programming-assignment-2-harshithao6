import data
import hw2
import unittest

from hw2 import create_rectangle, shorter_duration_than, song_shorter_than, running_time, longest_repetition


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        p1 = data.Point(2,2)
        p2 = data.Point(10,10)
        input = create_rectangle(p1,p2)
        newp1 = data.Point(2,10)
        newp2 = data.Point(10,2)
        expected = data.Rectangle(newp1,newp2)
        self.assertEqual(input,expected)

    # Part 2
    def test_shorter_duration_than(self):
        d1 = data.Duration(5,30)
        d2 = data.Duration(4,30)
        input = shorter_duration_than(d1,d2)
        expected = False
        self.assertEqual(input,expected)


    # Part 3
    def test_songs_shorter_than(self):
        s1 = data.Song("Lady Gaga and Bruno Mars","Die with a smile", data.Duration(4,11))
        s2 = data.Song("Billie Eilish", "Wildflower",data.Duration(4,21))
        s3 = data.Song("Kanye west","Carnival",data.Duration(4,24))
        songs = [s1,s2,s3]
        compDuration = data.Duration(4,20)
        input = song_shorter_than(songs,compDuration)
        expected = [s1,s2]
        self.assertEqual(input,expected)

    # Part 4
    def test_running_time(self):
        s1 = data.Song("Lady Gaga and Bruno Mars", "Die with a smile", data.Duration(4, 11))
        s2 = data.Song("Billie Eilish", "Wildflower", data.Duration(4, 21))
        s3 = data.Song("Kanye west", "Carnival", data.Duration(4, 24))
        songs = [s1,s2,s3]
        ints = [0,2,2]
        input  = running_time(songs,ints)
        expected = data.Duration(12,59)
        self.assertEqual(input,expected)

    # Part 5


    # Part 6
    def test_longest_repetition(self):
        ints = [3,3,3,4,4,5,6,1,1,1,1]
        input = longest_repetition(ints)
        expected = 7
        self.assertEqual(input,expected)




if __name__ == '__main__':
    unittest.main()
