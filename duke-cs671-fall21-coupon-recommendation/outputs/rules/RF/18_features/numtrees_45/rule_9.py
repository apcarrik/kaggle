def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]>1:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[17]<=1:
			# {"feature": "Weather", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Gender", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[17]>1:
			# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[11]<=1:
		return 'False'
	else: return 'False'
