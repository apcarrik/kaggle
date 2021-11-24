def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]>0:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[18]>1:
			# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[12]<=6:
					return 'True'
				elif obj[12]>6:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>1:
				return 'False'
			else: return 'False'
		elif obj[18]<=1:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[11]>1:
				return 'False'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0:
		return 'False'
	else: return 'False'
