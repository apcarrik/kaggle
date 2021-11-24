def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=5:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[3]>0:
			# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[6]>0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[17]>1:
					# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				elif obj[17]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[11]>5:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[3]<=3:
			return 'True'
		elif obj[3]>3:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
