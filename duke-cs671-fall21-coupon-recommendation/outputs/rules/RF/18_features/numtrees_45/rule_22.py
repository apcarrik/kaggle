def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]<=4:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[3]>2:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[3]<=2:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[10]<=12:
				# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[14]>1.0:
					return 'True'
				elif obj[14]<=1.0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>12:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]>4:
		return 'True'
	else: return 'True'
