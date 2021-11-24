def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=6:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[4]>1:
			# {"feature": "Bar", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[13]<=2.0:
				return 'True'
			elif obj[13]>2.0:
				# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]>55:
					return 'False'
				elif obj[2]<=55:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[3]<=1:
				# {"feature": "Temperature", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[2]<=55:
					# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[12]<=7:
						return 'False'
					elif obj[12]>7:
						return 'True'
					else: return 'True'
				elif obj[2]>55:
					return 'True'
				else: return 'True'
			elif obj[3]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[7]>6:
		return 'False'
	else: return 'False'
