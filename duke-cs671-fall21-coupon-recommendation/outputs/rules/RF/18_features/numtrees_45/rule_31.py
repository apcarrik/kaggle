def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]>1:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[3]>1:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[17]<=1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]<=3:
					return 'True'
				elif obj[6]>3:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[17]>1:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[11]<=1:
		return 'False'
	else: return 'False'
