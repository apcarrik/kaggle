def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon_validity", "instances": 44, "metric_value": 0.9257, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Income", "instances": 26, "metric_value": 0.6194, "depth": 3}
			if obj[13]<=6:
				# {"feature": "Passanger", "instances": 21, "metric_value": 0.2762, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[13]>6:
				# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[7]>0:
					return 'False'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>0:
			# {"feature": "Driving_to", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[0]<=0:
				# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[8]<=5:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[12]>4:
						return 'False'
					elif obj[12]<=4:
						return 'True'
					else: return 'True'
				elif obj[8]>5:
					return 'True'
				else: return 'True'
			elif obj[0]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]<=0:
		# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]<=1:
			return 'False'
		elif obj[2]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
