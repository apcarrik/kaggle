def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[2]<=11:
		# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.9734, "depth": 2}
		if obj[3]<=3.0:
			# {"feature": "Education", "instances": 45, "metric_value": 0.9565, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 43, "metric_value": 0.9682, "depth": 4}
				if obj[4]>1:
					# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Coupon", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]>3.0:
			return 'False'
		else: return 'False'
	elif obj[2]>11:
		return 'False'
	else: return 'False'
