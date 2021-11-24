def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Weather", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Temperature", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[3]>55:
			# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[14]<=0.0:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[15]<=2.0:
					return 'False'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			elif obj[14]>0.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=55:
			return 'True'
		else: return 'True'
	elif obj[2]>1:
		# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
