def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.994, "depth": 2}
		if obj[0]>0:
			# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[2]<=7:
					return 'True'
				elif obj[2]>7:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=0:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=6:
				return 'False'
			elif obj[2]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>3:
		return 'False'
	else: return 'False'
