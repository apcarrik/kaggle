def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[11]>9:
			return 'False'
		elif obj[11]<=9:
			# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[10]>0:
					# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[15]<=3.0:
						return 'False'
					elif obj[15]>3.0:
						return 'True'
					else: return 'True'
				elif obj[10]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>1:
		# {"feature": "Income", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[12]>2:
			# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=55:
						return 'True'
					elif obj[2]>55:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			elif obj[6]>0:
				return 'True'
			else: return 'True'
		elif obj[12]<=2:
			return 'True'
		else: return 'True'
	else: return 'True'
