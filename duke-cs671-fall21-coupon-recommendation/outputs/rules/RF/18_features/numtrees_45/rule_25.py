def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]>0:
		# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[11]>3:
			# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[10]<=7:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[17]<=1:
					return 'True'
				elif obj[17]>1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0:
							return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[10]>7:
				return 'False'
			else: return 'False'
		elif obj[11]<=3:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
