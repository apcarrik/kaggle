def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Restaurantlessthan20", "instances": 25, "metric_value": 0.9988, "depth": 2}
		if obj[16]<=2.0:
			# {"feature": "Temperature", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[3]>55:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[7]>0:
					return 'False'
				elif obj[7]<=0:
					# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[13]>1:
						return 'True'
					elif obj[13]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=55:
				return 'False'
			else: return 'False'
		elif obj[16]>2.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[12]<=8:
				return 'True'
			elif obj[12]>8:
				# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]>2:
		return 'True'
	else: return 'True'
