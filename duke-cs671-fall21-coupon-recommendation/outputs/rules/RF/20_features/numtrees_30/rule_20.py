def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[8]>1:
		# {"feature": "Bar", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[6]>0:
				return 'False'
			elif obj[6]<=0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[16]<=2.0:
						return 'True'
					elif obj[16]>2.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[14]>1.0:
			# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[3]>55:
				return 'True'
			elif obj[3]<=55:
				# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[8]<=1:
		# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[13]<=4:
			return 'True'
		elif obj[13]>4:
			# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
