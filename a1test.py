"""
	Name 		  : Raghav Dev Kukreti
	Roll No 	  : 2017082
	Section-Group : B1

"""
import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_weather_response(self):
		self.assertEqual(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"))
	
	def test_has_error(self):
		# self.assertTrue()
		self.assertTrue(has_error('California', weather_response("Noida","55caddfec6f90b2b717bb37ceab8abb0")))
		self.assertTrue(has_error('D', weather_response("Noida","55caddfec6f90b2b717bb37ceab8abb0")))
		self.assertTrue(has_error('Delhi', weather_response("Noida","55caddfec6f90b2b717bb37ceab8abb0")))
		self.assertTrue(has_error('Ghaziabad', weather_response("Noida","55caddfec6f90b2b717bb37ceab8abb0")))
		self.assertTrue(has_error('Faridabad', weather_response("Noida","55caddfec6f90b2b717bb37ceab8abb0")))

	def test_get_temperature(self):
		self.assertAlmostEqual(get_temperature(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 1), 300 ,delta=50)
		self.assertAlmostEqual(get_temperature(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "03:00:00", 0), 300 ,delta=50)
		self.assertAlmostEqual(get_temperature(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "06:00:00", 3), 298 ,delta=50)
		self.assertAlmostEqual(get_temperature(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "12:00:00", 2), 300 ,delta=50)
		self.assertAlmostEqual(get_temperature(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "21:00:00", 4), 300 ,delta=50)
	
	def test_get_humidity(self):
		self.assertAlmostEqual(get_humidity(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 3), 95 ,delta=50)
		self.assertAlmostEqual(get_humidity(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 2), 95 ,delta=50)
		self.assertAlmostEqual(get_humidity(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 2), 95 ,delta=50)
		self.assertAlmostEqual(get_humidity(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 4), 95 ,delta=50)
		self.assertAlmostEqual(get_humidity(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 0), 95 ,delta=50)

	def test_get_pressure(self):
		self.assertAlmostEqual(get_pressure(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 3), 1000 ,delta=50)
		self.assertAlmostEqual(get_pressure(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 4), 1000 ,delta=50)
		self.assertAlmostEqual(get_pressure(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 0), 1000 ,delta=50)
		self.assertAlmostEqual(get_pressure(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 3), 1000 ,delta=50)
		self.assertAlmostEqual(get_pressure(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 2), 1000 ,delta=50)


	def test_get_wind(self):
		self.assertAlmostEqual(get_wind(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 1), 10 ,delta=50)
		self.assertAlmostEqual(get_wind(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "03:00:00", 0), 10 ,delta=50)
		self.assertAlmostEqual(get_wind(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "06:00:00", 3), 10 ,delta=50)
		self.assertAlmostEqual(get_wind(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "12:00:00", 2), 10 ,delta=50)
		self.assertAlmostEqual(get_wind(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "21:00:00", 4), 10 ,delta=50)

	def test_get_sealevel(self):
		self.assertAlmostEqual(get_sealevel(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "00:00:00", 1), 1000 ,delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "03:00:00", 1), 1000 ,delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "06:00:00", 3), 1000 ,delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "12:00:00", 0), 1000 ,delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response("Delhi","55caddfec6f90b2b717bb37ceab8abb0"), "21:00:00", 4), 1000 ,delta=50)

	
if __name__=='__main__':
	unittest.main()
