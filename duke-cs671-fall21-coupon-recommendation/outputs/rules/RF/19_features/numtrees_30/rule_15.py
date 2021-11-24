def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[14]>0.0:
		# {"feature": "Gender", "instances": 25, "metric_value": 0.971, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[16]>-1.0:
				# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[8]<=1:
					return 'True'
				elif obj[8]>1:
					# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=55:
						return 'True'
					elif obj[2]>55:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[16]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[6]>0:
			# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[3]<=3:
				return 'False'
			elif obj[3]>3:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[10]<=2:
					return 'True'
				elif obj[10]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[14]<=0.0:
		# {"feature": "Temperature", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]>30:
			return 'False'
		elif obj[2]<=30:
			return 'True'
		else: return 'True'
	else: return 'False'
