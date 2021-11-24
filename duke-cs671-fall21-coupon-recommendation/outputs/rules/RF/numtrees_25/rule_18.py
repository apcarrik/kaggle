def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 41, "metric_value": 0.9892, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[10]<=0:
				return 'True'
			elif obj[10]>0:
				# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=55:
					return 'False'
				elif obj[3]>55:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>0:
			# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[17]<=2.0:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>30:
						return 'False'
					elif obj[3]<=30:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[17]>2.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[11]>1:
			return 'False'
		elif obj[11]<=1:
			# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=1:
				return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
