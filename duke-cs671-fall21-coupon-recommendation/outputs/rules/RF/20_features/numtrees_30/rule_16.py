def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Gender", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[7]<=0:
		# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[16]<=2.0:
			# {"feature": "Weather", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Time", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[10]>0:
						return 'True'
					elif obj[10]<=0:
						# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=1:
							return 'False'
						elif obj[9]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		elif obj[16]>2.0:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>55:
					return 'False'
				elif obj[3]<=55:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[7]>0:
		# {"feature": "Time", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[4]<=3:
			return 'True'
		elif obj[4]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
