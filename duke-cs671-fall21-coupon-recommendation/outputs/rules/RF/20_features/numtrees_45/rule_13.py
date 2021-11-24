def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[4]>0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]<=0:
					return 'True'
				elif obj[7]>0:
					# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=55:
						return 'False'
					elif obj[3]>55:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[5]>2:
		# {"feature": "Driving_to", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[9]<=0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[19]>1:
						return 'False'
					elif obj[19]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[9]>0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
