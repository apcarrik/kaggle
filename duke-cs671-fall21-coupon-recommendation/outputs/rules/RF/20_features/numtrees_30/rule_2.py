def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[11]>0:
		# {"feature": "Children", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[10]<=0:
			# {"feature": "Income", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[13]<=6:
				return 'False'
			elif obj[13]>6:
				return 'True'
			else: return 'True'
		elif obj[10]>0:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[11]<=0:
		# {"feature": "Passanger", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[13]<=6:
				# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]>55:
					return 'True'
				elif obj[3]<=55:
					# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]>6:
				return 'False'
			else: return 'False'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	else: return 'True'
